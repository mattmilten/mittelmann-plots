# %%

from time import sleep
from bs4 import BeautifulSoup
import requests
import math
import pandas as pd
import numpy as np
import sys, os, fnmatch
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from datetime import datetime as dt

# %%
def get_version(s, version):
    for v in version:
        # split up '(F)SCIP' entry
        if v.startswith("(F)SCIP"):
            version.append(v.replace("(F)", ""))
            version.append(v.replace("(F)", "F"))
            version.remove(v)
        # split up SCIP entry to support SCIP-cpx
        if v.startswith("SCIP-") or v.startswith("SCIP/"):
            version.append(v.replace("SCIP", "SCIPC"))

    if s in ["SPLX", "SOPLX"]:
        s = "SoPlex"
    elif s in ["MDOPT"]:
        s = "MindOpt"
    elif s in ["GLOP"]:
        s = "Google-GLOP"
    elif s in ["MSK"]:
        s = "Mosek"
    elif s in ["HGHS"]:
        s = "HiGHS"
    elif s in ["GUROBI"]:
        s = "Gurobi"
    elif s in ["SCIPC"]:
        s = "SCIPC"
    elif s in ["PDLP%"]:
        s = "ORTOOLS"

    match = [v for v in version if v.lower().startswith(s.lower())]
    return match[0] if match else s


