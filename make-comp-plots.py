from bs4 import BeautifulSoup
import requests
import pandas as pd
import re
import os, fnmatch
import plotly.graph_objects as go
from datetime import date

def parse_table(url, timelimit=3600):
    """
    parse a specific table to generate a dictionary with the runtimes and
    auxiliary information
    """
    resp = requests.get(url) 
    soup = BeautifulSoup(resp.text, features="html.parser")
    pre = soup.find_all('pre')
    
    stats = {}
    
    stats['date'] = pre[0].text.split('\n')[1].replace('=','').replace('-','').strip()
    stats['title'] = pre[0].text.split('\n')[2].strip()

    if url.find('lpsimp') >= 0:
        tab = pre[3].text.split('\n')
        _version = pre[2].text.split('\n')[1:-1]
        _version = [x.split()[0].rstrip(':') for x in _version]
        _score = tab[3].split()
        _solved = tab[4].split()[1:]
        solver = tab[6].split()[2:]
        stats['solver'] = solver
        nprobs = int(tab[6].split()[0])
        stats['nprobs'] = nprobs
        stats['score'] = {solver[i]:float(_score[i]) for i in range(len(solver))}
        stats['solved'] = {solver[i]:_solved[i] for i in range(len(solver))}
        stats['version'] = {solver[i]:_version[i] for i in range(len(solver))}
        stats['timelimit'] = int(pre[3].text.split('\n')[-2].split()[1].replace(',',''))
        stats['times'] = pd.DataFrame([l.split() for l in tab[8:nprobs+8]], columns=['instance']+solver)

    else:
        tab = pre[2].text.split('\n')
        tabmark = [ind for ind,i in enumerate(tab) if i.startswith('=====')]
        _version = pre[1].text.split('\n')[1:-1]
        _version = [x.split()[0].rstrip(':') for x in _version]
        _score = tab[1].split()[1:]
        _solved = tab[2].split()[1:]
        solver = tab[4].split()[1:]
        stats['solver'] = solver
        nprobs = len(tab[tabmark[0]+3:tabmark[1]])
        stats['nprobs'] = nprobs
        stats['score'] = {solver[i]:float(_score[i]) for i in range(len(solver))}
        stats['solved'] = {solver[i]:int(_solved[i].strip('*')) for i in range(len(solver))}
        if len(_version) == len(solver):
            stats['version'] = {solver[i]:_version[i] for i in range(len(solver))}
        else:
            stats['version'] = {solver[i]:solver[i] for i in range(len(solver))}
        stats['timelimit'] = timelimit
        stats['times'] = pd.DataFrame([l.split() for l in tab[tabmark[0]+3:tabmark[1]]], columns=['instance']+solver)
        
    return stats


def plot_benchmark(stats, base):
    """
    generate an interactive Plotly figure from the given dictionary
    """
    # clean up non-numeric values and replace with timelimit
    time = stats['times']
    for s in stats['solver']:
        time[s] = pd.to_numeric(stats['times'][s], errors='coerce')
    time.fillna(value=stats['timelimit'], inplace=True)
    fig = go.Figure()
    for s in sorted(time.keys().drop('instance')):
        if s == base:
            fig.add_trace(go.Scatter(x=time['instance'], y=time[base], mode='markers', name=stats['version'][s]))
        else:
            fig.add_trace(go.Bar(x=time['instance'], y=time[s]-time[base], name=stats['version'][s]))
    
    fig.update_layout(title=f'Absolute time differences using {stats["version"][base]} as base solver ({stats["date"]})',
        xaxis=dict(type='category')
        )
    return fig


def write_bench(url, timelimit):
    benchname = url.split('/')[-1][:-5]
    stats = parse_table(url, timelimit)

    time = stats['times']
    for s in stats['solver']:
        time[s] = pd.to_numeric(stats['times'][s], errors='coerce')
    time.fillna(value=stats['timelimit'], inplace=True)

    storedate = stats["date"].replace(' ','-')
    newdata = True
    # check whether there is already a file for this date
    if os.path.exists(f'docs/{benchname}-{storedate}.html'):
        newdata = False
        os.system(f'rm -f docs/{benchname}-{storedate}.html')

    # generate list of previous benchmarks
    def findbench(pattern, path):
        result = []
        for root, dirs, files in os.walk(path):
            for name in files:
                if fnmatch.fnmatch(name, pattern):
                    result.append(os.path.join(root, name))
        return result

    oldbench = findbench(f'{benchname}-[0-9]*.html', 'docs')

    plots = '\n'
    plots += f'## [{stats["title"]}]({url}) ({stats["date"]})\n'
    plots += '**Choose base solver for comparison:**\n\n'
    plots += '|      | score | solved |\n'
    plots += '| :--- | ---:  | ---:   |\n'
    for score, s in sorted(zip(stats['score'].values(), time.keys().drop('instance'))):
        plots += f'|[{stats["version"][s]}]({benchname}-{s}.html) | {stats["score"][s]} | {float(stats["solved"][s])/stats["nprobs"]*100:.0f}%|\n'
        if newdata:
            fig = plot_benchmark(stats, s)
            fig.write_html(f'docs/{benchname}-{s}.html', include_plotlyjs='cdn')
        os.system(f'cat docs/{benchname}-{s}.html >> docs/{benchname}-{storedate}.html')

    if oldbench:
        plots += '\n\n older versions:\n'

        for ob in oldbench:
            filename = os.path.basename(ob)
            date = filename.lstrip(benchname).rstrip('html').replace('-',' ')
            plots += f' - [{date}]({filename})\n'
    
    plots += '\n\n --- \n\n'

    return plots

top = """# Visualizations of Mittelmann benchmarks"""

bottom = '\n\nCheck out [my Github page](https://github.com/mattmilten/mittelmann-plots) for more information.\n'

urls = [('http://plato.asu.edu/ftp/lpsimp.html', 15000),
('http://plato.asu.edu/ftp/qplib.html', 3600),
('http://plato.asu.edu/ftp/nonbinary.html', 10800),
('http://plato.asu.edu/ftp/cnconv.html', 10800),
('http://plato.asu.edu/ftp/convex.html', 7200),
('http://plato.asu.edu/ftp/cconvex.html', 3600),
]

with open('docs/index.md', 'w') as index:
    index.write(top)

    for url in urls:
        index.write(write_bench(url[0], url[1]))

#     index.write(bottom)
