Interactive charts comparing the results of [Hans Mittelmann's benchmarks](http://plato.asu.edu/bench.html).
Each solver can be selected to show pairwise running time factors for every other solver in the respective benchmark.
These plots should make browsing the results easier.
The score ([scaled shifted geometric mean](http://plato.asu.edu/ftp/shgeom.html)) is recomputed using the reported solving times.
We also calculate a "virtual best" or "ensemble" solver that picks the best performance over all solvers for every single problem
instance. This might reveal how much potential the individual solvers still have.
[Please let me know](https://github.com/mattmilten/mittelmann-plots/issues/new) if you have a question or if there is an error.

    
## [LPfeas Benchmark (find PD feasible point) (9 Dec 2022)](http://plato.asu.edu/ftp/lpfeas.html)
Choose base solver for comparison:

| solver | score (as reported) | solved of 71|
| :--- | ---:  | ---:   |
|[⭐ virtual best](lpfeas-vbest.html) | 0.64  | 100%|
|[🥇 Gurobi-10.0.0](lpfeas-Gurobi.html) | 1.00 (0.00) | 100%|
|[🥈 COPT-6.0.3](lpfeas-COPT.html) | 1.04 (1.00) | 100%|
|[🥉 MOSEK-10.0.25](lpfeas-MOSEK.html) | 2.01 (1.94) | 100%|
|[📊 ORTOOLS-9.4](lpfeas-PDLP%.html) | 15.10 (14.60) | 77%|
|[📊 HiGHS-1.4.1](lpfeas-HiGHS.html) | 18.23 (17.60) | 82%|
|[📊 KNITRO-13.0.0](lpfeas-KNITRO.html) | 20.85 (20.10) | 70%|
|[📊 MATLAB-R2022b](lpfeas-MATL.html) | 27.38 (22.90) | 79%|
|[📊 Tulip-0.9.4](lpfeas-TULIP.html) | 70.61 (68.10) | 56%|

---


## [LPopt Benchmark (find optimal basic solution) (14 Dec 2022)](http://plato.asu.edu/ftp/lpopt.html)
Choose base solver for comparison:

| solver | score (as reported) | solved of 71|
| :--- | ---:  | ---:   |
|[⭐ virtual best](lpopt-vbest.html) | 0.81  | 100%|
|[🥇 COPT-6.0.3](lpopt-COPT.html) | 1.00 (1.00) | 100%|
|[🥈 Gurobi-10.0.0](lpopt-Gurob.html) | 1.18 (1.18) | 99%|
|[🥉 MOSEK-10.0.24](lpopt-MOSEK.html) | 5.14 (5.14) | 82%|
|[📊 Optverse-0.2.6](lpopt-OPTV.html) | 8.55 (8.55) | 77%|
|[📊 HiGHS-1.4.1](lpopt-HiGHS.html) | 16.89 (16.90) | 79%|
|[📊 CLP-1.17.7](lpopt-CLP.html) | 28.99 (29.00) | 61%|
|[📊 MATLAB-R2022b](lpopt-MATL.html) | 41.14 (41.10) | 65%|
|[📊 Google-GLOP](lpopt-GLOP.html) | 60.65 (60.70) | 48%|
|[📊 SOPLEX-6.0.0](lpopt-SPLX.html) | 98.11 (98.10) | 48%|

---


## [Large Network-LP Benchmark (commercial vs free) (9 Dec 2022)](http://plato.asu.edu/ftp/network.html)
Choose base solver for comparison:

| solver | score (as reported) | solved of 25|
| :--- | ---:  | ---:   |
|[⭐ virtual best](network-vbest.html) | 0.92  | 100%|
|[🥇 MindOpt-0.18.6](network-MDOPT.html) | 1.00 (1.00) | 100%|
|[🥈 OptVerse-0.2.6](network-OPTV.html) | 1.19 (1.19) | 100%|
|[🥉 Gurobi-10.0.0](network-GUR.html) | 1.33 (1.33) | 100%|
|[📊 COPT-5.0.0](network-COPT.html) | 1.68 (1.68) | 100%|
|[📊 Clp-1.17.7](network-CLP.html) | 4.71 (4.71) | 100%|
|[📊 HiGHS-1.4.1](network-HGHS.html) | 9.92 (9.92) | 80%|
|[📊 MATLAB-R2022b](network-MATL.html) | 16.52 (16.50) | 80%|
|[📊 MOSEK-10.0.24](network-MOSEK.html) | 20.36 (20.40) | 88%|
|[📊 QSopt-1.01](network-QSOPT.html) | 27.55 (27.60) | 68%|
|[📊 SOPLEX-6.0.0](network-SPLX.html) | 52.38 (52.40) | 64%|


<details><summary>previous benchmarks 🔽</summary>
<br>

<ul>
<li><a href="/mittelmann-plots/network-12-Nov-2022.html">12 Nov 2022</a></li>
<li><a href="/mittelmann-plots/network-3-Oct-2022.html">3 Oct 2022</a></li>
<li><a href="/mittelmann-plots/network-24-Aug-2022.html">24 Aug 2022</a></li>
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


## [The MIPLIB2017 Benchmark Instances - 8 threads (13 Nov 2022)](http://plato.asu.edu/ftp/milp.html)
Choose base solver for comparison:

| solver | score (as reported) | solved of 240|
| :--- | ---:  | ---:   |
|[⭐ virtual best](milp_8threads-vbest.html) | 0.82  | 96%|
|[🥇 Gurobi-10.0.0](milp_8threads-Gurobi.html) | 1.00 (1.00) | 95%|
|[🥈 COPT-6.0.1](milp_8threads-COPT.html) | 2.63 (2.63) | 82%|
|[🥉 SCIPC/spx-8.0.0](milp_8threads-SCIPC.html) | 8.92 (8.92) | 63%|
|[📊 HiGHS-1.3.0](milp_8threads-HiGHS.html) | 9.28 (9.27) | 65%|
|[📊 SCIP/spx-8.0.0](milp_8threads-SCIP.html) | 10.90 (10.90) | 57%|
|[📊 CBC-2.10.5](milp_8threads-CBC.html) | 16.30 (16.30) | 45%|


<details><summary>previous benchmarks 🔽</summary>
<br>

<ul>
<li><a href="/mittelmann-plots/milp_8threads-30-Oct-2022.html">30 Oct 2022</a></li>
<li><a href="/mittelmann-plots/milp_8threads-30-Jun-2022.html">30 Jun 2022</a></li>
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


## [MILP cases that are slightly pathological (26 Nov 2022)](http://plato.asu.edu/ftp/path.html)
Choose base solver for comparison:

| solver | score (as reported) | solved of 45|
| :--- | ---:  | ---:   |
|[⭐ virtual best](path-vbest.html) | 0.82  | 98%|
|[🥇 GUROBI-10.0.0](path-Gurobi.html) | 1.00 (1.00) | 98%|
|[🥈 COPT-5.0.0](path-COPT.html) | 4.79 (4.79) | 76%|
|[🥉 HiGHS-1.2.2](path-HiGHS.html) | 20.74 (20.70) | 56%|
|[📊 SCIPC-8.0.0](path-SCIPC.html) | 20.80 (20.80) | 51%|
|[📊 SCIP-8.0.0](path-SCIP.html) | 26.66 (26.70) | 42%|
|[📊 CBC-2.10.7](path-CBC.html) | 41.62 (41.60) | 11%|
|[📊 GLPK-5.0](path-GLPK.html) | 42.19 (42.20) | 13%|
|[📊 MATLAB-2020a](path-MATLAB.html) | 50.84 (50.80) | 7%|


<details><summary>previous benchmarks 🔽</summary>
<br>

<ul>
<li><a href="/mittelmann-plots/path-25-Jul-2022.html">25 Jul 2022</a></li>
<li><a href="/mittelmann-plots/path-6-Jul-2022.html">6 Jul 2022</a></li>
<li><a href="/mittelmann-plots/path-19-Jun-2022.html">19 Jun 2022</a></li>
<li><a href="/mittelmann-plots/path-27-Apr-2022.html">27 Apr 2022</a></li>
<li><a href="/mittelmann-plots/path-1-Feb-2022.html">1 Feb 2022</a></li>
<li><a href="/mittelmann-plots/path-26-Jan-2022.html">26 Jan 2022</a></li>
<li><a href="/mittelmann-plots/path-15-Dec-2021.html">15 Dec 2021</a></li>
<li><a href="/mittelmann-plots/path-11-Nov-2021.html">11 Nov 2021</a></li>
</ul></details>

---


## [Infeasibility Detection for MILP Problems (22 Nov 2022)](http://plato.asu.edu/ftp/infeas.html)
Choose base solver for comparison:

| solver | score (as reported) | solved of 32|
| :--- | ---:  | ---:   |
|[⭐ virtual best](infeas-vbest.html) | 0.92  | 94%|
|[🥇 GUROBI-10.0.0](infeas-Gurobi.html) | 1.00 (1.00) | 94%|
|[🥈 COPT-6.0.1](infeas-COPT.html) | 1.62 (1.62) | 94%|
|[🥉 SCIPC-8.0.0](infeas-SCIPC.html) | 6.24 (6.24) | 81%|
|[📊 SCIP-8.0.0](infeas-SCIP.html) | 8.00 (8.00) | 78%|
|[📊 HiGHS-1.2.2](infeas-HiGHS.html) | 10.72 (10.70) | 91%|
|[📊 CBC-2.10.5](infeas-CBC.html) | 19.53 (19.50) | 62%|
|[📊 MATLAB-2020b](infeas-MATLAB.html) | 30.36 (30.00) | 47%|


<details><summary>previous benchmarks 🔽</summary>
<br>

<ul>
<li><a href="/mittelmann-plots/infeas-24-Jul-2022.html">24 Jul 2022</a></li>
<li><a href="/mittelmann-plots/infeas-18-Jun-2022.html">18 Jun 2022</a></li>
<li><a href="/mittelmann-plots/infeas-25-Apr-2022.html">25 Apr 2022</a></li>
<li><a href="/mittelmann-plots/infeas-28-Jan-2022.html">28 Jan 2022</a></li>
<li><a href="/mittelmann-plots/infeas-14-Dec-2021.html">14 Dec 2021</a></li>
<li><a href="/mittelmann-plots/infeas-3-Dec-2021.html">3 Dec 2021</a></li>
<li><a href="/mittelmann-plots/infeas-10-Nov-2021.html">10 Nov 2021</a></li>
</ul></details>

---


## [Several SDP-codes on sparse and other SDP problems (4 Nov 2022)](http://plato.asu.edu/ftp/sparse_sdp.html)
Choose base solver for comparison:

| solver | score (as reported) | solved of 76|
| :--- | ---:  | ---:   |
|[⭐ virtual best](sparse_sdp-vbest.html) | 0.59  | 99%|
|[🥇 COPT-6.0.1](sparse_sdp-COPT.html) | 1.00 (1.00) | 99%|
|[🥈 MindOpt-0.22.0](sparse_sdp-MDOPT.html) | 1.77 (1.80) | 97%|
|[🥉 MOSEK-10.0.27](sparse_sdp-MOSEK.html) | 2.99 (3.07) | 95%|
|[📊 SDPT3-4.0](sparse_sdp-SDPT3.html) | 4.47 (4.62) | 91%|
|[📊 CSDP-6.2.0](sparse_sdp-CSDP.html) | 4.52 (4.68) | 92%|
|[📊 HDSDP-0.9.2](sparse_sdp-HDSDP.html) | 7.31 (7.62) | 92%|
|[📊 SDPA-7.4.2](sparse_sdp-SDPA.html) | 8.98 (9.39) | 80%|
|[📊 SeDuMi-1.3.5](sparse_sdp-SeDuMi.html) | 24.46 (25.90) | 82%|


<details><summary>previous benchmarks 🔽</summary>
<br>

<ul>
<li><a href="/mittelmann-plots/sparse_sdp-30-Oct-2022.html">30 Oct 2022</a></li>
<li><a href="/mittelmann-plots/sparse_sdp-13-Oct-2022.html">13 Oct 2022</a></li>
<li><a href="/mittelmann-plots/sparse_sdp-13-Sep-2022.html">13 Sep 2022</a></li>
<li><a href="/mittelmann-plots/sparse_sdp-29-Aug-2022.html">29 Aug 2022</a></li>
<li><a href="/mittelmann-plots/sparse_sdp-27-Jul-2022.html">27 Jul 2022</a></li>
</ul></details>

---


## [Large Second Order Cone Benchmark (12 Nov 2022)](http://plato.asu.edu/ftp/socp.html)
Choose base solver for comparison:

| solver | score (as reported) | solved of 18|
| :--- | ---:  | ---:   |
|[⭐ virtual best](socp-vbest.html) | 0.77  | 100%|
|[🥇 MOSEK-10.0.18](socp-MOSEK.html) | 1.00 (1.00) | 100%|
|[🥈 Gurobi-10.0.0](socp-Gurobi.html) | 1.11 (1.11) | 100%|
|[🥉 COPT-6.0.0](socp-COPT.html) | 1.15 (1.15) | 100%|
|[📊 KNITRO-13.0.0](socp-KNITRO.html) | 10.06 (10.10) | 83%|
|[📊 ECOS-2.0.4](socp-ECOS.html) | 83.02 (83.00) | 33%|


<details><summary>previous benchmarks 🔽</summary>
<br>

<ul>
<li><a href="/mittelmann-plots/socp-26-Oct-2022.html">26 Oct 2022</a></li>
<li><a href="/mittelmann-plots/socp-19-Sep-2022.html">19 Sep 2022</a></li>
<li><a href="/mittelmann-plots/socp-29-Aug-2022.html">29 Aug 2022</a></li>
<li><a href="/mittelmann-plots/socp-19-Jun-2022.html">19 Jun 2022</a></li>
<li><a href="/mittelmann-plots/socp-6-May-2022.html">6 May 2022</a></li>
<li><a href="/mittelmann-plots/socp-28-Jan-2022.html">28 Jan 2022</a></li>
<li><a href="/mittelmann-plots/socp-18-Jan-2022.html">18 Jan 2022</a></li>
<li><a href="/mittelmann-plots/socp-10-Nov-2021.html">10 Nov 2021</a></li>
</ul></details>

---


## [Mixed-integer SOCP Benchmark (12 Nov 2022)](http://plato.asu.edu/ftp/misocp.html)
Choose base solver for comparison:

| solver | score (as reported) | solved of 47|
| :--- | ---:  | ---:   |
|[⭐ virtual best](misocp-vbest.html) | 0.94  | 100%|
|[🥇 Gurobi-10.0.0](misocp-GUROBI.html) | 1.00 (1.00) | 100%|
|[🥈 COPT-6.0.1](misocp-COPT.html) | 2.78 (2.78) | 98%|
|[🥉 MOSEK-10.0.18](misocp-MOSEK.html) | 14.07 (14.10) | 72%|
|[📊 SCIP-8.0.0](misocp-SCIP.html) | 24.28 (24.30) | 66%|


<details><summary>previous benchmarks 🔽</summary>
<br>

<ul>
<li><a href="/mittelmann-plots/misocp-18-Oct-2022.html">18 Oct 2022</a></li>
<li><a href="/mittelmann-plots/misocp-12-Oct-2022.html">12 Oct 2022</a></li>
<li><a href="/mittelmann-plots/misocp-31-Aug-2022.html">31 Aug 2022</a></li>
<li><a href="/mittelmann-plots/misocp-5-May-2022.html">5 May 2022</a></li>
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


## [Binary Non-Convex QPLIB Benchmark (13 Nov 2022)](http://plato.asu.edu/ftp/qplib.html)
Choose base solver for comparison:

| solver | score (as reported) | solved of 96|
| :--- | ---:  | ---:   |
|[⭐ virtual best](qplib-vbest.html) | 0.69  | 100%|
|[🥇 Gurobi-10.0.0](qplib-GUROBI.html) | 1.00 (1.00) | 97%|
|[🥈 OCTERACT-4.5.1](qplib-OCTERACT.html) | 1.76 (1.76) | 95%|
|[🥉 Baron-22.9.1](qplib-BARON.html) | 7.59 (7.59) | 57%|
|[📊 SCIP-8.0.0](qplib-SCIP.html) | 38.48 (38.50) | 36%|
|[📊 ANTIGONE-1.1](qplib-ANTIGONE.html) | 78.03 (78.00) | 17%|
|[📊 COUENNE-0.5](qplib-COUENNE.html) | 92.85 (92.90) | 6%|


<details><summary>previous benchmarks 🔽</summary>
<br>

<ul>
<li><a href="/mittelmann-plots/qplib-3-Nov-2022.html">3 Nov 2022</a></li>
<li><a href="/mittelmann-plots/qplib-5-Sep-2022.html">5 Sep 2022</a></li>
<li><a href="/mittelmann-plots/qplib-3-Sep-2022.html">3 Sep 2022</a></li>
<li><a href="/mittelmann-plots/qplib-18-Aug-2022.html">18 Aug 2022</a></li>
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


## [Discrete Non-Convex QPLIB Benchmark (non-binary) (20 Nov 2022)](http://plato.asu.edu/ftp/nonbinary.html)
Choose base solver for comparison:

| solver | score (as reported) | solved of 97|
| :--- | ---:  | ---:   |
|[⭐ virtual best](nonbinary-vbest.html) | 0.25  | 95%|
|[🥇 Gurobi-10.0.0](nonbinary-GUROBI.html) | 1.00 (1.00) | 84%|
|[🥈 OCTERACT-4.5.1](nonbinary-OCTERACT.html) | 2.50 (5.65) | 76%|
|[🥉 SCIP-8.0.0](nonbinary-SCIP.html) | 8.25 (18.70) | 38%|
|[📊 Baron-22.9.1](nonbinary-BARON.html) | 13.23 (30.00) | 32%|
|[📊 ANTIGONE-1.1](nonbinary-ANTIGONE.html) | 14.14 (32.00) | 30%|
|[📊 MINOTAUR-0.3.0](nonbinary-MINOTAUR.html) | 17.15 (38.80) | 15%|
|[📊 COUENNE-0.5](nonbinary-COUENNE.html) | 26.73 (60.50) | 8%|


<details><summary>previous benchmarks 🔽</summary>
<br>

<ul>
<li><a href="/mittelmann-plots/nonbinary-10-Sep-2022.html">10 Sep 2022</a></li>
<li><a href="/mittelmann-plots/nonbinary-4-Sep-2022.html">4 Sep 2022</a></li>
<li><a href="/mittelmann-plots/nonbinary-16-Jul-2022.html">16 Jul 2022</a></li>
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


## [Continuous Non-Convex QPLIB Benchmark (20 Nov 2022)](http://plato.asu.edu/ftp/cnconv.html)
Choose base solver for comparison:

| solver | score (as reported) | solved of 69|
| :--- | ---:  | ---:   |
|[⭐ virtual best](cnconv-vbest.html) | 0.22  | 91%|
|[🥇 GUROBI-10.0.0](cnconv-GUROBI.html) | 1.00 (1.00) | 62%|
|[🥈 OCTERACT-4.5.1](cnconv-OCTERACT.html) | 1.33 (1.70) | 65%|
|[🥉 ANTIGONE-1.1](cnconv-ANTIGONE.html) | 3.85 (5.35) | 41%|
|[📊 Baron-22.9.1](cnconv-BARON.html) | 4.51 (6.55) | 28%|
|[📊 MINOTAUR-0.3.0](cnconv-MINOTAUR.html) | 5.43 (8.03) | 22%|
|[📊 SCIP-8.0.0](cnconv-SCIP.html) | 7.65 (11.40) | 19%|
|[📊 COUENNE-0.5](cnconv-COUENNE.html) | 8.69 (13.30) | 12%|


<details><summary>previous benchmarks 🔽</summary>
<br>

<ul>
<li><a href="/mittelmann-plots/cnconv-24-Oct-2022.html">24 Oct 2022</a></li>
<li><a href="/mittelmann-plots/cnconv-10-Sep-2022.html">10 Sep 2022</a></li>
<li><a href="/mittelmann-plots/cnconv-21-Jul-2022.html">21 Jul 2022</a></li>
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


## [Convex Continuous QPLIB Benchmark (26 Nov 2022)](http://plato.asu.edu/ftp/cconvex.html)
Choose base solver for comparison:

| solver | score (as reported) | solved of 32|
| :--- | ---:  | ---:   |
|[⭐ virtual best](cconvex-vbest.html) | 0.85  | 100%|
|[🥇 COPT-6.0.2](cconvex-COPT.html) | 1.00 (1.00) | 100%|
|[🥈 MOSEK-10.0.18](cconvex-MOSEK.html) | 1.33 (1.33) | 100%|
|[🥉 KNITRO-13.0.0](cconvex-KNITRO.html) | 1.53 (1.53) | 100%|
|[📊 Gurobi-10.0.0](cconvex-Gurobi.html) | 1.95 (1.95) | 94%|
|[📊 IPOPT-3.14.5](cconvex-IPOPT.html) | 7.29 (7.29) | 91%|


<details><summary>previous benchmarks 🔽</summary>
<br>

<ul>
<li><a href="/mittelmann-plots/cconvex-29-Aug-2022.html">29 Aug 2022</a></li>
<li><a href="/mittelmann-plots/cconvex-26-Jul-2022.html">26 Jul 2022</a></li>
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


## [Convex Discrete QPLIB Benchmark (12 Nov 2022)](http://plato.asu.edu/ftp/convex.html)
Choose base solver for comparison:

| solver | score (as reported) | solved of 31|
| :--- | ---:  | ---:   |
|[⭐ virtual best](convex-vbest.html) | 0.70  | 87%|
|[🥇 GUROBI-10.0.0](convex-GUROBI.html) | 1.00 (1.00) | 81%|
|[🥈 COPT-6.0.1](convex-COPT.html) | 1.09 (1.09) | 77%|
|[🥉 OCTACT](convex-OCTACT.html) | 6.72 (6.72) | 68%|
|[📊 Shot-1.1](convex-SHOT.html) | 8.42 (8.42) | 48%|
|[📊 MOSEK-10.0.18](convex-MOSEK.html) | 8.96 (8.96) | 61%|
|[📊 KNITRO-13.1.0](convex-KNITRO.html) | 12.88 (12.90) | 52%|
|[📊 Baron-22.9.1](convex-BARON.html) | 13.61 (13.60) | 58%|
|[📊 SCIP-8.0.0](convex-SCIP.html) | 35.52 (35.50) | 39%|
|[📊 MNTAUR](convex-MNTAUR.html) | 40.70 (40.70) | 45%|
|[📊 Bonmin-1.8.7](convex-BONMIN.html) | 52.55 (52.60) | 23%|


<details><summary>previous benchmarks 🔽</summary>
<br>

<ul>
<li><a href="/mittelmann-plots/convex-28-Oct-2022.html">28 Oct 2022</a></li>
<li><a href="/mittelmann-plots/convex-13-Oct-2022.html">13 Oct 2022</a></li>
<li><a href="/mittelmann-plots/convex-25-Sep-2022.html">25 Sep 2022</a></li>
<li><a href="/mittelmann-plots/convex-4-Sep-2022.html">4 Sep 2022</a></li>
<li><a href="/mittelmann-plots/convex-12-Aug-2022.html">12 Aug 2022</a></li>
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


## [Mixed Integer Nonlinear Programming Benchmark (MINLPLIB) (27 Oct 2022)](http://plato.asu.edu/ftp/minlp.html)
Choose base solver for comparison:

| solver | score (as reported) | solved of 87|
| :--- | ---:  | ---:   |
|[⭐ virtual best](minlp-vbest.html) | 0.31  | 99%|
|[🥇 OCTERACT](minlp-OCTERACT.html) | 1.00 (1.00) | 91%|
|[🥈 BARON](minlp-BARON.html) | 1.71 (1.72) | 82%|
|[🥉 SCIP](minlp-SCIP.html) | 2.04 (2.05) | 74%|
|[📊 ANTIGONE](minlp-ANTIGONE.html) | 7.68 (7.59) | 61%|
|[📊 LINDO](minlp-LINDO.html) | 10.10 (10.20) | 43%|
|[📊 COUENNE](minlp-COUENNE.html) | 17.38 (17.50) | 28%|


<details><summary>previous benchmarks 🔽</summary>
<br>

<ul>
<li><a href="/mittelmann-plots/minlp-26-Oct-2022.html">26 Oct 2022</a></li>
<li><a href="/mittelmann-plots/minlp-20-Sep-2022.html">20 Sep 2022</a></li>
<li><a href="/mittelmann-plots/minlp-4-Sep-2022.html">4 Sep 2022</a></li>
<li><a href="/mittelmann-plots/minlp-10-Aug-2022.html">10 Aug 2022</a></li>
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