# %%
def parse_table(url, session, timelimit=3600, threads=1):
    """
    parse a specific table to generate a dictionary with the runtimes and
    auxiliary information
    """
    resp = session.get(url)
    soup = BeautifulSoup(resp.text, features="html.parser")
    pre = soup.find_all("pre")

    stats = {}

    stats["date"] = pre[0].text.split("\n")[1].replace("=", "").replace("-", "").replace("`"," ").strip()
    stats["title"] = pre[0].text.split("\n")[2].strip()

    if "lpopt.html" in url:
        tab = pre[0].text.split("\n")
        tabmark = [ind for ind, i in enumerate(tab) if i.startswith("=====")]
        _version = pre[0].text.split("\n\n")[6].split("\n")
        _version = [x.split()[0].rstrip(":") for x in _version]
        _score = tab[tabmark[0] - 2].split()[2:]
        _solved = tab[tabmark[0] - 1].split()[1:]
        solver = tab[tabmark[0] + 1].split()[1:]
        solver.remove("MDOPT")
        stats["solver"] = solver
        stats["nprobs"] = len(tab[tabmark[1] + 1 : tabmark[2]])
        stats["score"] = {
            solver[i]: float(_score[i]) for i in range(len(solver))
        }
        stats["solved"] = {solver[i]: int(_solved[i]) for i in range(len(solver))}
        stats["version"] = {s: get_version(s, _version) for s in solver}
        stats["timelimit"] = timelimit
        stats["times"] = pd.DataFrame(
            [l.split() for l in tab[tabmark[1] + 1 : tabmark[2]]],
            columns=["instance"] + solver,
        )

    elif "lpfeas.html" in url:
        tab = pre[0].text.split("\n")
        tabmark = [ind for ind, i in enumerate(tab) if i.startswith("=====")]
        _version = pre[0].text.split("\n\n")[6].split("\n")
        _version = [x.split()[0].rstrip(":") for x in _version]
        _score = tab[tabmark[0] - 2].split()[2:]
        _solved = ["0"]
        _solved.extend(tab[tabmark[0] - 1].split()[1:]) # hack to add the missing solved number for Gurobi
        solver = tab[tabmark[0] + 1].split()[1:]
        solver.remove("MDOPT")
        stats["solver"] = solver
        stats["nprobs"] = len(tab[tabmark[1] + 1 : tabmark[2]])
        stats["score"] = {
            solver[i]: float(_score[i].strip("$")) for i in range(len(solver))
        }
        stats["solved"] = {solver[i]: int(_solved[i]) for i in range(len(solver))}
        stats["version"] = {s: get_version(s, _version) for s in solver}
        stats["timelimit"] = timelimit
        stats["times"] = pd.DataFrame(
            [l.split() for l in tab[tabmark[1] + 1 : tabmark[2]]],
            columns=["instance"] + solver,
        )
        stats["solved"]["Gurobi"] = len(stats["times"][stats["times"]["Gurobi"].astype(float) < timelimit])

    elif "network.html" in url:
        tab = pre[2].text.split("\n")
        tabmark = [ind for ind, i in enumerate(tab) if i.startswith("=====")]
        _version = pre[1].text.split("\n")[1:-1]
        _version = [x.split()[1] for x in _version]
        _score = tab[3].split()
        solver = tab[5].split()[3:]
        stats["solver"] = solver
        stats["nprobs"] = len(tab[tabmark[0] + 3 : tabmark[-1]])
        stats["score"] = {solver[i]: float(_score[i]) for i in range(len(solver))}
        stats["solved"] = {}
        stats["version"] = {s: get_version(s, _version) for s in solver}
        stats["timelimit"] = timelimit
        stats["times"] = pd.DataFrame(
            [l.split() for l in tab[tabmark[0] + 3 : tabmark[-1]]],
            columns=["instance", "nodes", "arcs"] + solver,
        )
        stats["times"] = stats["times"].drop(["nodes", "arcs"], axis=1)
        for s in solver:
            stats["solved"][s] = (
                stats["nprobs"]
                - pd.to_numeric(stats["times"][s], errors="coerce").isna().sum()
            )

    elif "milp.html" in url:
        if threads == 1:
            taburl = "http://plato.asu.edu/ftp/milp_tables/1thread.res"
            scoretab = pre[1].text.split("\n")[5:10]
            stats["title"] += f" - 1 thread - discontinued"
        else:
            taburl = "http://plato.asu.edu/ftp/milp_tables/8threads.res"
            scoretab = pre[1].text.split("\n")[5:10]
            stats["title"] += f" - {threads} threads"

        resp = session.get(taburl)
        souptab = BeautifulSoup(resp.text, features="html.parser")
        tab = souptab.contents[0].split("\n")
        tabmark = [ind for ind, i in enumerate(tab) if i.startswith("----")]
        columns = tab[tabmark[0] + 1].replace("|", " ").split()[1:]

        for i, c in enumerate(columns):
            if c.startswith("lpsolve"):
                columns[i] = "LP_SOL"
            elif c.startswith("FiberSCIP"):
                columns[i] = "FSCIP"
            elif c.startswith("SCIP-spx"):
                columns[i] = "SCIP"
            elif c.startswith("SCIP-cpx"):
                columns[i] = "SCIPC"

        _version = str(soup.contents[2]).split("<p>")[4].split("\n")[1:-1]
        _version = [x.split()[0].rstrip(":") for x in _version]
        _solved = scoretab[4].split()[1:]
        _score = scoretab[3].split()[1:]
        solver = scoretab[0].split()[:]
        stats["solver"] = solver
        stats["solved"] = {solver[i]: int(_solved[i]) for i in range(len(solver))}
        stats["version"] = {s: get_version(s, _version) for s in solver}
        stats["score"] = {
            solver[i]: float(_score[i].strip("`")) for i in range(len(solver))
        }
        stats["times"] = pd.DataFrame(
            [l.split() for l in tab[tabmark[1] + 1 : tabmark[-2]]],
            columns=["instance"] + columns,
        )
        stats["nprobs"] = len(stats["times"])
        stats["timelimit"] = timelimit

    elif "path.html" in url:
        taburl = "http://plato.asu.edu/ftp/path.res"
        scoretab = pre[1].text.split("\n")[3:7]
        resp = session.get(taburl)
        souptab = BeautifulSoup(resp.text, features="html.parser")
        tab = souptab.contents[0].split("\n")
        tabmark = [ind for ind, i in enumerate(tab) if i.startswith("----")]
        columns = tab[tabmark[0] + 1].replace("|", " ").split()[1:]

        for i, c in enumerate(columns):
            if c.startswith("lpsolve"):
                columns[i] = "LP_SOL"
            elif c.startswith("FiberSCIP"):
                columns[i] = "FSCIP"
            elif c.startswith("SCIP-spx"):
                columns[i] = "SCIP"
            elif c.startswith("SCIPC-cpx"):
                columns[i] = "SCIPC"

        _version = str(soup.contents[2]).split("<br/>")[1:-1]
        _version = [x.split()[0].rstrip(":") for x in _version]
        _solved = scoretab[3].split()[:]
        _score = scoretab[2].split()[:]
        solver = [get_version(s, "") for s in scoretab[0].split()[:]]
        stats["solver"] = solver
        stats["solved"] = {solver[i]: int(_solved[i]) for i in range(len(solver))}
        stats["version"] = {s: get_version(s, _version) for s in solver}
        stats["score"] = {solver[i]: float(_score[i]) for i in range(len(solver))}
        stats["times"] = pd.DataFrame(
            [l.split() for l in tab[tabmark[1] + 1 : tabmark[-2]]],
            columns=["instance"] + columns,
        )
        stats["nprobs"] = len(stats["times"])
        stats["timelimit"] = timelimit

    elif "infeas.html" in url:
        taburl = "http://plato.asu.edu/ftp/infeasible.res"
        scoretab = pre[1].text.split("\n")[1:7]
        resp = session.get(taburl)
        souptab = BeautifulSoup(resp.text, features="html.parser")
        tab = souptab.contents[0].split("\n")
        tabmark = [ind for ind, i in enumerate(tab) if i.startswith("----")]
        columns = tab[tabmark[0] + 1].replace("|", " ").split()[1:]

        for i, c in enumerate(columns):
            if c.startswith("lpsolve"):
                columns[i] = "LP_SOL"
            elif c.startswith("FiberSCIP"):
                columns[i] = "FSCIP"
            elif c.startswith("SCIP-spx"):
                columns[i] = "SCIP"
            elif c.startswith("SCIP-cpx"):
                columns[i] = "SCIPC"

        _version = str(soup.contents[2]).split("<p>")[3].split("\n")[1:-1]
        _version = [x.split()[0].rstrip(":") for x in _version]
        _solved = scoretab[4].split()[3:]
        _score = scoretab[2].split()[:]
        solver = [get_version(s, "") for s in scoretab[0].split()]
        stats["solver"] = solver
        stats["solved"] = {solver[i]: int(_solved[i]) for i in range(len(solver))}
        stats["version"] = {s: get_version(s, _version) for s in solver}
        stats["score"] = {solver[i]: float(_score[i]) for i in range(len(solver))}
        stats["times"] = pd.DataFrame(
            [l.split() for l in tab[tabmark[1] + 1 : tabmark[-2]]],
            columns=["instance"] + columns,
        )
        stats["nprobs"] = len(stats["times"])
        stats["timelimit"] = timelimit

    elif "misocp.html" in url:
        tab = pre[1].text.split("\n")
        tabmark = [ind for ind, i in enumerate(tab) if i.startswith("=====")]
        _score = tab[2].split()
        _solved = tab[5].split()[3:]
        solver = [s.rstrip("&") for s in tab[4].split()[1:]]
        _version = [x.text for x in soup.find_all("td")][0::2]
        stats["solver"] = solver
        stats["nprobs"] = len(tab[tabmark[0] + 4 : tabmark[-1]])
        stats["score"] = {solver[i]: float(_score[i]) for i in range(len(solver))}
        stats["solved"] = {
            solver[i]: int(_solved[i].strip("*")) for i in range(len(solver))
        }
        stats["version"] = {
            solver[i]: get_version(solver[i], _version) for i in range(len(solver))
        }
        stats["timelimit"] = timelimit
        stats["times"] = pd.DataFrame(
            [l.split() for l in tab[tabmark[0] + 4 : tabmark[-1]]],
            columns=["instance"] + solver,
        )

    elif "socp.html" in url:
        tab = pre[1].text.split("\n")
        tabmark = [
            ind
            for ind, i in enumerate(tab)
            if i.startswith("-----") or i.startswith("======")
        ]
        # Solvers version on this page are in a table
        _version = [x.text for x in soup.find_all("td")][0::2]
        _score = tab[3].split()[1:]
        _solved = tab[4].split()[1:]
        solver = [s.rstrip("&") for s in tab[6].split()[1:]]
        stats["solver"] = solver
        nprobs = len(tab[tabmark[1] + 1 : tabmark[2]])
        stats["nprobs"] = nprobs
        stats["score"] = {solver[i]: float(_score[i]) for i in range(len(solver))}
        stats["solved"] = {
            solver[i]: int(_solved[i].strip("*")) for i in range(len(solver))
        }
        stats["version"] = {s: get_version(s, _version) for s in solver}
        stats["timelimit"] = timelimit
        stats["times"] = pd.DataFrame(
            [l.split() for l in tab[tabmark[1] + 1 : tabmark[2]]],
            columns=["instance"] + solver,
        )

    elif "sparse_sdp.html" in url:
        tab = pre[3].text.split("\n")
        tabmark = [ind for ind, i in enumerate(tab) if i.startswith("=====")]
        _version = pre[1].text.split("\n")[1:-1]
        _version = [x.split()[0].rstrip(":") for x in _version]
        _score = tab[2].split()[:]
        _solved = tab[5].split()[3:]
        solver = [s.rstrip("&") for s in tab[7].split()[1:]]
        stats["solver"] = solver
        nprobs = len(tab[tabmark[1] : tabmark[2]])
        stats["nprobs"] = nprobs
        stats["score"] = {solver[i]: float(_score[i]) for i in range(len(solver))}
        stats["solved"] = {
            solver[i]: int(_solved[i].strip("*")) for i in range(len(solver))
        }
        stats["version"] = {s: get_version(s, _version) for s in solver}
        stats["timelimit"] = timelimit
        stats["times"] = pd.DataFrame(
            [l.split() for l in tab[tabmark[1] : tabmark[2]]],
            columns=["instance"] + solver,
        )
        # count small violations (marked with an "a" suffix) as solved
        stats["times"].replace({r"(\s*[0-9]+)a": r"\1"}, regex=True, inplace=True)

    elif "mpec.html" in url:
        p = soup.find_all("p")
        stats["date"] = (
            p[0].text.split("\n")[0].replace("=", "").replace("-", "").strip()
        )
        tab = pre[1].text.split("\n")
        tabmark = [ind for ind, i in enumerate(tab) if i.startswith("=====")]
        _version = p[4].text.split("\n")[0:3]
        _version = [x.split()[0].rstrip(":") for x in _version]
        _score = tab[1].split()[2:]
        _solved = tab[2].split()[4:]
        solver = [s.rstrip("&") for s in tab[4].split()[1:]]
        stats["solver"] = solver
        nprobs = len(tab[tabmark[0] + 2 : tabmark[1]])
        stats["nprobs"] = nprobs
        stats["score"] = {solver[i]: float(_score[i]) for i in range(len(solver))}
        stats["solved"] = {
            solver[i]: int(_solved[i].strip("*")) for i in range(len(solver))
        }
        stats["version"] = {s: get_version(s, _version) for s in solver}
        stats["timelimit"] = timelimit
        stats["times"] = pd.DataFrame(
            [l.split() for l in tab[tabmark[0] + 2 : tabmark[1]]],
            columns=["instance"] + solver,
        )

    elif "minlp.html" in url:
        taburl = "http://plato.asu.edu/ftp/compare.txt"
        resp = session.get(taburl)
        souptab = BeautifulSoup(resp.text, features="html.parser")
        tab = souptab.contents[0].split("\n")
        scoretab = pre[1].text.split("\n")
        solver = [s.rstrip("&") for s in scoretab[1].split()]
        stats["solver"] = solver
        _score = scoretab[3].split()[2:]
        _solved = scoretab[4].split()[1:]
        stats["score"] = {solver[i]: float(_score[i]) for i in range(len(solver))}
        stats["solved"] = {solver[i]: int(_solved[i]) for i in range(len(solver))}
        stats["version"] = {s: s for s in solver}
        stats["timelimit"] = timelimit
        tabmark = [ind for ind, i in enumerate(tab) if i.startswith("-----")]
        # need to get solver names again because of different order in table
        solver = [s[0:s.find("(")] for s in tab[0].replace("|", " ").split()]
        columns = ["instance"] + [f"{solver[0]}_nodes_drop", f"{solver[0]}"]
        for i in range(1, len(solver)):
            columns.append(f"{solver[i]}_nodes_drop")
            columns.append(f"{solver[i]}")
            columns.append(f"{solver[i]}_nodesQ_drop")
            columns.append(f"{solver[i]}_timeQ_drop")
        columns.append("check_drop")
        times = pd.DataFrame(
            [
                l.replace("*", " ").replace(">", " ").replace("#", " ").split()
                for l in tab[tabmark[1] + 1 : tabmark[2]]
            ],
            columns=columns,
        )
        drop = [c for c in times.columns if c.find("drop") >= 0]
        times.drop(drop, axis=1, inplace=True)
        stats["times"] = times
        stats["nprobs"] = len(times)

    elif "nonbinary.html" in url:
        tab = pre[2].text.split("\n")
        tabmark = [ind for ind, i in enumerate(tab) if i.startswith("=====")]
        _version = pre[1].text.split("\n")[1:-1]
        _version = [x.split()[0].rstrip(":") for x in _version]
        _score = tab[1].split()[1:]
        _solved = tab[2].split()[1:]
        solver = [s.rstrip("&") for s in tab[4].split()[1:]]
        stats["solver"] = solver
        nprobs = len(tab[tabmark[0] + 3 : tabmark[1]])
        stats["nprobs"] = nprobs
        stats["score"] = {solver[i]: float(_score[i]) for i in range(len(solver))}
        stats["solved"] = {
            solver[i]: int(_solved[i].strip("*")) for i in range(len(solver))
        }
        stats["version"] = {s: get_version(s, _version) for s in solver}
        stats["timelimit"] = timelimit
        stats["times"] = pd.DataFrame(
            [l.split() for l in tab[tabmark[0] + 3 : tabmark[1]]],
            columns=["instance"] + solver,
        )

    else:
        tab = pre[2].text.split("\n")
        tabmark = [ind for ind, i in enumerate(tab) if i.startswith("=====")]
        _version = pre[1].text.split("\n")[1:-1]
        _version = [x.split()[0].rstrip(":") for x in _version]
        _score = tab[1].split()[1:]
        _solved = tab[2].split()[1:]
        solver = [s.rstrip("&") for s in tab[4].split()[1:]]
        stats["solver"] = solver
        nprobs = len(tab[tabmark[0] + 3 : tabmark[1]])
        stats["nprobs"] = nprobs
        stats["score"] = {solver[i]: float(_score[i].replace("r","").replace("R","")) for i in range(len(solver))}
        stats["solved"] = {
            solver[i]: int(_solved[i].strip("*")) for i in range(len(solver))
        }
        stats["version"] = {s: get_version(s, _version) for s in solver}
        stats["timelimit"] = timelimit
        stats["times"] = pd.DataFrame(
            [l.split() for l in tab[tabmark[0] + 3 : tabmark[1]]],
            columns=["instance"] + solver,
        )

    # clean up non-numeric values and replace with timelimit
    time = stats["times"]
    for s in stats["solver"]:
        time[s] = pd.to_numeric(stats["times"][s], errors="coerce")
    time.fillna(value=stats["timelimit"], inplace=True)
    stats["times"] = time

    return stats


