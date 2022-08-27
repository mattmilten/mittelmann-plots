Interactive charts comparing the results of [Hans Mittelmann's benchmarks](http://plato.asu.edu/bench.html).
Each solver can be selected to show pairwise running time factors for every other solver in the respective benchmark.
These plots should make browsing the results easier.
The score ([scaled shifted geometric mean](http://plato.asu.edu/ftp/shgeom.html)) is recomputed using the reported solving times.
We also calculate a "virtual best" or "ensemble" solver that picks the best performance over all solvers for every single problem
instance. This might reveal how much potential the individual solvers still have.
[Please let me know](https://github.com/mattmilten/mittelmann-plots/issues/new) if you have a question or if there is an error.

    
## [Benchmark of Simplex LP solvers (26 Aug 2022)](http://plato.asu.edu/ftp/lpsimp.html)
Choose base solver for comparison:

| solver | score (as reported) | solved of 60|
| :--- | ---:  | ---:   |
|[⭐ virtual best](lpsimp-vbest.html) | 0.74  | 100%|
|[🥇 COPT-5.0.4](lpsimp-COPT.html) | 1.00 (1.00) | 100%|
|[🥈 MindOpt-0.18.6](lpsimp-MDOPT.html) | 1.16 (1.16) | 100%|
|[🥉 Gurobi-9.5.0](lpsimp-Gurob.html) | 1.70 (1.70) | 98%|
|[📊 Optverse-0.2.6](lpsimp-OPTV.html) | 2.62 (2.62) | 88%|
|[📊 CLP-1.17.7](lpsimp-CLP.html) | 9.96 (9.96) | 72%|
|[📊 HiGHS-1.2.1](lpsimp-HiGHS.html) | 13.79 (13.80) | 78%|
|[📊 MOSEK-9.3.18](lpsimp-MOSEK.html) | 16.87 (16.90) | 72%|
|[📊 MATLAB-R2020b](lpsimp-MATL.html) | 25.13 (25.10) | 65%|
|[📊 Google-GLOP](lpsimp-GLOP.html) | 26.43 (26.40) | 53%|
|[📊 SOPLEX-6.0.0](lpsimp-SPLX.html) | 42.28 (42.30) | 57%|
|[📊 GLPK-5.0](lpsimp-GLPK.html) | 78.65 (78.70) | 47%|


<details><summary>previous benchmarks 🔽</summary>
<br>

<ul>
<li><a href="/mittelmann-plots/lpsimp-23-Aug-2022.html">23 Aug 2022</a></li>
<li><a href="/mittelmann-plots/lpsimp-20-Aug-2022.html">20 Aug 2022</a></li>
<li><a href="/mittelmann-plots/lpsimp-19-Aug-2022.html">19 Aug 2022</a></li>
<li><a href="/mittelmann-plots/lpsimp-18-Aug-2022.html">18 Aug 2022</a></li>
<li><a href="/mittelmann-plots/lpsimp-31-Jul-2022.html">31 Jul 2022</a></li>
<li><a href="/mittelmann-plots/lpsimp-29-Jul-2022.html">29 Jul 2022</a></li>
<li><a href="/mittelmann-plots/lpsimp-17-Jun-2022.html">17 Jun 2022</a></li>
<li><a href="/mittelmann-plots/lpsimp-15-Jun-2022.html">15 Jun 2022</a></li>
<li><a href="/mittelmann-plots/lpsimp-12-Jun-2022.html">12 Jun 2022</a></li>
<li><a href="/mittelmann-plots/lpsimp-6-Jun-2022.html">6 Jun 2022</a></li>
<li><a href="/mittelmann-plots/lpsimp-26-May-2022.html">26 May 2022</a></li>
<li><a href="/mittelmann-plots/lpsimp-8-May-2022.html">8 May 2022</a></li>
<li><a href="/mittelmann-plots/lpsimp-7-May-2022.html">7 May 2022</a></li>
<li><a href="/mittelmann-plots/lpsimp-17-Apr-2022.html">17 Apr 2022</a></li>
<li><a href="/mittelmann-plots/lpsimp-7-Apr-2022.html">7 Apr 2022</a></li>
<li><a href="/mittelmann-plots/lpsimp-2-Apr-2022.html">2 Apr 2022</a></li>
<li><a href="/mittelmann-plots/lpsimp-1-Apr-2022.html">1 Apr 2022</a></li>
<li><a href="/mittelmann-plots/lpsimp-4-Mar-2022.html">4 Mar 2022</a></li>
<li><a href="/mittelmann-plots/lpsimp-17-Feb-2022.html">17 Feb 2022</a></li>
<li><a href="/mittelmann-plots/lpsimp-1-Feb-2022.html">1 Feb 2022</a></li>
<li><a href="/mittelmann-plots/lpsimp-30-Jan-2022.html">30 Jan 2022</a></li>
<li><a href="/mittelmann-plots/lpsimp-28-Jan-2022.html">28 Jan 2022</a></li>
<li><a href="/mittelmann-plots/lpsimp-15-Dec-2021.html">15 Dec 2021</a></li>
<li><a href="/mittelmann-plots/lpsimp-11-Dec-2021.html">11 Dec 2021</a></li>
<li><a href="/mittelmann-plots/lpsimp-10-Nov-2021.html">10 Nov 2021</a></li>
<li><a href="/mittelmann-plots/lpsimp-3-Oct-2021.html">3 Oct 2021</a></li>
<li><a href="/mittelmann-plots/lpsimp-18-Sep-2021.html">18 Sep 2021</a></li>
<li><a href="/mittelmann-plots/lpsimp-17-Sep-2021.html">17 Sep 2021</a></li>
<li><a href="/mittelmann-plots/lpsimp-11-Sep-2021.html">11 Sep 2021</a></li>
<li><a href="/mittelmann-plots/lpsimp-26-Jul-2021.html">26 Jul 2021</a></li>
<li><a href="/mittelmann-plots/lpsimp-21-Jul-2021.html">21 Jul 2021</a></li>
<li><a href="/mittelmann-plots/lpsimp-9-Jun-2021.html">9 Jun 2021</a></li>
<li><a href="/mittelmann-plots/lpsimp-28-May-2021.html">28 May 2021</a></li>
<li><a href="/mittelmann-plots/lpsimp-3-Mar-2021.html">3 Mar 2021</a></li>
<li><a href="/mittelmann-plots/lpsimp-18-Jan-2021.html">18 Jan 2021</a></li>
<li><a href="/mittelmann-plots/lpsimp-5-Jan-2021.html">5 Jan 2021</a></li>
<li><a href="/mittelmann-plots/lpsimp-28-Dec-2020.html">28 Dec 2020</a></li>
<li><a href="/mittelmann-plots/lpsimp-4-Dec-2020.html">4 Dec 2020</a></li>
<li><a href="/mittelmann-plots/lpsimp-3-Dec-2020.html">3 Dec 2020</a></li>
<li><a href="/mittelmann-plots/lpsimp-2-Nov-2020.html">2 Nov 2020</a></li>
<li><a href="/mittelmann-plots/lpsimp-22-Oct-2020.html">22 Oct 2020</a></li>
<li><a href="/mittelmann-plots/lpsimp-26-Sep-2020.html">26 Sep 2020</a></li>
<li><a href="/mittelmann-plots/lpsimp-5-Sep-2020.html">5 Sep 2020</a></li>
<li><a href="/mittelmann-plots/lpsimp-27-Aug-2020.html">27 Aug 2020</a></li>
<li><a href="/mittelmann-plots/lpsimp-08-Aug-2020.html">08 Aug 2020</a></li>
</ul></details>

---


## [Benchmark of Barrier LP solvers (20 Aug 2022)](http://plato.asu.edu/ftp/lpbar.html)
Choose base solver for comparison:

| solver | score (as reported) | solved of 51|
| :--- | ---:  | ---:   |
|[⭐ virtual best](lpbar-vbest.html) | 0.65  | 100%|
|[🥇 COPT-5.0.0](lpbar-COPT.html) | 1.00 (1.00) | 100%|
|[🥈 Gurobi-9.5.1](lpbar-Gurobi.html) | 1.31 (1.31) | 98%|
|[🥉 MindOpt-0.18.2](lpbar-MDOPT.html) | 2.39 (2.39) | 96%|
|[📊 MOSEK-9.3.20](lpbar-MOSEK.html) | 4.92 (4.92) | 92%|
|[📊 PDLP$](lpbar-PDLP$.html) | 12.09 (12.10) | 86%|
|[📊 KNITRO-13.0.0](lpbar-KNITRO.html) | 14.47 (14.40) | 76%|
|[📊 HiGHS-1.2.2](lpbar-HiGHS.html) | 20.35 (18.60) | 82%|
|[📊 MATLAB-R2020b](lpbar-MATLAB.html) | 44.61 (36.80) | 71%|
|[📊 Tulip-0.9.4](lpbar-TULIP.html) | 52.37 (52.40) | 63%|
|[📊 CLP-1.17.7](lpbar-CLP.html) | 69.14 (69.10) | 69%|


<details><summary>previous benchmarks 🔽</summary>
<br>

<ul>
<li><a href="/mittelmann-plots/lpbar-29-Jul-2022.html">29 Jul 2022</a></li>
<li><a href="/mittelmann-plots/lpbar-15-Jun-2022.html">15 Jun 2022</a></li>
<li><a href="/mittelmann-plots/lpbar-1-Jun-2022.html">1 Jun 2022</a></li>
<li><a href="/mittelmann-plots/lpbar-25-May-2022.html">25 May 2022</a></li>
<li><a href="/mittelmann-plots/lpbar-14-May-2022.html">14 May 2022</a></li>
<li><a href="/mittelmann-plots/lpbar-15-Apr-2022.html">15 Apr 2022</a></li>
<li><a href="/mittelmann-plots/lpbar-12-Mar-2022.html">12 Mar 2022</a></li>
<li><a href="/mittelmann-plots/lpbar-4-Mar-2022.html">4 Mar 2022</a></li>
<li><a href="/mittelmann-plots/lpbar-17-Feb-2022.html">17 Feb 2022</a></li>
<li><a href="/mittelmann-plots/lpbar-28-Jan-2022.html">28 Jan 2022</a></li>
<li><a href="/mittelmann-plots/lpbar-19-Jan-2022.html">19 Jan 2022</a></li>
<li><a href="/mittelmann-plots/lpbar-9-Dec-2021.html">9 Dec 2021</a></li>
<li><a href="/mittelmann-plots/lpbar-10-Nov-2021.html">10 Nov 2021</a></li>
<li><a href="/mittelmann-plots/lpbar-3-Oct-2021.html">3 Oct 2021</a></li>
<li><a href="/mittelmann-plots/lpbar-1-Oct-2021.html">1 Oct 2021</a></li>
<li><a href="/mittelmann-plots/lpbar-18-Sep-2021.html">18 Sep 2021</a></li>
<li><a href="/mittelmann-plots/lpbar-11-Sep-2021.html">11 Sep 2021</a></li>
<li><a href="/mittelmann-plots/lpbar-24-Aug-2021.html">24 Aug 2021</a></li>
<li><a href="/mittelmann-plots/lpbar-26-Jul-2021.html">26 Jul 2021</a></li>
<li><a href="/mittelmann-plots/lpbar-21-Jul-2021.html">21 Jul 2021</a></li>
<li><a href="/mittelmann-plots/lpbar-9-Jun-2021.html">9 Jun 2021</a></li>
<li><a href="/mittelmann-plots/lpbar-28-May-2021.html">28 May 2021</a></li>
<li><a href="/mittelmann-plots/lpbar-3-Mar-2021.html">3 Mar 2021</a></li>
<li><a href="/mittelmann-plots/lpbar-28-Dec-2020.html">28 Dec 2020</a></li>
<li><a href="/mittelmann-plots/lpbar-13-Dec-2020.html">13 Dec 2020</a></li>
<li><a href="/mittelmann-plots/lpbar-10-Dec-2020.html">10 Dec 2020</a></li>
<li><a href="/mittelmann-plots/lpbar-4-Dec-2020.html">4 Dec 2020</a></li>
<li><a href="/mittelmann-plots/lpbar-3-Dec-2020.html">3 Dec 2020</a></li>
<li><a href="/mittelmann-plots/lpbar-2-Nov-2020.html">2 Nov 2020</a></li>
<li><a href="/mittelmann-plots/lpbar-22-Oct-2020.html">22 Oct 2020</a></li>
<li><a href="/mittelmann-plots/lpbar-8-Sep-2020.html">8 Sep 2020</a></li>
</ul></details>

---


## [Large Network-LP Benchmark (commercial vs free) (24 Aug 2022)](http://plato.asu.edu/ftp/network.html)
Choose base solver for comparison:

| solver | score (as reported) | solved of 25|
| :--- | ---:  | ---:   |
|[⭐ virtual best](network-vbest.html) | 0.92  | 100%|
|[🥇 MindOpt-0.18.6](network-MDOPT.html) | 1.00 (1.00) | 100%|
|[🥈 OptVerse-0.2.6](network-OPTV.html) | 1.19 (1.19) | 100%|
|[🥉 Gurobi-9.5.1](network-GUR.html) | 1.32 (1.32) | 100%|
|[📊 COPT-5.0.0](network-COPT.html) | 1.68 (1.68) | 100%|
|[📊 Clp-1.17.7](network-CLP.html) | 4.71 (4.71) | 100%|
|[📊 HiGHS-1.1.1](network-HGHS.html) | 10.15 (10.20) | 80%|
|[📊 MATLAB-R2020b](network-MATL.html) | 17.17 (17.20) | 80%|
|[📊 MOSEK-9.3.6](network-MOSEK.html) | 18.16 (18.20) | 84%|
|[📊 QSopt-1.01](network-QSOPT.html) | 27.55 (27.50) | 68%|
|[📊 SOPLEX-6.0.0](network-SPLX.html) | 52.38 (52.40) | 64%|


<details><summary>previous benchmarks 🔽</summary>
<br>

<ul>
<li><a href="/mittelmann-plots/network-17-Aug-2022.html">17 Aug 2022</a></li>
<li><a href="/mittelmann-plots/network-16-Jun-2022.html">16 Jun 2022</a></li>
<li><a href="/mittelmann-plots/network-13-Jun-2022.html">13 Jun 2022</a></li>
<li><a href="/mittelmann-plots/network-17-Apr-2022.html">17 Apr 2022</a></li>
<li><a href="/mittelmann-plots/network-26-Mar-2022.html">26 Mar 2022</a></li>
<li><a href="/mittelmann-plots/network-4-Mar-2022.html">4 Mar 2022</a></li>
<li><a href="/mittelmann-plots/network-3-Mar-2022.html">3 Mar 2022</a></li>
<li><a href="/mittelmann-plots/network-1-Mar-2022.html">1 Mar 2022</a></li>
<li><a href="/mittelmann-plots/network-1-Feb-2022.html">1 Feb 2022</a></li>
<li><a href="/mittelmann-plots/network-14-Dec-2021.html">14 Dec 2021</a></li>
<li><a href="/mittelmann-plots/network-10-Nov-2021.html">10 Nov 2021</a></li>
<li><a href="/mittelmann-plots/network-8-Nov-2021.html">8 Nov 2021</a></li>
<li><a href="/mittelmann-plots/network-22-Oct-2021.html">22 Oct 2021</a></li>
<li><a href="/mittelmann-plots/network-11-Oct-2021.html">11 Oct 2021</a></li>
<li><a href="/mittelmann-plots/network-8-Oct-2021.html">8 Oct 2021</a></li>
<li><a href="/mittelmann-plots/network-4-Oct-2021.html">4 Oct 2021</a></li>
<li><a href="/mittelmann-plots/network-26-Aug-2021.html">26 Aug 2021</a></li>
<li><a href="/mittelmann-plots/network-27-Jul-2021.html">27 Jul 2021</a></li>
<li><a href="/mittelmann-plots/network-21-Jul-2021.html">21 Jul 2021</a></li>
<li><a href="/mittelmann-plots/network-28-May-2021.html">28 May 2021</a></li>
<li><a href="/mittelmann-plots/network-3-Mar-2021.html">3 Mar 2021</a></li>
<li><a href="/mittelmann-plots/network-23-Feb-2021.html">23 Feb 2021</a></li>
<li><a href="/mittelmann-plots/network-29-Dec-2020.html">29 Dec 2020</a></li>
<li><a href="/mittelmann-plots/network-5-Dec-2020.html">5 Dec 2020</a></li>
<li><a href="/mittelmann-plots/network-2-Nov-2020.html">2 Nov 2020</a></li>
<li><a href="/mittelmann-plots/network-23-Oct-2020.html">23 Oct 2020</a></li>
<li><a href="/mittelmann-plots/network-26-Sep-2020.html">26 Sep 2020</a></li>
<li><a href="/mittelmann-plots/network-8-Sep-2020.html">8 Sep 2020</a></li>
</ul></details>

---


## [The MIPLIB2017 Benchmark Instances - 8 threads (30 Jun 2022)](http://plato.asu.edu/ftp/milp.html)
Choose base solver for comparison:

| solver | score (as reported) | solved of 240|
| :--- | ---:  | ---:   |
|[⭐ virtual best](milp_8threads-vbest.html) | 0.81  | 96%|
|[🥇 Gurobi-9.5.0](milp_8threads-Gurobi.html) | 1.00 (1.00) | 93%|
|[🥈 COPT-5.0.0](milp_8threads-COPT.html) | 2.34 (2.34) | 81%|
|[🥉 SCIPC/spx-8.0.0](milp_8threads-SCIPC.html) | 7.95 (7.95) | 63%|
|[📊 HiGHS-1.2.2](milp_8threads-HiGHS.html) | 9.15 (9.15) | 62%|
|[📊 SCIP/spx-8.0.0](milp_8threads-SCIP.html) | 9.72 (9.72) | 57%|
|[📊 CBC-2.10.5](milp_8threads-CBC.html) | 14.53 (14.50) | 45%|


<details><summary>previous benchmarks 🔽</summary>
<br>

<ul>
<li><a href="/mittelmann-plots/milp_8threads-8-May-2022.html">May 2022</a></li>
<li><a href="/mittelmann-plots/milp_8threads-23-Apr-2022.html">23 Apr 2022</a></li>
<li><a href="/mittelmann-plots/milp_8threads-5-Feb-2022.html">5 Feb 2022</a></li>
<li><a href="/mittelmann-plots/milp_8threads-30-Dec-2021.html">30 Dec 2021</a></li>
<li><a href="/mittelmann-plots/milp_8threads-25-Dec-2021.html">25 Dec 2021</a></li>
<li><a href="/mittelmann-plots/milp_8threads-19-Dec-2021.html">19 Dec 2021</a></li>
<li><a href="/mittelmann-plots/milp_8threads-13-Nov-2021.html">13 Nov 2021</a></li>
<li><a href="/mittelmann-plots/milp_8threads-5-Oct-2021.html">5 Oct 2021</a></li>
<li><a href="/mittelmann-plots/milp_8threads-3-Oct-2021.html">3 Oct 2021</a></li>
<li><a href="/mittelmann-plots/milp_8threads-10-Aug-2021.html">10 Aug 2021</a></li>
<li><a href="/mittelmann-plots/milp_8threads-4-Jun-2021.html">4 Jun 2021</a></li>
<li><a href="/mittelmann-plots/milp_8threads-5-Feb-2021.html">5 Feb 2021</a></li>
<li><a href="/mittelmann-plots/milp_8threads-15-Nov-2020.html">15 Nov 2020</a></li>
<li><a href="/mittelmann-plots/milp_8threads-2-Oct-2020.html">2 Oct 2020</a></li>
</ul></details>

---


## [MILP cases that are slightly pathological (25 Jul 2022)](http://plato.asu.edu/ftp/path.html)
Choose base solver for comparison:

| solver | score (as reported) | solved of 45|
| :--- | ---:  | ---:   |
|[⭐ virtual best](path-vbest.html) | 0.80  | 98%|
|[🥇 GUROBI-9.5.0](path-Gurobi.html) | 1.00 (1.00) | 98%|
|[🥈 COPT-5.0.0](path-COPT.html) | 3.99 (3.99) | 76%|
|[🥉 HiGHS-1.2.2](path-HiGHS.html) | 17.28 (17.30) | 56%|
|[📊 SCIPC-8.0.0](path-SCIPC.html) | 17.33 (17.30) | 51%|
|[📊 SCIP-8.0.0](path-SCIP.html) | 22.21 (22.20) | 42%|
|[📊 CBC-2.10.7](path-CBC.html) | 34.68 (34.70) | 11%|
|[📊 GLPK-5.0](path-GLPK.html) | 35.15 (35.20) | 13%|
|[📊 MATLAB-2020a](path-MATLAB.html) | 42.36 (42.40) | 7%|


<details><summary>previous benchmarks 🔽</summary>
<br>

<ul>
<li><a href="/mittelmann-plots/path-6-Jul-2022.html">6 Jul 2022</a></li>
<li><a href="/mittelmann-plots/path-19-Jun-2022.html">19 Jun 2022</a></li>
<li><a href="/mittelmann-plots/path-27-Apr-2022.html">27 Apr 2022</a></li>
<li><a href="/mittelmann-plots/path-1-Feb-2022.html">1 Feb 2022</a></li>
<li><a href="/mittelmann-plots/path-26-Jan-2022.html">26 Jan 2022</a></li>
<li><a href="/mittelmann-plots/path-15-Dec-2021.html">15 Dec 2021</a></li>
<li><a href="/mittelmann-plots/path-11-Nov-2021.html">11 Nov 2021</a></li>
</ul></details>

---


## [Infeasibility Detection for MILP Problems (24 Jul 2022)](http://plato.asu.edu/ftp/infeas.html)
Choose base solver for comparison:

| solver | score (as reported) | solved of 32|
| :--- | ---:  | ---:   |
|[⭐ virtual best](infeas-vbest.html) | 0.66  | 94%|
|[🥇 GUROBI-9.5.0](infeas-Gurobi.html) | 1.00 (1.00) | 91%|
|[🥈 COPT-5.0.0](infeas-COPT.html) | 1.39 (1.39) | 91%|
|[🥉 SCIPC-8.0.0](infeas-SCIPC.html) | 4.73 (4.68) | 81%|
|[📊 SCIP-8.0.0](infeas-SCIP.html) | 6.06 (6.06) | 78%|
|[📊 HiGHS-1.2.2](infeas-HiGHS.html) | 8.12 (8.12) | 75%|
|[📊 CBC-2.10.5](infeas-CBC.html) | 14.80 (14.80) | 62%|
|[📊 MATLAB-2020b](infeas-MATLAB.html) | 23.00 (23.00) | 47%|


<details><summary>previous benchmarks 🔽</summary>
<br>

<ul>
<li><a href="/mittelmann-plots/infeas-18-Jun-2022.html">18 Jun 2022</a></li>
<li><a href="/mittelmann-plots/infeas-25-Apr-2022.html">25 Apr 2022</a></li>
<li><a href="/mittelmann-plots/infeas-28-Jan-2022.html">28 Jan 2022</a></li>
<li><a href="/mittelmann-plots/infeas-14-Dec-2021.html">14 Dec 2021</a></li>
<li><a href="/mittelmann-plots/infeas-3-Dec-2021.html">3 Dec 2021</a></li>
<li><a href="/mittelmann-plots/infeas-10-Nov-2021.html">10 Nov 2021</a></li>
</ul></details>

---


## [Several SDP-codes on sparse and other SDP problems (27 Jul 2022)](http://plato.asu.edu/ftp/sparse_sdp.html)
Choose base solver for comparison:

| solver | score (as reported) | solved of 76|
| :--- | ---:  | ---:   |
|[⭐ virtual best](sparse_sdp-vbest.html) | 0.44  | 99%|
|[🥇 COPT-5.0](sparse_sdp-COPT.html) | 1.00 (1.00) | 97%|
|[🥈 SDPT3-4.0](sparse_sdp-SDPT3.html) | 2.13 (2.17) | 91%|
|[🥉 CSDP-6.2.0](sparse_sdp-CSDP.html) | 2.16 (2.19) | 92%|
|[📊 HDSDP-0.9.2](sparse_sdp-HDSDP.html) | 3.50 (3.57) | 92%|
|[📊 SDPA-7.4.2](sparse_sdp-SDPA.html) | 4.29 (4.40) | 80%|
|[📊 SeDuMi-1.3.5](sparse_sdp-SeDuMi.html) | 11.69 (12.20) | 82%|

---


## [Large Second Order Cone Benchmark (19 Jun 2022)](http://plato.asu.edu/ftp/socp.html)
Choose base solver for comparison:

| solver | score (as reported) | solved of 18|
| :--- | ---:  | ---:   |
|[⭐ virtual best](socp-vbest.html) | 0.74  | 100%|
|[🥇 MOSEK-9.3.20](socp-MOSEK.html) | 1.00 (1.00) | 100%|
|[🥈 Gurobi-9.5.0](socp-Gurobi.html) | 1.07 (1.07) | 100%|
|[🥉 COPT-5.0.0](socp-COPT.html) | 1.10 (1.10) | 100%|
|[📊 KNITRO-13.0.0](socp-KNITRO.html) | 9.47 (9.47) | 83%|
|[📊 ECOS-2.0.4](socp-ECOS.html) | 78.11 (78.10) | 33%|


<details><summary>previous benchmarks 🔽</summary>
<br>

<ul>
<li><a href="/mittelmann-plots/socp-6-May-2022.html">6 May 2022</a></li>
<li><a href="/mittelmann-plots/socp-28-Jan-2022.html">28 Jan 2022</a></li>
<li><a href="/mittelmann-plots/socp-18-Jan-2022.html">18 Jan 2022</a></li>
<li><a href="/mittelmann-plots/socp-10-Nov-2021.html">10 Nov 2021</a></li>
</ul></details>

---


## [Mixed-integer SOCP Benchmark (5 May 2022)](http://plato.asu.edu/ftp/misocp.html)
Choose base solver for comparison:

| solver | score (as reported) | solved of 47|
| :--- | ---:  | ---:   |
|[⭐ virtual best](misocp-vbest.html) | 1.00  | 100%|
|[🥇 Gurobi-9.5.1](misocp-GUROBI.html) | 1.00 (1.00) | 100%|
|[🥈 MOSEK-9.3.20](misocp-MOSEK.html) | 13.25 (13.20) | 68%|
|[🥉 SCIP-8.0.0](misocp-SCIP.html) | 20.43 (20.40) | 66%|


<details><summary>previous benchmarks 🔽</summary>
<br>

<ul>
<li><a href="/mittelmann-plots/misocp-4-Mar-2022.html">4 Mar 2022</a></li>
<li><a href="/mittelmann-plots/misocp-26-Dec-2021.html">26 Dec 2021</a></li>
<li><a href="/mittelmann-plots/misocp-10-Nov-2021.html">10 Nov 2021</a></li>
<li><a href="/mittelmann-plots/misocp-3-Sep-2021.html">3 Sep 2021</a></li>
<li><a href="/mittelmann-plots/misocp-21-Aug-2021.html">21 Aug 2021</a></li>
<li><a href="/mittelmann-plots/misocp-12-Aug-2021.html">12 Aug 2021</a></li>
<li><a href="/mittelmann-plots/misocp-16-Feb-2021.html">16 Feb 2021</a></li>
<li><a href="/mittelmann-plots/misocp-28-Jan-2021.html">28 Jan 2021</a></li>
<li><a href="/mittelmann-plots/misocp-10-Nov-2020.html">10 Nov 2020</a></li>
<li><a href="/mittelmann-plots/misocp-14-Jun-2020.html">14 Jun 2020</a></li>
</ul></details>

---


## [Binary Non-Convex QPLIB Benchmark (18 Aug 2022)](http://plato.asu.edu/ftp/qplib.html)
Choose base solver for comparison:

| solver | score (as reported) | solved of 92|
| :--- | ---:  | ---:   |
|[⭐ virtual best](qplib-vbest.html) | 0.72  | 98%|
|[🥇 Gurobi-9.5.2](qplib-GUROBI.html) | 1.00 (1.00) | 97%|
|[🥈 OCTERACT-4.4.0](qplib-OCTERACT.html) | 1.94 (1.94) | 87%|
|[🥉 Baron-22.7.23](qplib-BARON.html) | 16.98 (17.00) | 47%|
|[📊 SCIP-8.0.0](qplib-SCIP.html) | 41.07 (41.10) | 38%|
|[📊 ANTIGONE-1.1](qplib-ANTIGONE.html) | 85.88 (85.90) | 17%|
|[📊 COUENNE-0.5](qplib-COUENNE.html) | 102.98 (103.00) | 7%|


<details><summary>previous benchmarks 🔽</summary>
<br>

<ul>
<li><a href="/mittelmann-plots/qplib-23-Jul-2022.html">23 Jul 2022</a></li>
<li><a href="/mittelmann-plots/qplib-15-Jul-2022.html">15 Jul 2022</a></li>
<li><a href="/mittelmann-plots/qplib-9-Jul-2022.html">9 Jul 2022</a></li>
<li><a href="/mittelmann-plots/qplib-6-May-2022.html">6 May 2022</a></li>
<li><a href="/mittelmann-plots/qplib-1-May-2022.html">1 May 2022</a></li>
<li><a href="/mittelmann-plots/qplib-25-Feb-2022.html">25 Feb 2022</a></li>
<li><a href="/mittelmann-plots/qplib-27-Jan-2022.html">27 Jan 2022</a></li>
<li><a href="/mittelmann-plots/qplib-7-Jan-2022.html">7 Jan 2022</a></li>
<li><a href="/mittelmann-plots/qplib-18-Dec-2021.html">18 Dec 2021</a></li>
<li><a href="/mittelmann-plots/qplib-3-Dec-2021.html">3 Dec 2021</a></li>
<li><a href="/mittelmann-plots/qplib-29-Nov-2021.html">29 Nov 2021</a></li>
<li><a href="/mittelmann-plots/qplib-24-Nov-2021.html">24 Nov 2021</a></li>
<li><a href="/mittelmann-plots/qplib-13-Nov-2021.html">13 Nov 2021</a></li>
<li><a href="/mittelmann-plots/qplib-23-Aug-2021.html">23 Aug 2021</a></li>
<li><a href="/mittelmann-plots/qplib-27-May-2021.html">27 May 2021</a></li>
<li><a href="/mittelmann-plots/qplib-6-May-2021.html">6 May 2021</a></li>
<li><a href="/mittelmann-plots/qplib-25-Jan-2021.html">25 Jan 2021</a></li>
<li><a href="/mittelmann-plots/qplib-10-Nov-2020.html">10 Nov 2020</a></li>
<li><a href="/mittelmann-plots/qplib-7-Oct-2020.html">7 Oct 2020</a></li>
<li><a href="/mittelmann-plots/qplib-12-Aug-2020.html">12 Aug 2020</a></li>
</ul></details>

---


## [Discrete Non-Convex QPLIB Benchmark (non-binary) (16 Jul 2022)](http://plato.asu.edu/ftp/nonbinary.html)
Choose base solver for comparison:

| solver | score (as reported) | solved of 88|
| :--- | ---:  | ---:   |
|[⭐ virtual best](nonbinary-vbest.html) | 0.17  | 99%|
|[🥇 Gurobi-9.5.0](nonbinary-GUROBI.html) | 1.00 (1.00) | 83%|
|[🥈 OCTERACT-4.4.0](nonbinary-OCTERACT.html) | 1.63 (3.91) | 85%|
|[🥉 SCIP-8.0.0](nonbinary-SCIP.html) | 8.97 (21.60) | 42%|
|[📊 ANTIGONE-1.1](nonbinary-ANTIGONE.html) | 16.24 (39.00) | 33%|
|[📊 Baron-22.3.21](nonbinary-BARON.html) | 16.85 (40.50) | 31%|
|[📊 MINOTAUR-0.3.0](nonbinary-MINOTAUR.html) | 20.10 (48.30) | 17%|
|[📊 COUENNE-0.5](nonbinary-COUENNE.html) | 32.78 (78.80) | 9%|


<details><summary>previous benchmarks 🔽</summary>
<br>

<ul>
<li><a href="/mittelmann-plots/nonbinary-15-Jul-2022.html">15 Jul 2022</a></li>
<li><a href="/mittelmann-plots/nonbinary-7-Jul-2022.html">7 Jul 2022</a></li>
<li><a href="/mittelmann-plots/nonbinary-30-Apr-2022.html">30 Apr 2022</a></li>
<li><a href="/mittelmann-plots/nonbinary-26-Apr-2022.html">26 Apr 2022</a></li>
<li><a href="/mittelmann-plots/nonbinary-9-Mar-2022.html">9 Mar 2022</a></li>
<li><a href="/mittelmann-plots/nonbinary-28-Jan-2022.html">28 Jan 2022</a></li>
<li><a href="/mittelmann-plots/nonbinary-15-Jan-2022.html">15 Jan 2022</a></li>
<li><a href="/mittelmann-plots/nonbinary-18-Dec-2021.html">18 Dec 2021</a></li>
<li><a href="/mittelmann-plots/nonbinary-3-Dec-2021.html">3 Dec 2021</a></li>
<li><a href="/mittelmann-plots/nonbinary-1-Dec-2021.html">1 Dec 2021</a></li>
<li><a href="/mittelmann-plots/nonbinary-17-Nov-2021.html">17 Nov 2021</a></li>
<li><a href="/mittelmann-plots/nonbinary-7-Sep-2021.html">7 Sep 2021</a></li>
<li><a href="/mittelmann-plots/nonbinary-27-Jan-2021.html">27 Jan 2021</a></li>
<li><a href="/mittelmann-plots/nonbinary-10-Nov-2020.html">10 Nov 2020</a></li>
<li><a href="/mittelmann-plots/nonbinary-8-Oct-2020.html">8 Oct 2020</a></li>
<li><a href="/mittelmann-plots/nonbinary-20-Aug-2020.html">20 Aug 2020</a></li>
</ul></details>

---


## [Continuous Non-Convex QPLIB Benchmark (21 Jul 2022)](http://plato.asu.edu/ftp/cnconv.html)
Choose base solver for comparison:

| solver | score (as reported) | solved of 68|
| :--- | ---:  | ---:   |
|[⭐ virtual best](cnconv-vbest.html) | 0.20  | 94%|
|[🥇 GUROBI-9.5.0](cnconv-GUROBI.html) | 1.00 (1.00) | 62%|
|[🥈 OCTERACT-4.4.0](cnconv-OCTERACT.html) | 1.50 (1.87) | 62%|
|[🥉 ANTIGONE-1.1](cnconv-ANTIGONE.html) | 3.93 (4.90) | 41%|
|[📊 Baron-22.1.8](cnconv-BARON.html) | 5.32 (6.64) | 25%|
|[📊 MINOTAUR-0.3.0](cnconv-MINOTAUR.html) | 5.57 (6.95) | 22%|
|[📊 SCIP-8.0.0](cnconv-SCIP.html) | 7.89 (9.85) | 19%|
|[📊 COUENNE-0.5](cnconv-COUENNE.html) | 8.98 (11.20) | 12%|


<details><summary>previous benchmarks 🔽</summary>
<br>

<ul>
<li><a href="/mittelmann-plots/cnconv-5-Jul-2022.html">5 Jul 2022</a></li>
<li><a href="/mittelmann-plots/cnconv-3-May-2022.html">3 May 2022</a></li>
<li><a href="/mittelmann-plots/cnconv-7-Mar-2022.html">7 Mar 2022</a></li>
<li><a href="/mittelmann-plots/cnconv-2-Feb-2022.html">2 Feb 2022</a></li>
<li><a href="/mittelmann-plots/cnconv-15-Jan-2022.html">15 Jan 2022</a></li>
<li><a href="/mittelmann-plots/cnconv-20-Dec-2021.html">20 Dec 2021</a></li>
<li><a href="/mittelmann-plots/cnconv-3-Dec-2021.html">3 Dec 2021</a></li>
<li><a href="/mittelmann-plots/cnconv-30-Nov-2021.html">30 Nov 2021</a></li>
<li><a href="/mittelmann-plots/cnconv-17-Nov-2021.html">17 Nov 2021</a></li>
<li><a href="/mittelmann-plots/cnconv-16-Sep-2021.html">16 Sep 2021</a></li>
<li><a href="/mittelmann-plots/cnconv-7-Sep-2021.html">7 Sep 2021</a></li>
<li><a href="/mittelmann-plots/cnconv-2-Dec-2020.html">2 Dec 2020</a></li>
<li><a href="/mittelmann-plots/cnconv-11-Nov-2020.html">11 Nov 2020</a></li>
<li><a href="/mittelmann-plots/cnconv-10-Oct-2020.html">10 Oct 2020</a></li>
<li><a href="/mittelmann-plots/cnconv-20-Aug-2020.html">20 Aug 2020</a></li>
</ul></details>

---


## [Convex Continuous QPLIB Benchmark (26 Jul 2022)](http://plato.asu.edu/ftp/cconvex.html)
Choose base solver for comparison:

| solver | score (as reported) | solved of 32|
| :--- | ---:  | ---:   |
|[⭐ virtual best](cconvex-vbest.html) | 0.89  | 100%|
|[🥇 COPT-5.0.0](cconvex-COPT.html) | 1.00 (1.00) | 100%|
|[🥈 KNITRO-13.0.0](cconvex-KNITRO.html) | 1.55 (1.55) | 100%|
|[🥉 MOSEK-9.3.12](cconvex-MOSEK.html) | 2.00 (2.00) | 97%|
|[📊 Gurobi-9.5.0](cconvex-Gurobi.html) | 2.03 (2.03) | 94%|
|[📊 IPOPT-3.14.5](cconvex-IPOPT.html) | 7.40 (7.40) | 91%|


<details><summary>previous benchmarks 🔽</summary>
<br>

<ul>
<li><a href="/mittelmann-plots/cconvex-19-Jun-2022.html">19 Jun 2022</a></li>
<li><a href="/mittelmann-plots/cconvex-11-Apr-2022.html">11 Apr 2022</a></li>
<li><a href="/mittelmann-plots/cconvex-28-Jan-2022.html">28 Jan 2022</a></li>
<li><a href="/mittelmann-plots/cconvex-22-Jan-2022.html">22 Jan 2022</a></li>
<li><a href="/mittelmann-plots/cconvex-18-Jan-2022.html">18 Jan 2022</a></li>
<li><a href="/mittelmann-plots/cconvex-19-Dec-2021.html">19 Dec 2021</a></li>
<li><a href="/mittelmann-plots/cconvex-11-Nov-2021.html">11 Nov 2021</a></li>
<li><a href="/mittelmann-plots/cconvex-5-May-2021.html">5 May 2021</a></li>
<li><a href="/mittelmann-plots/cconvex-13-Dec-2020.html">13 Dec 2020</a></li>
<li><a href="/mittelmann-plots/cconvex-11-Nov-2020.html">11 Nov 2020</a></li>
<li><a href="/mittelmann-plots/cconvex-27-Sep-2020.html">27 Sep 2020</a></li>
<li><a href="/mittelmann-plots/cconvex-3-Apr-2020.html">3 Apr 2020</a></li>
</ul></details>

---


## [Convex Discrete QPLIB Benchmark (12 Aug 2022)](http://plato.asu.edu/ftp/convex.html)
Choose base solver for comparison:

| solver | score (as reported) | solved of 31|
| :--- | ---:  | ---:   |
|[⭐ virtual best](convex-vbest.html) | 0.64  | 87%|
|[🥇 GUROBI-9.5.0](convex-GUROBI.html) | 1.00 (1.00) | 74%|
|[🥈 OCTERACT-4.4.0](convex-OCTERACT.html) | 3.99 (3.99) | 74%|
|[🥉 Shot-1.1](convex-SHOT.html) | 5.15 (5.15) | 48%|
|[📊 Baron-22.1.8](convex-BARON.html) | 7.22 (7.22) | 55%|
|[📊 KNITRO-13.1.0](convex-KNITRO.html) | 8.43 (8.43) | 42%|
|[📊 MOSEK-9.3.11](convex-MOSEK.html) | 11.72 (11.70) | 42%|
|[📊 SCIP-8.0.0](convex-SCIP.html) | 13.06 (13.10) | 42%|
|[📊 Bonmin-1.8.7](convex-BONMIN.html) | 17.78 (17.80) | 32%|
|[📊 MINOTAUR-0.3.0](convex-MINOTAUR.html) | 23.42 (23.40) | 42%|
|[📊 ANTIGONE-1.1](convex-ANTIGONE.html) | 46.86 (46.90) | 6%|


<details><summary>previous benchmarks 🔽</summary>
<br>

<ul>
<li><a href="/mittelmann-plots/convex-16-Jul-2022.html">16 Jul 2022</a></li>
<li><a href="/mittelmann-plots/convex-7-Jul-2022.html">7 Jul 2022</a></li>
<li><a href="/mittelmann-plots/convex-12-Jun-2022.html">12 Jun 2022</a></li>
<li><a href="/mittelmann-plots/convex-25-Apr-2022.html">25 Apr 2022</a></li>
<li><a href="/mittelmann-plots/convex-23-Feb-2022.html">23 Feb 2022</a></li>
<li><a href="/mittelmann-plots/convex-25-Jan-2022.html">25 Jan 2022</a></li>
<li><a href="/mittelmann-plots/convex-11-Jan-2022.html">11 Jan 2022</a></li>
<li><a href="/mittelmann-plots/convex-8-Jan-2022.html">8 Jan 2022</a></li>
<li><a href="/mittelmann-plots/convex-16-Dec-2021.html">16 Dec 2021</a></li>
<li><a href="/mittelmann-plots/convex-22-Nov-2021.html">22 Nov 2021</a></li>
<li><a href="/mittelmann-plots/convex-11-Nov-2021.html">11 Nov 2021</a></li>
<li><a href="/mittelmann-plots/convex-21-Aug-2021.html">21 Aug 2021</a></li>
<li><a href="/mittelmann-plots/convex-23-Jan-2021.html">23 Jan 2021</a></li>
<li><a href="/mittelmann-plots/convex-22-Jan-2021.html">22 Jan 2021</a></li>
<li><a href="/mittelmann-plots/convex-13-Dec-2020.html">13 Dec 2020</a></li>
<li><a href="/mittelmann-plots/convex-15-Nov-2020.html">15 Nov 2020</a></li>
<li><a href="/mittelmann-plots/convex-10-Nov-2020.html">10 Nov 2020</a></li>
<li><a href="/mittelmann-plots/convex-8-Oct-2020.html">8 Oct 2020</a></li>
<li><a href="/mittelmann-plots/convex-15-Aug-2020.html">15 Aug 2020</a></li>
</ul></details>

---


## [Mixed Integer Nonlinear Programming Benchmark (MINLPLIB) (10 Aug 2022)](http://plato.asu.edu/ftp/minlp.html)
Choose base solver for comparison:

| solver | score (as reported) | solved of 87|
| :--- | ---:  | ---:   |
|[⭐ virtual best](minlp-vbest.html) | 0.21  | 95%|
|[🥇 OCTERACT](minlp-OCTERACT.html) | 1.00 (0.74) | 77%|
|[🥈 SCIP](minlp-SCIP.html) | 1.07 (0.79) | 74%|
|[🥉 BARON](minlp-BARON.html) | 1.35 (1.00) | 71%|
|[📊 ANTIGONE](minlp-ANTIGONE.html) | 4.03 (2.99) | 61%|
|[📊 LINDO](minlp-LINDO.html) | 5.30 (3.93) | 43%|


<details><summary>previous benchmarks 🔽</summary>
<br>

<ul>
<li><a href="/mittelmann-plots/minlp-23-Jul-2022.html">23 Jul 2022</a></li>
</ul></details>

---


## [MPEC Benchmark (Math. Progr. w. Equilibrium Constraints) (12 Apr 2022)](http://plato.asu.edu/ftp/mpec.html)
Choose base solver for comparison:

| solver | score (as reported) | solved of 29|
| :--- | ---:  | ---:   |
|[⭐ virtual best](mpec-vbest.html) | 1.00  | 83%|
|[🥇 KNITRO-13.0](mpec-KNITRO.html) | 1.00 (1.00) | 83%|
|[🥈 filter-MPEC](mpec-filter.html) | 7.82 (8.90) | 62%|
|[🥉 LOQO-7.03](mpec-LOQO.html) | 16.69 (19.50) | 21%|

---

