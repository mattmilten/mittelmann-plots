from bs4 import BeautifulSoup
import requests
import pandas as pd
import re
import os, fnmatch
import plotly.graph_objects as go

def parse_table(url):
    """
    parse a specific table to generate a dictionary with the runtimes and
    auxiliary information
    """
    resp = requests.get(url) 
    soup = BeautifulSoup(resp.text, features="html.parser")
    pre = soup.find_all('pre')
    
    stats = {}

    stats['date'] = pre[0].text.split('\n')[1].replace('=','').rstrip()
    stats['title'] = pre[0].text.split('\n')[2].strip()
    _version = pre[2].text.split('\n')[1:-1]
    _version = [x.split()[0].rstrip(':') for x in _version]
    _score = pre[3].text.split('\n')[3].split()
    _solved = pre[3].text.split('\n')[4].split()[1:]
    solver = pre[3].text.split('\n')[6].split()[2:]
    stats['solver'] = solver
    nprobs = int(pre[3].text.split('\n')[6].split()[0])
    stats['nprobs'] = nprobs
    stats['score'] = {solver[i]:_score[i] for i in range(len(solver))}
    stats['solved'] = {solver[i]:_solved[i] for i in range(len(solver))}
    stats['version'] = {solver[i]:_version[i] for i in range(len(solver))}
    stats['timelimit'] = int(pre[3].text.split('\n')[-2].split()[1].replace(',',''))
    _table = pre[3].text.split('\n')[8:nprobs+8]
    stats['times'] = pd.DataFrame([l.split() for l in _table], columns=['instance']+solver)
    
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
    
    fig.update_layout(title=f'Absolute time differences between {stats["version"][base]} and other Simplex LP solvers ({stats["date"]})')
    return fig

stats = parse_table('http://plato.asu.edu/ftp/lpsimp.html')

time = stats['times']
for s in stats['solver']:
    time[s] = pd.to_numeric(stats['times'][s], errors='coerce')
time.fillna(value=stats['timelimit'], inplace=True)

storedate = stats["date"].replace(' ','-')
# delete current stored file if present
os.system(f'rm -f docs/lpcomp-{storedate}.html')

# generate list of previous benchmarks
def find(pattern, path):
    result = []
    for root, dirs, files in os.walk(path):
        for name in files:
            if fnmatch.fnmatch(name, pattern):
                result.append(os.path.join(root, name))
    return result

oldbench = find('lpcomp-*.html', 'docs')

plots = ""
plots += f'<h2 id="simplex-lp">Simplex LP ({stats["date"]})</h2>\n'
plots += '<h3>Choose base solver for comparison:<h3>\n<ul>\n'

for s in sorted(time.keys().drop('instance')):
    fig = plot_benchmark(stats, s)
    fig.write_html(f'docs/{s}.html', include_plotlyjs='cdn')
    plots += f'\t<li><a href={s}.html>{stats["version"][s]}</a></li>\n'
    os.system(f'cat docs/{s}.html >> docs/lpcomp-{storedate}.html')
plots += '</ul>\n'

oldlinks = """
      <p>older versions:
        <ul>
"""

for ob in oldbench:
    name = os.path.basename(ob)
    oldlinks += f"<li><a href={name}>{name.lstrip('lpcomp').rstrip('html').replace('-',' ')}</a></li>\n"

oldlinks +="""
        </ul>
      </p>
"""

top = """<!DOCTYPE html>
<html lang="en-US">
  <head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">

<!-- Begin Jekyll SEO tag v2.6.1 -->
<title>Visualizations of Mittelmann benchmarks | mittelmann-plots</title>
<meta name="generator" content="Jekyll v3.8.5" />
<meta property="og:title" content="Visualizations of Mittelmann benchmarks" />
<meta property="og:locale" content="en_US" />
<meta name="description" content="Visualizations of Mittelmann benchmarks" />
<meta property="og:description" content="Visualizations of Mittelmann benchmarks" />
<link rel="canonical" href="https://mattmilten.github.io/mittelmann-plots/" />
<meta property="og:url" content="https://mattmilten.github.io/mittelmann-plots/" />
<meta property="og:site_name" content="mittelmann-plots" />
<script type="application/ld+json">
{"@type":"WebSite","headline":"Visualizations of Mittelmann benchmarks","url":"https://github.com/mattmilten/mittelmann-plots","name":"mittelmann-plots","description":"Visualizations of Mittelmann benchmarks","@context":"https://schema.org"}</script>
<!-- End Jekyll SEO tag -->

    <link rel="stylesheet" href="/mittelmann-plots/assets/css/style.css?v=73b8bebba12f73a6e4f8873242ca033c15630844">
    <script src="https://cdn.plot.ly/plotly-latest.min.js"></script>
  </head>
  <body>
    <div class="container-lg px-3 my-5 markdown-body">
      <h1 id="visualizations-of-mittelmann-benchmarks">Visualizations of Mittelmann benchmarks</h1>

"""

bottom = """
      <div class="footer border-top border-gray-light mt-5 pt-3 text-right text-gray">
        This site is open source. Check out <a href="https://github.com/mattmilten/mittelmann-plots">my Github page</a> for more information.
      </div>
      
    </div>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/anchor-js/4.1.0/anchor.min.js" integrity="sha256-lZaRhKri35AyJSypXXs4o6OPFTbTmUoltBbDCbdzegg=" crossorigin="anonymous"></script>
    <script>anchors.add();</script>
    
  </body>
</html>
"""

with open('docs/index.html', 'w') as index:
    index.write(top)
    index.write(plots)
    index.write(oldlinks)
    index.write(bottom)
