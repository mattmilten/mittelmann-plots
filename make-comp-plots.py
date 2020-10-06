from bs4 import BeautifulSoup
import requests
import pandas as pd
import numpy as np
import os, fnmatch
import plotly.graph_objects as go
from datetime import datetime as dt

def get_version(s, version):
    if s in ['SPLX', 'SOPLX']:
        s = 'SoPlex'
    elif s in ['MDOPT']:
        s = 'MindOpt'
    elif s in ['GLOP']:
        s = 'Google-GLOP'
    elif s in ['MSK']:
        s = 'Mosek'
    
    match = [v for v in version if v.lower().find(s.lower()) >= 0]
    return match[0] if match else s


def parse_table(url, timelimit=3600, threads=1):
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

    if url.find('lpsimp.html') >= 0:
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
        stats['solved'] = {solver[i]:int(_solved[i]) for i in range(len(solver))}
        stats['version'] = {s:get_version(s, _version) for s in solver}
        stats['timelimit'] = int(pre[3].text.split('\n')[-2].split()[1].replace(',',''))
        stats['times'] = pd.DataFrame([l.split() for l in tab[8:nprobs+8]], columns=['instance']+solver)

    elif url.find('lpbar.html') >= 0:
        tab = pre[3].text.split('\n')
        tabmark = [ind for ind,i in enumerate(tab) if i.startswith('=====')]
        _version = pre[2].text.split('\n')[1:-1]
        _version = [x.split()[0].rstrip(':') for x in _version]
        _score = tab[3].split()[2:]
        _solved = tab[4].split()[1:]
        solver = tab[6].split()[1:]
        stats['solver'] = solver
        nprobs = int(tab[3].split()[0])
        stats['nprobs'] = nprobs
        stats['score'] = {solver[i]:float(_score[i]) for i in range(len(solver))}
        stats['solved'] = {solver[i]:int(_solved[i]) for i in range(len(solver))}
        stats['version'] = {s:get_version(s, _version) for s in solver}
        stats['timelimit'] = timelimit
        stats['times'] = pd.DataFrame([l.split() for l in tab[tabmark[0]+3:tabmark[-1]]], columns=['instance']+solver)

    elif url.find('network.html') >= 0:
        tab = pre[2].text.split('\n')
        tabmark = [ind for ind,i in enumerate(tab) if i.startswith('=====')]
        _version = pre[1].text.split('\n')[1:-1]
        _version = [x.split()[1] for x in _version]
        _score = tab[3].split()
        solver = tab[5].split()[3:]
        stats['solver'] = solver
        stats['nprobs'] = len(tab[tabmark[0]+3:tabmark[-1]])
        stats['score'] = {solver[i]:float(_score[i]) for i in range(len(solver))}
        stats['solved'] = {}
        stats['version'] = {s:get_version(s, _version) for s in solver}
        stats['timelimit'] = timelimit
        stats['times'] = pd.DataFrame([l.split() for l in tab[tabmark[0]+3:tabmark[-1]]], columns=['instance','nodes','arcs']+solver)
        stats['times'] = stats['times'].drop(['nodes','arcs'], axis=1)
        for s in solver:
            stats['solved'][s] = stats['nprobs'] - pd.to_numeric(stats['times'][s], errors='coerce').isna().sum()

    elif url.find('milp.html') >= 0:
        if threads == 1:
            taburl = 'http://plato.asu.edu/ftp/milp_tables/1thread.res'
            scoretab = pre[1].text.split('\n')[5:10]
        else:
            taburl = 'http://plato.asu.edu/ftp/milp_tables/8threads.res'
            scoretab = pre[1].text.split('\n')[13:18]
            stats['title'] += f' - {threads} threads'
        
        resp = requests.get(taburl) 
        souptab = BeautifulSoup(resp.text, features="html.parser")
        tab = souptab.contents[0].split('\n')
        tabmark = [ind for ind,i in enumerate(tab) if i.startswith('----')]
        columns = tab[tabmark[0]+1].replace('|',' ').split()[1:]
        
        for i,c in enumerate(columns):
            if c.startswith('lpsolve'):
                columns[i] = 'LP_SOL'
            elif c.startswith('FiberSCIP'):
                columns[i] = 'FSCIP'
            elif c.startswith('SCIP'):
                columns[i] = 'SCIP'

        _version = str(soup.contents[2]).split('<p>')[4].split('\n')[1:-1]
        _version = [x.split()[0].rstrip(':') for x in _version]
        _solved = scoretab[4].split()[1:]
        _score = scoretab[3].split()[1:]
        solver = scoretab[0].split()[2:]
        stats['solver'] = solver
        stats['solved'] = {solver[i]:int(_solved[i]) for i in range(len(solver))}
        stats['version'] = {s:get_version(s, _version) for s in solver}
        stats['score'] = {solver[i]:float(_score[i].strip('`')) for i in range(len(solver))}
        stats['times'] = pd.DataFrame([l.split() for l in tab[tabmark[1]+1:tabmark[-2]]], columns=['instance']+columns)
        stats['nprobs'] = len(stats['times'])
        stats['timelimit'] = timelimit

    elif url.find('misocp.html') >= 0:
        tab = pre[1].text.split('\n')
        tabmark = [ind for ind,i in enumerate(tab) if i.startswith('=====')]
        _score = tab[2].split()
        _solved = tab[5].split()[3:]
        solver = tab[4].split()[1:]
        stats['solver'] = solver
        stats['nprobs'] = len(tab[tabmark[0]+4:tabmark[-1]])
        stats['score'] = {solver[i]:float(_score[i]) for i in range(len(solver))}
        stats['solved'] = {solver[i]:int(_solved[i].strip('*')) for i in range(len(solver))}
        stats['version'] = {solver[i]:solver[i] for i in range(len(solver))}
        stats['timelimit'] = timelimit
        stats['times'] = pd.DataFrame([l.split() for l in tab[tabmark[0]+4:tabmark[-1]]], columns=['instance']+solver)

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
        stats['version'] = {s:get_version(s, _version) for s in solver}
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

    # this is to define the tick labels on the y axis (built-in log-scale doesn't work well with bar charts)
    power = 2
    maxtime = time.max(numeric_only=True).max()
    tickvals = np.arange(-int(np.log2(maxtime)),int(np.log2(maxtime)))
    ticktext = [str(power**i)  if i >= 0 else f'1/{power**-i}' for i in tickvals]

    fig = go.Figure()
    for s in sorted(time.keys().drop(['instance', base])):
        hovertext = [f'time: {time[s][i]}</br>factor:{(time[s][i]+10)/(time[base][i]+10):.3f}</br>base time: {time[base][i]}' for i in range(len(time[base]))]
        fig.add_trace(go.Bar(x=time['instance'], y=np.log2((time[s]+10)/(time[base]+10)), hoverinfo='text+x+name', hovertext=hovertext, name=stats['version'][s]))
    
    fig.update_layout(title=f'Shifted time ratios (shift=10 seconds) using {stats["version"][base]} as base solver ({stats["date"]})',
                      legend_title_text='click to hide/show',
                      xaxis_type='category',
                      yaxis_title='time ratios (log scale)',
                      yaxis_tickvals=tickvals,
                      yaxis_ticktext=ticktext
                     )

    return fig


