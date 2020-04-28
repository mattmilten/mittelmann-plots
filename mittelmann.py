from bs4 import BeautifulSoup
import requests
import pandas as pd
import re
import plotly.express as px
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


def plot_benchmark(stats):
    """
    generate an interactive Plotly figure from the given dictionary
    """
    # clean up non-numeric values and replace with timelimit
    time = stats['times']
    for s in stats['solver']:
        time[s] = pd.to_numeric(stats['times'][s], errors='coerce')
    time.fillna(value=stats['timelimit'], inplace=True)
    fig = go.Figure()

    for s in stats['solver']:
        fig.add_trace(go.Scatter(x=time['instance'], y=time[s],
                        mode='markers',
                        name=stats['version'][s]))
    fig.update_layout(title=f'{stats["title"]} ({stats["date"]})')
    fig.show()
    return fig


if __name__ == '__main__':
    stats = parse_table('http://plato.asu.edu/ftp/lpsimp.html')
    fig = plot_benchmark(stats)
    fig.write_html('lpsimp.html', include_plotlyjs=False)