# %%
def timeout_symbol(basetime, time, limit):
    if basetime >= limit:
        if time >= limit:
            return "❌"
        return "🔻"
    if time >= limit:
        return "🔺"
    else:
        return ""


# %%
def plot_benchmark(stats, base):
    """
    generate an interactive Plotly figure from the given dictionary
    """

    # this is to define the tick labels on the y-axis (built-in log-scale doesn't work well with bar charts)
    power = 2
    time = stats["times"]
    maxtime = time.max(numeric_only=True).max()
    tickvals = np.arange(-int(np.log2(maxtime)), int(np.log2(maxtime)))
    ticktext = [str(power ** i) if i >= 0 else f"1/{power**-i}" for i in tickvals]

    fig = make_subplots(specs=[[{"secondary_y": True}]])
    time = time.sort_values(base).reset_index(drop=True)

    for s in sorted(time.keys().drop(["instance"])):
        if not s in stats["version"]:
            continue
        if s == base:
            fig.add_trace(
                go.Scatter(
                    x=time["instance"],
                    y=time[base],
                    name=stats["version"][base],
                    mode="markers",
                    hovertext=time[base],
                    hoverinfo="text+x+name",
                ),
                secondary_y=True,
            )
            continue

        hovertext = [
            f'{stats["version"][s]}: {time[s][i]}s<br>{stats["version"][base]}: {time[base][i]}s<br>factor:{(time[s][i]+10)/(time[base][i]+10):.3f}'
            for i in range(len(time[base]))
        ]
        text = [
            timeout_symbol(time[base][i], time[s][i], stats["timelimit"])
            for i in range(len(time[base]))
        ]
        fig.add_trace(
            go.Bar(
                x=time["instance"],
                y=np.log2((time[s] + 10) / (time[base] + 10)),
                name=stats["version"][s],
                text=text,
                textposition="outside",
                textfont_size=20,
                hoverinfo="text+x",
                hovertext=hovertext,
            ),
            secondary_y=False,
        )

    title = f'<b>{stats["title"]}</b>'
    title += f'<br>shifted time ratios (shift=10 seconds) using {stats["version"][base]} as base solver ({stats["date"]}) - <a href="https://mattmilten.github.io/mittelmann-plots/">mattmilten.github.io/mittelmann-plots</a>'

    subtext = (
        "(🔻)🔺: (base) solver failed to solve within the time limit<br> ❌: no solution"
    )
    fig.add_annotation(
        x=0,
        y=1,
        xref="paper",
        yref="paper",
        showarrow=False,
        align="left",
        text=subtext,
    )

    fig.update_layout(
        title=title,
        legend_title_text="click to hide/show",
        xaxis_type="category",
        xaxis_title=f'instances sorted by solving time of {stats["version"][base]}',
        yaxis_title="time ratios (log scale)",
        yaxis_tickvals=tickvals,
        yaxis_ticktext=ticktext,
    )
    fig.update_yaxes(
        automargin=True,
        title_text=f'time of {stats["version"][base]}',
        secondary_y=True,
        type="log",
    )
    return fig


