Interactive charts comparing the results of [Hans Mittelmann's benchmarks](http://plato.asu.edu/bench.html).
Each solver can be selected to show pairwise running time factors for every other solver in the respective benchmark.
These plots should make browsing the results easier.
The score ([scaled shifted geometric mean](http://plato.asu.edu/ftp/shgeom.html)) is recomputed using the reported solving times.
We also calculate a "virtual best" or "ensemble" solver that picks the best performance over all solvers for every single problem
instance. This might reveal how much potential the individual solvers still have.
[Please let me know](https://github.com/mattmilten/mittelmann-plots/issues/new) if you have a question or if there is an error.

    
## [LPfeas Benchmark (find PD feasible point) (8 Feb 2024)](http://plato.asu.edu/ftp/lpfeas.html)
Choose base solver for comparison:

| solver | score (as reported) | solved of 65|
| :--- | ---:  | ---:   |
|[⭐ virtual best](lpfeas-vbest.html) | 0.74  | 100%|
|[🥇 COPT-7.1.0](lpfeas-COPT.html) | 1.00 (1.00) | 100%|
|[🥈 Gurobi-11.0.0](lpfeas-Gurobi.html) | 1.29 (1.29) | 97%|
|[🥉 MindOpt-1.0.0](lpfeas-MDOPT.html) | 1.81 (1.81) | 97%|
|[📊 MOSEK-10.1.9](lpfeas-MOSEK.html) | 2.62 (2.62) | 98%|
|[📊 XOPT-0.0.3](lpfeas-XOPT.html) | 5.45 (5.45) | 91%|
|[📊 ORTOOLS-9.7](lpfeas-PDLP%.html) | 17.09 (17.10) | 75%|
|[📊 KNITRO-14.0.0](lpfeas-KNITRO.html) | 19.34 (19.30) | 74%|
|[📊 HiGHS-1.6.0](lpfeas-HiGHS.html) | 19.35 (19.30) | 80%|
|[📊 MATLAB-R2023a](lpfeas-MATL.html) | 27.07 (27.10) | 77%|
|[📊 Tulip-0.9.4](lpfeas-TULIP.html) | 66.89 (66.90) | 55%|


<details><summary>previous benchmarks 🔽</summary>
<br>

<ul>
<li><a href="/mittelmann-plots/lpfeas-5-Feb-2024.html">5 Feb 2024</a></li>
<li><a href="/mittelmann-plots/lpfeas-15-Jan-2024.html">15 Jan 2024</a></li>
<li><a href="/mittelmann-plots/lpfeas-12-Jan-2024.html">12 Jan 2024</a></li>
<li><a href="/mittelmann-plots/lpfeas-30-Nov-2023.html">30 Nov 2023</a></li>
<li><a href="/mittelmann-plots/lpfeas-4-Oct-2023.html">4 Oct 2023</a></li>
<li><a href="/mittelmann-plots/lpfeas-5-Sep-2023.html">5 Sep 2023</a></li>
<li><a href="/mittelmann-plots/lpfeas-1-Sep-2023.html">1 Sep 2023</a></li>
<li><a href="/mittelmann-plots/lpfeas-18-Aug-2023.html">18 Aug 2023</a></li>
<li><a href="/mittelmann-plots/lpfeas-16-Aug-2023.html">16 Aug 2023</a></li>
<li><a href="/mittelmann-plots/lpfeas-21-Jun-2023.html">21 Jun 2023</a></li>
<li><a href="/mittelmann-plots/lpfeas-24-Mar-2023.html">24 Mar 2023</a></li>
<li><a href="/mittelmann-plots/lpfeas-22-Mar-2023.html">22 Mar 2023</a></li>
<li><a href="/mittelmann-plots/lpfeas-9-Dec-2022.html">9 Dec 2022</a></li>
</ul></details>

---


## [LPopt Benchmark (find optimal basic solution) (8 Feb 2024)](http://plato.asu.edu/ftp/lpopt.html)
Choose base solver for comparison:

| solver | score (as reported) | solved of 65|
| :--- | ---:  | ---:   |
|[⭐ virtual best](lpopt-vbest.html) | 0.79  | 100%|
|[🥇 COPT-7.1.0](lpopt-COPT.html) | 1.00 (1.00) | 100%|
|[🥈 Gurobi-11.0.0](lpopt-Gurob.html) | 1.58 (1.58) | 97%|
|[🥉 Optverse-0.7.1](lpopt-OPTV.html) | 1.66 (1.66) | 98%|
|[📊 MindOpt-1.0.0](lpopt-MDOPT.html) | 1.89 (1.89) | 97%|
|[📊 MOSEK-10.1.9](lpopt-MOSEK.html) | 5.61 (5.61) | 80%|
|[📊 XOPT-0.0.3](lpopt-XOPT.html) | 6.79 (6.79) | 78%|
|[📊 HiGHS-1.6.0](lpopt-HiGHS.html) | 17.44 (17.40) | 78%|
|[📊 CLP-1.17.7](lpopt-CLP.html) | 26.13 (26.10) | 62%|
|[📊 MATLAB-R2022b](lpopt-MATL.html) | 39.83 (39.80) | 65%|
|[📊 Google-GLOP](lpopt-GLOP.html) | 56.97 (57.00) | 51%|
|[📊 SOPLEX-6.0.0](lpopt-SPLX.html) | 87.20 (87.20) | 49%|


<details><summary>previous benchmarks 🔽</summary>
<br>

<ul>
<li><a href="/mittelmann-plots/lpopt-13-Jan-2024.html">13 Jan 2024</a></li>
<li><a href="/mittelmann-plots/lpopt-13-Dec-2023.html">13 Dec 2023</a></li>
<li><a href="/mittelmann-plots/lpopt-5-Dec-2023.html">5 Dec 2023</a></li>
<li><a href="/mittelmann-plots/lpopt-30-Nov-2023.html">30 Nov 2023</a></li>
<li><a href="/mittelmann-plots/lpopt-5-Oct-2023.html">5 Oct 2023</a></li>
<li><a href="/mittelmann-plots/lpopt-5-Sep-2023.html">5 Sep 2023</a></li>
<li><a href="/mittelmann-plots/lpopt-18-Aug-2023.html">18 Aug 2023</a></li>
<li><a href="/mittelmann-plots/lpopt-16-Aug-2023.html">16 Aug 2023</a></li>
<li><a href="/mittelmann-plots/lpopt-24-Mar-2023.html">24 Mar 2023</a></li>
<li><a href="/mittelmann-plots/lpopt-25-Jan-2023.html">25 Jan 2023</a></li>
<li><a href="/mittelmann-plots/lpopt-14-Dec-2022.html">14 Dec 2022</a></li>
</ul></details>

---


## [Large Network-LP Benchmark (commercial vs free) (6 Feb 2024)](http://plato.asu.edu/ftp/network.html)
Choose base solver for comparison:

| solver | score (as reported) | solved of 25|
| :--- | ---:  | ---:   |
|[⭐ virtual best](network-vbest.html) | 0.87  | 100%|
|[🥇 OptVerse-0.7.0](network-OPTV.html) | 1.00 (1.00) | 100%|
|[🥈 MindOpt-1.0.0](network-MDOPT.html) | 1.18 (1.18) | 100%|
|[🥉 Gurobi-11.0.0](network-GUR.html) | 1.69 (1.69) | 100%|
|[📊 COPT-7.1.0](network-COPT.html) | 2.16 (2.16) | 100%|
|[📊 Clp-1.17.7](network-CLP.html) | 6.07 (6.07) | 100%|
|[📊 HiGHS-1.6.0](network-HGHS.html) | 12.65 (12.60) | 80%|
|[📊 MATLAB-R2022b](network-MATL.html) | 21.28 (21.30) | 80%|
|[📊 MOSEK-10.1.9](network-MOSEK.html) | 26.86 (26.90) | 88%|
|[📊 QSopt-1.01](network-QSOPT.html) | 35.49 (35.50) | 68%|
|[📊 SOPLEX-6.0.0](network-SPLX.html) | 67.48 (67.40) | 64%|


<details><summary>previous benchmarks 🔽</summary>
<br>

<ul>
<li><a href="/mittelmann-plots/network-4-Dec-2023.html">4 Dec 2023</a></li>
<li><a href="/mittelmann-plots/network-30-Nov-2023.html">30 Nov 2023</a></li>
<li><a href="/mittelmann-plots/network-4-Oct-2023.html">4 Oct 2023</a></li>
<li><a href="/mittelmann-plots/network-18-Aug-2023.html">18 Aug 2023</a></li>
<li><a href="/mittelmann-plots/network-27-Jun-2023.html">27 Jun 2023</a></li>
<li><a href="/mittelmann-plots/network-24-Mar-2023.html">24 Mar 2023</a></li>
<li><a href="/mittelmann-plots/network-24-Jan-2023.html">24 Jan 2023</a></li>
<li><a href="/mittelmann-plots/network-9-Dec-2022.html">9 Dec 2022</a></li>
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


## [The MIPLIB2017 Benchmark Instances - 8 threads (4 Mar 2024)](http://plato.asu.edu/ftp/milp.html)
Choose base solver for comparison:

| solver | score (as reported) | solved of 240|
| :--- | ---:  | ---:   |
|[⭐ virtual best](milp_8threads-vbest.html) | 0.66  | 98%|
|[🥇 Gurobi-11.0.0](milp_8threads-Gurobi.html) | 1.00 (1.00) | 95%|
|[🥈 COPT-7.1.0](milp_8threads-COPT.html) | 1.44 (1.44) | 92%|
|[🥉 OptVerse-0.7.0](milp_8threads-optverse.html) | 2.88 (2.88) | 84%|
|[📊 MindOpt-1.0.0](milp_8threads-MindOpt.html) | 4.18 (4.18) | 82%|
|[📊 XOPT-0.0.3](milp_8threads-XOPT.html) | 7.09 (7.09) | 75%|
|[📊 HiGHS-1.6.0](milp_8threads-HiGHS.html) | 9.98 (9.98) | 66%|
|[📊 SCIPC/spx-8.1.0](milp_8threads-SCIPC.html) | 10.59 (10.60) | 63%|
|[📊 SCIP/spx-8.1.0](milp_8threads-SCIP.html) | 12.46 (12.50) | 55%|
|[📊 CBC-2.10.5](milp_8threads-CBC.html) | 18.42 (18.40) | 45%|
|[📊 MATLAB-2023a](milp_8threads-Matlab.html) | 37.65 (37.60) | 30%|


<details><summary>previous benchmarks 🔽</summary>
<br>

<ul>
<li><a href="/mittelmann-plots/milp_8threads-7-Feb-2024.html">7 Feb 2024</a></li>
<li><a href="/mittelmann-plots/milp_8threads-1-Feb-2024.html">1 Feb 2024</a></li>
<li><a href="/mittelmann-plots/milp_8threads-26-Jan-2024.html">26 Jan 2024</a></li>
<li><a href="/mittelmann-plots/milp_8threads-18-Dec-2023.html">18 Dec 2023</a></li>
<li><a href="/mittelmann-plots/milp_8threads-17-Dec-2023.html">17 Dec 2023</a></li>
<li><a href="/mittelmann-plots/milp_8threads-7-Dec-2023.html">7 Dec 2023</a></li>
<li><a href="/mittelmann-plots/milp_8threads-1-Dec-2023.html">1 Dec 2023</a></li>
<li><a href="/mittelmann-plots/milp_8threads-4-Oct-2023.html">4 Oct 2023</a></li>
<li><a href="/mittelmann-plots/milp_8threads-19-Aug-2023.html">19 Aug 2023</a></li>
<li><a href="/mittelmann-plots/milp_8threads-29-Jun-2023.html">29 Jun 2023</a></li>
<li><a href="/mittelmann-plots/milp_8threads-1-Apr-2023.html">1 Apr 2023</a></li>
<li><a href="/mittelmann-plots/milp_8threads-26-Mar-2023.html">26 Mar 2023</a></li>
<li><a href="/mittelmann-plots/milp_8threads-13-Nov-2022.html">13 Nov 2022</a></li>
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


## [MILP cases that are slightly pathological (7 Mar 2024)](http://plato.asu.edu/ftp/path.html)
Choose base solver for comparison:

| solver | score (as reported) | solved of 45|
| :--- | ---:  | ---:   |
|[⭐ virtual best](path-vbest.html) | 0.55  | 98%|
|[🥇 GUROBI-11.0.0](path-Gurobi.html) | 1.00 (1.00) | 96%|
|[🥈 COPT-7.1.0](path-COPT.html) | 1.98 (1.98) | 87%|
|[🥉 OptVerse-0.7.0](path-optverse.html) | 3.89 (3.89) | 80%|
|[📊 MindOpt-1.0.0](path-MindOpt.html) | 16.84 (16.80) | 44%|
|[📊 XOPT-0.0.3](path-XOPT.html) | 18.12 (18.10) | 47%|
|[📊 HiGHS-1.6.0](path-HiGHS.html) | 19.42 (19.40) | 53%|
|[📊 SCIPC-9.0.0](path-SCIPC.html) | 25.00 (25.00) | 47%|
|[📊 SCIP-9.0.0](path-SCIP.html) | 30.12 (30.10) | 42%|
|[📊 CBC-2.10.7](path-CBC.html) | 45.02 (45.00) | 11%|
|[📊 GLPK-5.0](path-GLPK.html) | 45.63 (45.60) | 13%|
|[📊 MATLAB-2023a](path-MATLAB.html) | 60.86 (60.90) | 4%|


<details><summary>previous benchmarks 🔽</summary>
<br>

<ul>
<li><a href="/mittelmann-plots/path-5-Feb-2024.html">5 Feb 2024</a></li>
<li><a href="/mittelmann-plots/path-17-Jan-2024.html">17 Jan 2024</a></li>
<li><a href="/mittelmann-plots/path-15-Jan-2024.html">15 Jan 2024</a></li>
<li><a href="/mittelmann-plots/path-17-Dec-2023.html">17 Dec 2023</a></li>
<li><a href="/mittelmann-plots/path-8-Dec-2023.html">8 Dec 2023</a></li>
<li><a href="/mittelmann-plots/path-30-Nov-2023.html">30 Nov 2023</a></li>
<li><a href="/mittelmann-plots/path-5-Oct-2023.html">5 Oct 2023</a></li>
<li><a href="/mittelmann-plots/path-25-Jun-2023.html">25 Jun 2023</a></li>
<li><a href="/mittelmann-plots/path-9-Apr-2023.html">9 Apr 2023</a></li>
<li><a href="/mittelmann-plots/path-26-Mar-2023.html">26 Mar 2023</a></li>
<li><a href="/mittelmann-plots/path-26-Nov-2022.html">26 Nov 2022</a></li>
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


## [Infeasibility Detection for MILP Problems (29 Feb 2024)](http://plato.asu.edu/ftp/infeas.html)
Choose base solver for comparison:

| solver | score (as reported) | solved of 32|
| :--- | ---:  | ---:   |
|[⭐ virtual best](infeas-vbest.html) | 0.98  | 94%|
|[🥇 GUROBI-11.0.0](infeas-Gurobi.html) | 1.00 (1.00) | 94%|
|[🥈 COPT-7.1.0](infeas-COPT.html) | 1.37 (1.37) | 94%|
|[🥉 OptVerse-0.7.0](infeas-optverse.html) | 3.00 (3.00) | 88%|
|[📊 XOPT-0.0.3](infeas-XOPT.html) | 7.34 (7.34) | 78%|
|[📊 MindOpt-1.0.0](infeas-MindOpt.html) | 7.81 (7.81) | 84%|
|[📊 SCIPC-9.0.0](infeas-SCIPC.html) | 7.96 (7.96) | 78%|
|[📊 HiGHS-1.6.0](infeas-HiGHS.html) | 8.18 (8.18) | 81%|
|[📊 SCIP-9.0.0](infeas-SCIP.html) | 10.97 (10.30) | 81%|
|[📊 CBC-2.10.5](infeas-CBC.html) | 22.51 (22.50) | 62%|
|[📊 MATLAB-2023a](infeas-MATLAB.html) | 44.55 (44.50) | 50%|


<details><summary>previous benchmarks 🔽</summary>
<br>

<ul>
<li><a href="/mittelmann-plots/infeas-6-Feb-2024.html">6 Feb 2024</a></li>
<li><a href="/mittelmann-plots/infeas-14-Jan-2024.html">14 Jan 2024</a></li>
<li><a href="/mittelmann-plots/infeas-13-Jan-2024.html">13 Jan 2024</a></li>
<li><a href="/mittelmann-plots/infeas-6-Dec-2023.html">6 Dec 2023</a></li>
<li><a href="/mittelmann-plots/infeas-30-Nov-2023.html">30 Nov 2023</a></li>
<li><a href="/mittelmann-plots/infeas-4-Oct-2023.html">4 Oct 2023</a></li>
<li><a href="/mittelmann-plots/infeas-27-Jun-2023.html">27 Jun 2023</a></li>
<li><a href="/mittelmann-plots/infeas-13-Apr-2023.html">13 Apr 2023</a></li>
<li><a href="/mittelmann-plots/infeas-24-Mar-2023.html">24 Mar 2023</a></li>
<li><a href="/mittelmann-plots/infeas-22-Nov-2022.html">22 Nov 2022</a></li>
<li><a href="/mittelmann-plots/infeas-24-Jul-2022.html">24 Jul 2022</a></li>
<li><a href="/mittelmann-plots/infeas-18-Jun-2022.html">18 Jun 2022</a></li>
<li><a href="/mittelmann-plots/infeas-25-Apr-2022.html">25 Apr 2022</a></li>
<li><a href="/mittelmann-plots/infeas-28-Jan-2022.html">28 Jan 2022</a></li>
<li><a href="/mittelmann-plots/infeas-14-Dec-2021.html">14 Dec 2021</a></li>
<li><a href="/mittelmann-plots/infeas-3-Dec-2021.html">3 Dec 2021</a></li>
<li><a href="/mittelmann-plots/infeas-10-Nov-2021.html">10 Nov 2021</a></li>
</ul></details>

---


## [Several SDP-codes on sparse and other SDP problems (8 Feb 2024)](http://plato.asu.edu/ftp/sparse_sdp.html)
Choose base solver for comparison:

| solver | score (as reported) | solved of 75|
| :--- | ---:  | ---:   |
|[⭐ virtual best](sparse_sdp-vbest.html) | 0.61  | 100%|
|[🥇 COPT-7.1.0](sparse_sdp-COPT.html) | 1.00 (1.00) | 100%|
|[🥈 MindOpt-1.0.0](sparse_sdp-MDOPT.html) | 1.45 (1.45) | 100%|
|[🥉 MOSEK-10.1.23](sparse_sdp-MOSEK.html) | 3.67 (3.67) | 97%|
|[📊 SDPT3-4.0](sparse_sdp-SDPT3.html) | 5.18 (5.18) | 92%|
|[📊 CSDP-6.2.0](sparse_sdp-CSDP.html) | 5.25 (5.25) | 93%|
|[📊 HDSDP-1.0.0](sparse_sdp-HDSDP.html) | 7.91 (7.91) | 93%|
|[📊 SDPA-7.4.2](sparse_sdp-SDPA.html) | 10.52 (10.50) | 81%|
|[📊 SeDuMi-1.3.5](sparse_sdp-SeDuMi.html) | 29.06 (29.10) | 83%|


<details><summary>previous benchmarks 🔽</summary>
<br>

<ul>
<li><a href="/mittelmann-plots/sparse_sdp-1-Feb-2024.html">1 Feb 2024</a></li>
<li><a href="/mittelmann-plots/sparse_sdp-28-Sep-2023.html">28 Sep 2023</a></li>
<li><a href="/mittelmann-plots/sparse_sdp-19-Aug-2023.html">19 Aug 2023</a></li>
<li><a href="/mittelmann-plots/sparse_sdp-6-Aug-2023.html">6 Aug 2023</a></li>
<li><a href="/mittelmann-plots/sparse_sdp-27-Jun-2023.html">27 Jun 2023</a></li>
<li><a href="/mittelmann-plots/sparse_sdp-24-Mar-2023.html">24 Mar 2023</a></li>
<li><a href="/mittelmann-plots/sparse_sdp-4-Nov-2022.html">4 Nov 2022</a></li>
<li><a href="/mittelmann-plots/sparse_sdp-30-Oct-2022.html">30 Oct 2022</a></li>
<li><a href="/mittelmann-plots/sparse_sdp-13-Oct-2022.html">13 Oct 2022</a></li>
<li><a href="/mittelmann-plots/sparse_sdp-13-Sep-2022.html">13 Sep 2022</a></li>
<li><a href="/mittelmann-plots/sparse_sdp-29-Aug-2022.html">29 Aug 2022</a></li>
<li><a href="/mittelmann-plots/sparse_sdp-27-Jul-2022.html">27 Jul 2022</a></li>
</ul></details>

---


## [Large Second Order Cone Benchmark (7 Feb 2024)](http://plato.asu.edu/ftp/socp.html)
Choose base solver for comparison:

| solver | score (as reported) | solved of 18|
| :--- | ---:  | ---:   |
|[⭐ virtual best](socp-vbest.html) | 0.80  | 100%|
|[🥇 COPT-7.1.0](socp-COPT.html) | 1.00 (1.00) | 100%|
|[🥈 MOSEK-10.1.9](socp-MOSEK.html) | 1.06 (1.06) | 100%|
|[🥉 Gurobi-11.0.0](socp-Gurobi.html) | 1.11 (1.11) | 100%|
|[📊 KNITRO-14.0.0](socp-KNITRO.html) | 9.24 (9.24) | 94%|
|[📊 ECOS-2.0.4](socp-ECOS.html) | 97.22 (97.20) | 61%|


<details><summary>previous benchmarks 🔽</summary>
<br>

<ul>
<li><a href="/mittelmann-plots/socp-30-Nov-2023.html">30 Nov 2023</a></li>
<li><a href="/mittelmann-plots/socp-27-Sep-2023.html">27 Sep 2023</a></li>
<li><a href="/mittelmann-plots/socp-17-Aug-2023.html">17 Aug 2023</a></li>
<li><a href="/mittelmann-plots/socp-28-Mar-2023.html">28 Mar 2023</a></li>
<li><a href="/mittelmann-plots/socp-24-Mar-2023.html">24 Mar 2023</a></li>
<li><a href="/mittelmann-plots/socp-12-Nov-2022.html">12 Nov 2022</a></li>
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


## [Mixed-integer SOCP Benchmark (9 Feb 2024)](http://plato.asu.edu/ftp/misocp.html)
Choose base solver for comparison:

| solver | score (as reported) | solved of 47|
| :--- | ---:  | ---:   |
|[⭐ virtual best](misocp-vbest.html) | 0.97  | 100%|
|[🥇 Gurobi-11.0.0](misocp-GUROBI.html) | 1.00 (1.00) | 100%|
|[🥈 COPT-7.1.0](misocp-COPT.html) | 2.20 (2.16) | 98%|
|[🥉 MOSEK-10.1.9](misocp-MOSEK.html) | 10.68 (9.00) | 77%|
|[📊 SCIP-8.1.0](misocp-SCIP.html) | 26.84 (21.10) | 66%|


<details><summary>previous benchmarks 🔽</summary>
<br>

<ul>
<li><a href="/mittelmann-plots/misocp-7-Feb-2024.html">7 Feb 2024</a></li>
<li><a href="/mittelmann-plots/misocp-30-Nov-2023.html">30 Nov 2023</a></li>
<li><a href="/mittelmann-plots/misocp-27-Sep-2023.html">27 Sep 2023</a></li>
<li><a href="/mittelmann-plots/misocp-17-Aug-2023.html">17 Aug 2023</a></li>
<li><a href="/mittelmann-plots/misocp-25-Mar-2023.html">25 Mar 2023</a></li>
<li><a href="/mittelmann-plots/misocp-4-Mar-2023.html">4 Mar 2023</a></li>
<li><a href="/mittelmann-plots/misocp-12-Nov-2022.html">12 Nov 2022</a></li>
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


## [Binary Non-Convex QPLIB Benchmark (11 Feb 2024)](http://plato.asu.edu/ftp/qplib.html)
Choose base solver for comparison:

| solver | score (as reported) | solved of 97|
| :--- | ---:  | ---:   |
|[⭐ virtual best](qplib-vbest.html) | 0.70  | 100%|
|[🥇 Gurobi-11.0.0](qplib-GUROBI.html) | 1.00 (1.00) | 97%|
|[🥈 SHOT-1.1](qplib-SHOT.html) | 1.48 (1.48) | 88%|
|[🥉 OCTERACT-4.7.1](qplib-OCTERACT.html) | 1.69 (1.69) | 96%|
|[📊 Baron-24.1.30](qplib-BARON.html) | 8.44 (8.44) | 67%|
|[📊 SCIP-8.1.0](qplib-SCIP.html) | 38.80 (38.80) | 37%|
|[📊 ANTIGONE-1.1](qplib-ANTIGONE.html) | 81.19 (81.20) | 16%|
|[📊 COUENNE-0.5](qplib-COUENNE.html) | 96.45 (96.40) | 6%|


<details><summary>previous benchmarks 🔽</summary>
<br>

<ul>
<li><a href="/mittelmann-plots/qplib-11-Jan-2024.html">11 Jan 2024</a></li>
<li><a href="/mittelmann-plots/qplib-1-Dec-2023.html">1 Dec 2023</a></li>
<li><a href="/mittelmann-plots/qplib-12-Jul-2023.html">12 Jul 2023</a></li>
<li><a href="/mittelmann-plots/qplib-20-Apr-2023.html">20 Apr 2023</a></li>
<li><a href="/mittelmann-plots/qplib-9-Mar-2023.html">9 Mar 2023</a></li>
<li><a href="/mittelmann-plots/qplib-28-Feb-2023.html">28 Feb 2023</a></li>
<li><a href="/mittelmann-plots/qplib-4-Feb-2023.html">4 Feb 2023</a></li>
<li><a href="/mittelmann-plots/qplib-13-Nov-2022.html">13 Nov 2022</a></li>
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


## [Nonconvex QUBO-QPLIB Benchmark (10 Feb 2024)](http://plato.asu.edu/ftp/qubo.html)
Choose base solver for comparison:

| solver | score (as reported) | solved of 23|
| :--- | ---:  | ---:   |
|[⭐ virtual best](qubo-vbest.html) | 0.87  | 70%|
|[🥇 QuBowl](qubo-QUBOWL.html) | 1.00 (1.00) | 65%|
|[🥈 Gurobi-11.0.0](qubo-GUROBI.html) | 1.30 (1.30) | 57%|
|[🥉 OCTERACT-4.7.1](qubo-OCTERACT.html) | 1.74 (1.74) | 52%|
|[📊 SHOT-1.1](qubo-SHOT.html) | 1.76 (1.76) | 52%|
|[📊 Baron-24.1.30](qubo-BARON.html) | 1.82 (1.82) | 52%|
|[📊 McSparse-2.0](qubo-MCSPARSE.html) | 2.36 (2.36) | 52%|
|[📊 Biqbin](qubo-BIQBIN.html) | 5.40 (5.40) | 39%|
|[📊 SCIP-8.1](qubo-SCIP.html) | 5.46 (5.46) | 35%|


<details><summary>previous benchmarks 🔽</summary>
<br>

<ul>
<li><a href="/mittelmann-plots/qubo-9-Feb-2024.html">9 Feb 2024</a></li>
<li><a href="/mittelmann-plots/qubo-10-Jan-2024.html">10 Jan 2024</a></li>
<li><a href="/mittelmann-plots/qubo-30-Nov-2023.html">30 Nov 2023</a></li>
<li><a href="/mittelmann-plots/qubo-20-Sep-2023.html">20 Sep 2023</a></li>
<li><a href="/mittelmann-plots/qubo-10-Jul-2023.html">10 Jul 2023</a></li>
<li><a href="/mittelmann-plots/qubo-22-Apr-2023.html">22 Apr 2023</a></li>
<li><a href="/mittelmann-plots/qubo-19-Apr-2023.html">19 Apr 2023</a></li>
<li><a href="/mittelmann-plots/qubo-8-Mar-2023.html">8 Mar 2023</a></li>
<li><a href="/mittelmann-plots/qubo-26-Feb-2023.html">26 Feb 2023</a></li>
<li><a href="/mittelmann-plots/qubo-16-Feb-2023.html">16 Feb 2023</a></li>
<li><a href="/mittelmann-plots/qubo-10-Feb-2023.html">10 Feb 2023</a></li>
</ul></details>

---


## [Discrete Non-Convex QPLIB Benchmark (non-binary) (22 Feb 2024)](http://plato.asu.edu/ftp/nonbinary.html)
Choose base solver for comparison:

| solver | score (as reported) | solved of 112|
| :--- | ---:  | ---:   |
|[⭐ virtual best](nonbinary-vbest.html) | 0.30  | 97%|
|[🥇 Gurobi-11.0.0](nonbinary-GUROBI.html) | 1.00 (1.00) | 83%|
|[🥈 SHOT-1.1](nonbinary-SHOT.html) | 2.23 (2.23) | 72%|
|[🥉 OCTERACT-4.7.1](nonbinary-OCTERACT.html) | 5.47 (5.47) | 71%|
|[📊 Baron-24.1.30](nonbinary-BARON.html) | 6.19 (6.19) | 59%|
|[📊 SCIP-8.1.0](nonbinary-SCIP.html) | 24.00 (24.00) | 37%|
|[📊 ANTIGONE-1.1](nonbinary-ANTIGONE.html) | 43.22 (43.20) | 26%|
|[📊 MINOTAUR-0.3.0](nonbinary-MINOTAUR.html) | 51.09 (51.10) | 13%|


<details><summary>previous benchmarks 🔽</summary>
<br>

<ul>
<li><a href="/mittelmann-plots/nonbinary-20-Feb-2024.html">20 Feb 2024</a></li>
<li><a href="/mittelmann-plots/nonbinary-13-Jan-2024.html">13 Jan 2024</a></li>
<li><a href="/mittelmann-plots/nonbinary-6-Dec-2023.html">6 Dec 2023</a></li>
<li><a href="/mittelmann-plots/nonbinary-14-Jul-2023.html">14 Jul 2023</a></li>
<li><a href="/mittelmann-plots/nonbinary-23-Apr-2023.html">23 Apr 2023</a></li>
<li><a href="/mittelmann-plots/nonbinary-11-Mar-2023.html">11 Mar 2023</a></li>
<li><a href="/mittelmann-plots/nonbinary-6-Feb-2023.html">6 Feb 2023</a></li>
<li><a href="/mittelmann-plots/nonbinary-20-Nov-2022.html">20 Nov 2022</a></li>
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


## [Continuous Non-Convex QPLIB Benchmark (9 Mar 2024)](http://plato.asu.edu/ftp/cnconv.html)
Choose base solver for comparison:

| solver | score (as reported) | solved of 71|
| :--- | ---:  | ---:   |
|[⭐ virtual best](cnconv-vbest.html) | 0.18  | 96%|
|[🥇 GUROBI-11.0.0](cnconv-GUROBI.html) | 1.00 (1.00) | 62%|
|[🥈 OCTERACT-4.7.1](cnconv-OCTERACT.html) | 1.51 (1.51) | 65%|
|[🥉 Baron-24.1.30](cnconv-BARON.html) | 2.46 (2.46) | 46%|
|[📊 ANTIGONE-1.1](cnconv-ANTIGONE.html) | 5.18 (5.18) | 39%|
|[📊 MINOTAUR-0.4.0](cnconv-MINOTAUR.html) | 6.87 (6.87) | 23%|
|[📊 SCIP-8.1.0](cnconv-SCIP.html) | 9.15 (9.15) | 20%|
|[📊 COUENNE-0.5](cnconv-COUENNE.html) | 11.44 (11.40) | 11%|
|[📊 RAPOSa-4.0.2](cnconv-RAPOSA.html) | 14.29 (14.30) | 6%|


<details><summary>previous benchmarks 🔽</summary>
<br>

<ul>
<li><a href="/mittelmann-plots/cnconv-22-Feb-2024.html">22 Feb 2024</a></li>
<li><a href="/mittelmann-plots/cnconv-14-Jan-2024.html">14 Jan 2024</a></li>
<li><a href="/mittelmann-plots/cnconv-5-Dec-2023.html">5 Dec 2023</a></li>
<li><a href="/mittelmann-plots/cnconv-18-Jul-2023.html">18 Jul 2023</a></li>
<li><a href="/mittelmann-plots/cnconv-26-Apr-2023.html">26 Apr 2023</a></li>
<li><a href="/mittelmann-plots/cnconv-6-Apr-2023.html">6 Apr 2023</a></li>
<li><a href="/mittelmann-plots/cnconv-15-Mar-2023.html">15 Mar 2023</a></li>
<li><a href="/mittelmann-plots/cnconv-8-Feb-2023.html">8 Feb 2023</a></li>
<li><a href="/mittelmann-plots/cnconv-7-Jan-2023.html">7 Jan 2023</a></li>
<li><a href="/mittelmann-plots/cnconv-20-Nov-2022.html">20 Nov 2022</a></li>
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


## [Convex Continuous QPLIB Benchmark (ext) (12 Mar 2024)](http://plato.asu.edu/ftp/cconvex.html)
Choose base solver for comparison:

| solver | score (as reported) | solved of 42|
| :--- | ---:  | ---:   |
|[⭐ virtual best](cconvex-vbest.html) | 0.73  | 100%|
|[🥇 COPT-7.1.0](cconvex-COPT.html) | 1.00 (1.00) | 100%|
|[🥈 OptVerse-0.7.0](cconvex-OPTVERS.html) | 1.28 (1.28) | 98%|
|[🥉 KNITRO-14.0.0](cconvex-KNITRO.html) | 1.49 (1.49) | 98%|
|[📊 Gurobi-11.0.0](cconvex-Gurobi.html) | 1.59 (1.59) | 98%|
|[📊 MOSEK-10.1.21](cconvex-MOSEK.html) | 1.60 (1.60) | 98%|
|[📊 MindOpt-1.0.0](cconvex-MINDOPT.html) | 5.74 (5.43) | 81%|
|[📊 IPOPT-3.14.5](cconvex-IPOPT.html) | 8.95 (8.95) | 83%|
|[📊 Mnotaur](cconvex-Mnotaur.html) | 45.32 (45.00) | 60%|


<details><summary>previous benchmarks 🔽</summary>
<br>

<ul>
<li><a href="/mittelmann-plots/cconvex-7-Feb-2024.html">7 Feb 2024</a></li>
<li><a href="/mittelmann-plots/cconvex-5-Feb-2024.html">5 Feb 2024</a></li>
<li><a href="/mittelmann-plots/cconvex-9-Dec-2023.html">9 Dec 2023</a></li>
<li><a href="/mittelmann-plots/cconvex-4-Dec-2023.html">4 Dec 2023</a></li>
<li><a href="/mittelmann-plots/cconvex-29-Nov-2023.html">29 Nov 2023</a></li>
<li><a href="/mittelmann-plots/cconvex-12-Nov-2023.html">12 Nov 2023</a></li>
<li><a href="/mittelmann-plots/cconvex-11-Nov-2023.html">11 Nov 2023</a></li>
<li><a href="/mittelmann-plots/cconvex-5-Nov-2023.html">5 Nov 2023</a></li>
<li><a href="/mittelmann-plots/cconvex-26-Aug-2023.html">26 Aug 2023</a></li>
<li><a href="/mittelmann-plots/cconvex-29-Jun-2023.html">29 Jun 2023</a></li>
<li><a href="/mittelmann-plots/cconvex-6-May-2023.html">6 May 2023</a></li>
<li><a href="/mittelmann-plots/cconvex-25-Mar-2023.html">25 Mar 2023</a></li>
<li><a href="/mittelmann-plots/cconvex-26-Nov-2022.html">26 Nov 2022</a></li>
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


## [Convex Discrete QPLIB Benchmark (11 Mar 2024)](http://plato.asu.edu/ftp/convex.html)
Choose base solver for comparison:

| solver | score (as reported) | solved of 31|
| :--- | ---:  | ---:   |
|[⭐ virtual best](convex-vbest.html) | 0.68  | 87%|
|[🥇 GUROBI-11.0.0](convex-GUROBI.html) | 1.00 (1.00) | 81%|
|[🥈 COPT-7.1.0](convex-COPT.html) | 1.00 (1.00) | 77%|
|[🥉 Shot-1.1](convex-SHOT.html) | 1.18 (1.18) | 81%|
|[📊 OCTERACT-4.7.1](convex-OCTACT.html) | 2.44 (2.44) | 77%|
|[📊 Baron-24.1.30](convex-BARON.html) | 3.45 (3.45) | 65%|
|[📊 MOSEK-10.1.23](convex-MOSEK.html) | 10.05 (10.00) | 58%|
|[📊 KNITRO-14.0.0](convex-KNITRO.html) | 13.63 (13.60) | 52%|
|[📊 SCIP-8.1.0](convex-SCIP.html) | 26.71 (26.70) | 42%|
|[📊 Bonmin-1.8.7](convex-BONMIN.html) | 54.64 (54.60) | 23%|
|[📊 MNTAUR](convex-MNTAUR.html) | 63.99 (64.00) | 26%|


<details><summary>previous benchmarks 🔽</summary>
<br>

<ul>
<li><a href="/mittelmann-plots/convex-11-Feb-2024.html">11 Feb 2024</a></li>
<li><a href="/mittelmann-plots/convex-9-Feb-2024.html">9 Feb 2024</a></li>
<li><a href="/mittelmann-plots/convex-5-Feb-2024.html">5 Feb 2024</a></li>
<li><a href="/mittelmann-plots/convex-1-Feb-2024.html">1 Feb 2024</a></li>
<li><a href="/mittelmann-plots/convex-10-Jan-2024.html">10 Jan 2024</a></li>
<li><a href="/mittelmann-plots/convex-30-Nov-2023.html">30 Nov 2023</a></li>
<li><a href="/mittelmann-plots/convex-27-Sep-2023.html">27 Sep 2023</a></li>
<li><a href="/mittelmann-plots/convex-17-Aug-2023.html">17 Aug 2023</a></li>
<li><a href="/mittelmann-plots/convex-10-Jul-2023.html">10 Jul 2023</a></li>
<li><a href="/mittelmann-plots/convex-30-Jun-2023.html">30 Jun 2023</a></li>
<li><a href="/mittelmann-plots/convex-19-Apr-2023.html">19 Apr 2023</a></li>
<li><a href="/mittelmann-plots/convex-25-Mar-2023.html">25 Mar 2023</a></li>
<li><a href="/mittelmann-plots/convex-8-Mar-2023.html">8 Mar 2023</a></li>
<li><a href="/mittelmann-plots/convex-1-Feb-2023.html">1 Feb 2023</a></li>
<li><a href="/mittelmann-plots/convex-12-Nov-2022.html">12 Nov 2022</a></li>
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


## [Mixed Integer Nonlinear Programming Benchmark (MINLPLIB) (7 Feb 2024)](http://plato.asu.edu/ftp/minlp.html)
Choose base solver for comparison:

| solver | score (as reported) | solved of 87|
| :--- | ---:  | ---:   |
|[⭐ virtual best](minlp-vbest.html) | 0.41  | 100%|
|[🥇 OCTERACT](minlp-OCTERACT.html) | 1.00 (1.00) | 100%|
|[🥈 BARON](minlp-BARON.html) | 2.42 (2.40) | 89%|
|[🥉 SHOT](minlp-SHOT.html) | 7.17 (6.20) | 62%|
|[📊 SCIP](minlp-SCIP.html) | 9.87 (9.90) | 75%|
|[📊 LINDO](minlp-LINDO.html) | 32.85 (32.80) | 48%|
|[📊 ANTIGONE](minlp-ANTIGONE.html) | 39.32 (39.30) | 61%|
|[📊 COUENNE](minlp-COUENNE.html) | 89.78 (89.80) | 28%|


<details><summary>previous benchmarks 🔽</summary>
<br>

<ul>
<li><a href="/mittelmann-plots/minlp-6-Feb-2024.html">6 Feb 2024</a></li>
<li><a href="/mittelmann-plots/minlp-17-Jan-2024.html">17 Jan 2024</a></li>
<li><a href="/mittelmann-plots/minlp-21-Oct-2023.html">21 Oct 2023</a></li>
<li><a href="/mittelmann-plots/minlp-10-Jul-2023.html">10 Jul 2023</a></li>
<li><a href="/mittelmann-plots/minlp-20-Apr-2023.html">20 Apr 2023</a></li>
<li><a href="/mittelmann-plots/minlp-5-Feb-2023.html">5 Feb 2023</a></li>
<li><a href="/mittelmann-plots/minlp-29-Jan-2023.html">29 Jan 2023</a></li>
<li><a href="/mittelmann-plots/minlp-24-Jan-2023.html">24 Jan 2023</a></li>
<li><a href="/mittelmann-plots/minlp-27-Oct-2022.html">27 Oct 2022</a></li>
<li><a href="/mittelmann-plots/minlp-26-Oct-2022.html">26 Oct 2022</a></li>
<li><a href="/mittelmann-plots/minlp-20-Sep-2022.html">20 Sep 2022</a></li>
<li><a href="/mittelmann-plots/minlp-4-Sep-2022.html">4 Sep 2022</a></li>
<li><a href="/mittelmann-plots/minlp-10-Aug-2022.html">10 Aug 2022</a></li>
<li><a href="/mittelmann-plots/minlp-23-Jul-2022.html">23 Jul 2022</a></li>
</ul></details>

---


## [MPEC Benchmark (Math. Progr. w. Equilibrium Constraints) (9 Feb 2024)](http://plato.asu.edu/ftp/mpec.html)
Choose base solver for comparison:

| solver | score (as reported) | solved of 29|
| :--- | ---:  | ---:   |
|[⭐ virtual best](mpec-vbest.html) | 1.00  | 93%|
|[🥇 KNITRO-14.0](mpec-KNITRO.html) | 1.00 (1.00) | 93%|
|[🥈 filter-MPEC](mpec-filter.html) | 16.90 (16.90) | 62%|
|[🥉 LOQO-7.03](mpec-LOQO.html) | 37.10 (37.10) | 21%|


<details><summary>previous benchmarks 🔽</summary>
<br>

<ul>
<li><a href="/mittelmann-plots/mpec-2-Feb-2024.html">2 Feb 2024</a></li>
<li><a href="/mittelmann-plots/mpec-12-Apr-2022.html">12 Apr 2022</a></li>
</ul></details>

---