def write_bench(url, timelimit, threads=1):
    benchname = url.split('/')[-1][:-5]
    stats = parse_table(url, timelimit, threads)

    if threads > 1:
        benchname += f'_{threads}threads'

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
        for root, _, files in os.walk(path):
            for name in files:
                if fnmatch.fnmatch(name, pattern):
                    result.append(os.path.join(root, name))
        return sorted(result, key=lambda x: dt.strptime(os.path.basename(x), f'{benchname}-%d-%b-%Y.html'), reverse=True)

    oldbench = findbench(f'{benchname}-[0-9]*.html', 'docs')

    plots = '\n'
    plots += f'## [{stats["title"]} ({stats["date"]})]({url})\n'
    plots += '**Choose base solver for comparison:**\n\n'
    plots += '|      | score | solved |\n'
    plots += '| :--- | ---:  | ---:   |\n'
    for s in sorted(stats['score'].items(), key=lambda x: x[1]):
        s = s[0]
        plots += f'|[{stats["version"][s]}]({benchname}-{s}.html) | {stats["score"][s]:.2f} | {float(stats["solved"][s])/stats["nprobs"]*100:.0f}%|\n'
        if newdata:
            fig = plot_benchmark(stats, s)
            fig.write_html(f'docs/{benchname}-{s}.html', include_plotlyjs='cdn')
        os.system(f'cat docs/{benchname}-{s}.html >> docs/{benchname}-{storedate}.html')

    if oldbench:
        plots += '\n\n older versions:\n'

        for ob in oldbench:
            filename = os.path.basename(ob)
            date = filename.lstrip(f'{benchname}-').rstrip('.html').replace('-',' ')
            plots += f' - [{date}]({filename})\n'
    
    plots += '\n\n --- \n\n'

    return plots

urls = [('http://plato.asu.edu/ftp/lpsimp.html', 15000, 1),
('http://plato.asu.edu/ftp/lpbar.html', 15000, 1),
('http://plato.asu.edu/ftp/network.html', 3600, 1),
('http://plato.asu.edu/ftp/milp.html', 7200, 1),
('http://plato.asu.edu/ftp/milp.html', 7200, 8),
('http://plato.asu.edu/ftp/misocp.html', 7200, 1),
('http://plato.asu.edu/ftp/qplib.html', 3600, 1),
('http://plato.asu.edu/ftp/nonbinary.html', 10800, 1),
('http://plato.asu.edu/ftp/cnconv.html', 10800, 1),
('http://plato.asu.edu/ftp/convex.html', 7200, 1),
('http://plato.asu.edu/ftp/cconvex.html', 3600, 1),
]

with open('docs/index.md', 'w') as index:
    for url in urls:
        index.write(write_bench(url[0], url[1], url[2]))