# %%
def write_bench(url, session, timelimit, threads=1):

    medals = {0: "⭐", 1: "🥇", 2: "🥈", 3: "🥉"}

    benchname = url.split("/")[-1][:-5]
    stats = parse_table(url, session, timelimit, threads)

    if threads > 1:
        benchname += f"_{threads}threads"

    # compute scores based on shifted geometric means of solve times
    stats["shmean"] = {}
    shift = 10
    for s in stats["solver"]:
        time = stats["times"][s]
        logsum = sum(time.apply(lambda x: math.log(max(1, x + shift))))
        stats["shmean"].update({s: math.exp(logsum / len(time)) - shift})
    bestshmean = min(stats["shmean"].values())
    for s in stats["solver"]:
        stats["shmean"][s] = stats["shmean"][s] / bestshmean

    # add data for the virtual best solver
    stats["solver"].append("vbest")
    stats["version"]["vbest"] = "virtual best"
    times = stats["times"].drop("instance", axis="columns")
    stats["times"]["vbest"] = times.apply(min, axis="columns")
    stats["solved"]["vbest"] = len(stats["times"][stats["times"]["vbest"] < timelimit])
    stats["score"]["vbest"] = 0
    logsum = sum(stats["times"]["vbest"].apply(lambda x: math.log(max(1, x + shift))))
    stats["shmean"]["vbest"] = (math.exp(logsum / len(time)) - shift) / bestshmean
    stats["shmean"]["vbest"] -= 1e-4 # enforce that vbest is always first in the list

    storedate = stats["date"].replace(" ", "-")
    newdata = True
    # check whether there is already a file for this date
    if os.path.exists(f"docs/{benchname}-{storedate}.html"):
        newdata = False
        os.system(f"rm -f docs/{benchname}-{storedate}.html")

    if "update" in sys.argv:
        newdata = True

    # generate list of previous benchmarks
    def findbench(pattern, path):
        result = []
        for root, _, files in os.walk(path):
            for name in files:
                if fnmatch.fnmatch(name, pattern):
                    result.append(os.path.join(root, name))
        return sorted(
            result,
            key=lambda x: dt.strptime(
                os.path.basename(x), f"{benchname}-%d-%b-%Y.html"
            ),
            reverse=True,
        )

    oldbench = findbench(f"{benchname}-[0-9]*.html", "docs")

    plots = "\n"
    plots += f'## [{stats["title"]} ({stats["date"]})]({url})\n'
    plots += "Choose base solver for comparison:\n\n"
    plots += f'| solver | score (as reported) | solved of {stats["nprobs"]}|\n'
    plots += "| :--- | ---:  | ---:   |\n"
    for i, s in enumerate(sorted(stats["shmean"].items(), key=lambda x: x[1])):
        s = s[0]
        score = f"({stats['score'][s]:.2f})" if not s == "vbest" else ""
        plots += f'|[{medals.get(i, "📊")} {stats["version"][s]}]({benchname}-{s}.html) | {stats["shmean"][s]:.2f} {score} | {float(stats["solved"][s])/stats["nprobs"]*100:.0f}%|\n'
        if newdata:
            fig = plot_benchmark(stats, s)
            fig.write_html(f"docs/{benchname}-{s}.html", include_plotlyjs="cdn")
        os.system(f"cat docs/{benchname}-{s}.html >> docs/{benchname}-{storedate}.html")

    if oldbench:
        plots += "\n\n<details><summary>previous benchmarks 🔽</summary>\n<br>\n\n"
        plots += "<ul>\n"
        for ob in oldbench:
            filename = os.path.basename(ob)
            date = filename.lstrip(f"{benchname}-").rstrip(".html").replace("-", " ")
            plots += f'<li><a href="/mittelmann-plots/{filename}">{date}</a></li>\n'
        plots += "</ul></details>\n"

    plots += "\n---\n\n"

    return plots


# %%
parsedata = [
    # LP
    ("http://plato.asu.edu/ftp/lpfeas.html", 15000, 1),
    ("http://plato.asu.edu/ftp/lpopt.html", 15000, 1),
    ("http://plato.asu.edu/ftp/network.html", 3600, 1),
    # MIP
    # ("http://plato.asu.edu/ftp/milp.html", 7200, 1), # deprecated
    ("http://plato.asu.edu/ftp/milp.html", 7200, 8),
    ("http://plato.asu.edu/ftp/path.html", 10800, 1),
    ("http://plato.asu.edu/ftp/infeas.html", 3600, 1),
    # SDP/SQLP
    ("http://plato.asu.edu/ftp/sparse_sdp.html", 40000, 1),
    ("http://plato.asu.edu/ftp/socp.html", 3600, 1),
    ("http://plato.asu.edu/ftp/misocp.html", 7200, 1),
    # MIQP/QCP
    ("http://plato.asu.edu/ftp/qplib.html", 3600, 1),
    ("http://plato.asu.edu/ftp/nonbinary.html", 10800, 1),
    ("http://plato.asu.edu/ftp/cnconv.html", 10800, 1),
    ("http://plato.asu.edu/ftp/cconvex.html", 7200, 1),
    ("http://plato.asu.edu/ftp/convex.html", 7200, 1),
    # MINLP
    ("http://plato.asu.edu/ftp/minlp.html", 7200, 1),
    # MPEC
    ("http://plato.asu.edu/ftp/mpec.html", 500, 1),
]

# %%
if __name__ == "__main__":
    session = requests.Session()
    with open("docs/index.md", "w", encoding="utf-8") as index:
        index.write(
            """Interactive charts comparing the results of [Hans Mittelmann's benchmarks](http://plato.asu.edu/bench.html).
Each solver can be selected to show pairwise running time factors for every other solver in the respective benchmark.
These plots should make browsing the results easier.
The score ([scaled shifted geometric mean](http://plato.asu.edu/ftp/shgeom.html)) is recomputed using the reported solving times.
We also calculate a "virtual best" or "ensemble" solver that picks the best performance over all solvers for every single problem
instance. This might reveal how much potential the individual solvers still have.
[Please let me know](https://github.com/mattmilten/mittelmann-plots/issues/new) if you have a question or if there is an error.\n
    """
        )
        for (url, timelimit, threads) in parsedata:
            print(f"processing {url}")
            index.write(write_bench(url, session, timelimit, threads))

# %%
