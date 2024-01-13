Interactive charts comparing the results of [Hans Mittelmann's benchmarks](http://plato.asu.edu/bench.html).
Each solver can be selected to show pairwise running time factors for every other solver in the respective benchmark.
These plots should make browsing the results easier.
The score ([scaled shifted geometric mean](http://plato.asu.edu/ftp/shgeom.html)) is recomputed using the reported solving times.
We also calculate a "virtual best" or "ensemble" solver that picks the best performance over all solvers for every single problem
instance. This might reveal how much potential the individual solvers still have.
[Please let me know](https://github.com/mattmilten/mittelmann-plots/issues/new) if you have a question or if there is an error.

    
## [LPfeas Benchmark (find PD feasible point) (12 Jan 2024)](http://plato.asu.edu/ftp/lpfeas.html)
Choose base solver for comparison:

| solver | score (as reported) | solved of 65|
| :--- | ---:  | ---:   |
|[⭐ virtual best](lpfeas-vbest.html) | 0.72  | 100%|
|[🥇 COPT-7.0.0](lpfeas-COPT.html) | 1.00 (1.00) | 100%|
|[🥈 Gurobi-11.0.0](lpfeas-Gurobi.html) | 1.28 (1.28) | 97%|
|[🥉 MindOpt-1.0.0](lpfeas-MDOPT.html) | 1.80 (1.80) | 97%|
|[📊 MOSEK-10.1.9](lpfeas-MOSEK.html) | 2.60 (2.60) | 98%|
|[📊 XOPT-0.0.3](lpfeas-XOPT.html) | 6.22 (6.22) | 89%|
|[📊 ORTOOLS-9.7](lpfeas-PDLP%.html) | 16.97 (17.00) | 75%|
|[📊 HiGHS-1.6.0](lpfeas-HiGHS.html) | 19.21 (19.20) | 80%|
|[📊 KNITRO-13.0.0](lpfeas-KNITRO.html) | 22.89 (22.90) | 66%|
|[📊 MATLAB-R2023a](lpfeas-MATL.html) | 26.88 (26.90) | 77%|
|[📊 Tulip-0.9.4](lpfeas-TULIP.html) | 66.41 (66.40) | 55%|


<details><summary>previous benchmarks 🔽</summary>
<br>

<ul>
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


## [LPopt Benchmark (find optimal basic solution) (13 Dec 2023)](http://plato.asu.edu/ftp/lpopt.html)
Choose base solver for comparison:

| solver | score (as reported) | solved of 65|
| :--- | ---:  | ---:   |
|[⭐ virtual best](lpopt-vbest.html) | 0.79  | 100%|
|[🥇 COPT-7.0.0](lpopt-COPT.html) | 1.00 (1.00) | 100%|
|[🥈 Gurobi-11.0.0](lpopt-Gurob.html) | 1.58 (1.58) | 97%|
|[🥉 Optverse-0.7.1](lpopt-OPTV.html) | 1.66 (1.66) | 98%|
|[📊 MindOpt-1.0.0](lpopt-MDOPT.html) | 1.89 (1.89) | 97%|
|[📊 MOSEK-10.1.9](lpopt-MOSEK.html) | 5.61 (5.61) | 80%|
|[📊 HiGHS-1.6.0](lpopt-HiGHS.html) | 17.44 (17.40) | 78%|
|[📊 CLP-1.17.7](lpopt-CLP.html) | 26.12 (26.10) | 62%|
|[📊 MATLAB-R2022b](lpopt-MATL.html) | 39.83 (39.80) | 65%|
|[📊 Google-GLOP](lpopt-GLOP.html) | 56.96 (57.00) | 51%|
|[📊 SOPLEX-6.0.0](lpopt-SPLX.html) | 87.19 (87.20) | 49%|


<details><summary>previous benchmarks 🔽</summary>
<br>

<ul>
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


## [Large Network-LP Benchmark (commercial vs free) (4 Dec 2023)](http://plato.asu.edu/ftp/network.html)
Choose base solver for comparison:

| solver | score (as reported) | solved of 25|
| :--- | ---:  | ---:   |
|[⭐ virtual best](network-vbest.html) | 0.87  | 100%|
|[🥇 OptVerse-0.7.0](network-OPTV.html) | 1.00 (1.00) | 100%|
|[🥈 MindOpt-1.0.0](network-MDOPT.html) | 1.18 (1.18) | 100%|
|[🥉 Gurobi-11.0.0](network-GUR.html) | 1.69 (1.69) | 100%|
|[📊 COPT-7.0.0](network-COPT.html) | 2.14 (2.14) | 100%|
|[📊 Clp-1.17.7](network-CLP.html) | 6.07 (6.07) | 100%|
|[📊 HiGHS-1.6.0](network-HGHS.html) | 12.65 (12.60) | 80%|
|[📊 MATLAB-R2022b](network-MATL.html) | 21.28 (21.30) | 80%|
|[📊 MOSEK-10.1.9](network-MOSEK.html) | 26.86 (26.90) | 88%|
|[📊 QSopt-1.01](network-QSOPT.html) | 35.49 (35.50) | 68%|
|[📊 SOPLEX-6.0.0](network-SPLX.html) | 67.48 (67.40) | 64%|


<details><summary>previous benchmarks 🔽</summary>
<br>

<ul>
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


## [The MIPLIB2017 Benchmark Instances - 8 threads (7 Dec 2023)](http://plato.asu.edu/ftp/milp.html)
Choose base solver for comparison:

| solver | score (as reported) | solved of 240|
| :--- | ---:  | ---:   |
|[⭐ virtual best](milp_8threads-vbest.html) | 0.67  | 98%|
|[🥇 Gurobi-11.0.0](milp_8threads-Gurobi.html) | 1.00 (1.00) | 95%|
|[🥈 COPT-7.0.0](milp_8threads-COPT.html) | 1.74 (1.74) | 88%|
|[🥉 OptVerse-0.7.0](milp_8threads-optverse.html) | 2.88 (2.88) | 84%|
|[📊 MindOpt-1.0.0](milp_8threads-MindOpt.html) | 4.18 (4.18) | 82%|
|[📊 HiGHS-1.6.0](milp_8threads-HiGHS.html) | 9.98 (9.98) | 66%|
|[📊 SCIPC/spx-8.0.0](milp_8threads-SCIPC.html) | 10.08 (10.10) | 63%|
|[📊 SCIP/spx-8.0.0](milp_8threads-SCIP.html) | 12.32 (12.30) | 57%|
|[📊 CBC-2.10.5](milp_8threads-CBC.html) | 18.42 (18.40) | 45%|
|[📊 MATLAB-2023a](milp_8threads-Matlab.html) | 37.65 (37.60) | 30%|


<details><summary>previous benchmarks 🔽</summary>
<br>

<ul>
<li><a href="/mittelmann-plots/milp_8threads-18-Dec-2023.html">18 Dec 2023</a></li>
<li><a href="/mittelmann-plots/milp_8threads-17-Dec-2023.html">17 Dec 2023</a></li>
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


## [MILP cases that are slightly pathological (8 Dec 2023)](http://plato.asu.edu/ftp/path.html)
Choose base solver for comparison:

| solver | score (as reported) | solved of 45|
| :--- | ---:  | ---:   |
|[⭐ virtual best](path-vbest.html) | 0.65  | 100%|
|[🥇 GUROBI-11.0.0](path-Gurobi.html) | 1.00 (1.00) | 96%|
|[🥈 COPT-7.0.0](path-COPT.html) | 2.91 (2.91) | 91%|
|[🥉 OptVerse-0.7.0](path-optverse.html) | 3.89 (3.89) | 80%|
|[📊 MindOpt-1.0.0](path-MindOpt.html) | 16.84 (16.80) | 44%|
|[📊 HiGHS-1.6.0](path-HiGHS.html) | 19.42 (19.40) | 53%|
|[📊 SCIPC-8.0.0](path-SCIPC.html) | 22.50 (22.50) | 51%|
|[📊 SCIP-8.0.0](path-SCIP.html) | 28.83 (28.80) | 42%|
|[📊 CBC-2.10.7](path-CBC.html) | 45.02 (45.00) | 11%|
|[📊 GLPK-5.0](path-GLPK.html) | 45.63 (45.60) | 13%|
|[📊 MATLAB-2023a](path-MATLAB.html) | 60.86 (60.90) | 4%|


<details><summary>previous benchmarks 🔽</summary>
<br>

<ul>
<li><a href="/mittelmann-plots/path-17-Dec-2023.html">17 Dec 2023</a></li>
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


## [Infeasibility Detection for MILP Problems (6 Dec 2023)](http://plato.asu.edu/ftp/infeas.html)
Choose base solver for comparison:

| solver | score (as reported) | solved of 32|
| :--- | ---:  | ---:   |
|[⭐ virtual best](infeas-vbest.html) | 0.98  | 94%|
|[🥇 GUROBI-11.0.0](infeas-Gurobi.html) | 1.00 (1.00) | 94%|
|[🥈 COPT-7.0.0](infeas-COPT.html) | 1.47 (1.47) | 94%|
|[🥉 OptVerse-0.7.0](infeas-optverse.html) | 3.00 (3.00) | 88%|
|[📊 SCIPC-8.0.0](infeas-SCIPC.html) | 7.19 (8.18) | 81%|
|[📊 MindOpt-1.0.0](infeas-MindOpt.html) | 7.81 (7.19) | 84%|
|[📊 HiGHS-1.6.0](infeas-HiGHS.html) | 8.18 (7.81) | 81%|
|[📊 SCIP-8.0.0](infeas-SCIP.html) | 9.22 (9.22) | 78%|
|[📊 CBC-2.10.5](infeas-CBC.html) | 22.51 (22.50) | 62%|
|[📊 MATLAB-2023a](infeas-MATLAB.html) | 44.55 (44.50) | 50%|


<details><summary>previous benchmarks 🔽</summary>
<br>

<ul>
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


## [Several SDP-codes on sparse and other SDP problems (28 Sep 2023)](http://plato.asu.edu/ftp/sparse_sdp.html)
Choose base solver for comparison:

| solver | score (as reported) | solved of 76|
| :--- | ---:  | ---:   |
|[⭐ virtual best](sparse_sdp-vbest.html) | 0.62  | 99%|
|[🥇 COPT-7.0.0](sparse_sdp-COPT.html) | 1.00 (1.00) | 99%|
|[🥈 MindOpt-1.0.0](sparse_sdp-MDOPT.html) | 1.43 (1.44) | 99%|
|[🥉 MOSEK-10.1.9](sparse_sdp-MOSEK.html) | 3.13 (3.22) | 96%|
|[📊 SDPT3-4.0](sparse_sdp-SDPT3.html) | 4.95 (5.14) | 91%|
|[📊 CSDP-6.2.0](sparse_sdp-CSDP.html) | 5.02 (5.21) | 92%|
|[📊 HDSDP-1.0.0](sparse_sdp-HDSDP.html) | 7.52 (7.86) | 92%|
|[📊 SDPA-7.4.2](sparse_sdp-SDPA.html) | 9.96 (10.50) | 80%|
|[📊 SeDuMi-1.3.5](sparse_sdp-SeDuMi.html) | 27.14 (28.90) | 82%|


<details><summary>previous benchmarks 🔽</summary>
<br>

<ul>
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


## [Large Second Order Cone Benchmark (30 Nov 2023)](http://plato.asu.edu/ftp/socp.html)
Choose base solver for comparison:

| solver | score (as reported) | solved of 18|
| :--- | ---:  | ---:   |
|[⭐ virtual best](socp-vbest.html) | 0.81  | 100%|
|[🥇 COPT-7.0.0](socp-COPT.html) | 1.00 (1.00) | 100%|
|[🥈 MOSEK-10.1.9](socp-MOSEK.html) | 1.08 (1.08) | 100%|
|[🥉 Gurobi-11.0.0](socp-Gurobi.html) | 1.14 (1.14) | 100%|
|[📊 KNITRO-13.2.0](socp-KNITRO.html) | 13.41 (13.40) | 83%|
|[📊 ECOS-2.0.4](socp-ECOS.html) | 99.20 (99.20) | 61%|


<details><summary>previous benchmarks 🔽</summary>
<br>

<ul>
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


## [Mixed-integer SOCP Benchmark (30 Nov 2023)](http://plato.asu.edu/ftp/misocp.html)
Choose base solver for comparison:

| solver | score (as reported) | solved of 47|
| :--- | ---:  | ---:   |
|[⭐ virtual best](misocp-vbest.html) | 0.97  | 100%|
|[🥇 Gurobi-11.0.0](misocp-GUROBI.html) | 1.00 (1.00) | 100%|
|[🥈 COPT-7.0.0](misocp-COPT.html) | 2.34 (2.34) | 100%|
|[🥉 MOSEK-10.1.9](misocp-MOSEK.html) | 10.68 (10.70) | 77%|
|[📊 SCIP-8.0.0](misocp-SCIP.html) | 26.68 (26.70) | 66%|


<details><summary>previous benchmarks 🔽</summary>
<br>

<ul>
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


## [Binary Non-Convex QPLIB Benchmark (11 Jan 2024)](http://plato.asu.edu/ftp/qplib.html)
Choose base solver for comparison:

| solver | score (as reported) | solved of 97|
| :--- | ---:  | ---:   |
|[⭐ virtual best](qplib-vbest.html) | 0.70  | 100%|
|[🥇 Gurobi-11.0.0](qplib-GUROBI.html) | 1.00 (1.00) | 97%|
|[🥈 SHOT-1.1](qplib-SHOT.html) | 1.48 (1.48) | 88%|
|[🥉 OCTERACT-4.7.1](qplib-OCTERACT.html) | 1.69 (1.69) | 96%|
|[📊 Baron-23.6.22](qplib-BARON.html) | 11.61 (11.60) | 60%|
|[📊 SCIP-8.1.0](qplib-SCIP.html) | 38.80 (38.80) | 37%|
|[📊 ANTIGONE-1.1](qplib-ANTIGONE.html) | 81.19 (81.20) | 16%|
|[📊 COUENNE-0.5](qplib-COUENNE.html) | 96.45 (96.40) | 6%|


<details><summary>previous benchmarks 🔽</summary>
<br>

<ul>
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


## [Nonconvex QUBO-QPLIB Benchmark (10 Jan 2024)](http://plato.asu.edu/ftp/qubo.html)
Choose base solver for comparison:

| solver | score (as reported) | solved of 23|
| :--- | ---:  | ---:   |
|[⭐ virtual best](qubo-vbest.html) | 0.87  | 70%|
|[🥇 QuBowl](qubo-QUBOWL.html) | 1.00 (1.00) | 65%|
|[🥈 Gurobi-11.0.0](qubo-GUROBI.html) | 1.30 (1.30) | 57%|
|[🥉 OCTERACT-4.7.1](qubo-OCTERACT.html) | 1.74 (1.74) | 52%|
|[📊 Baron-23.6.22](qubo-BARON.html) | 1.79 (1.79) | 52%|
|[📊 SHOT-1.1](qubo-SHOT.html) | 1.99 (1.99) | 48%|
|[📊 McSparse-2.0](qubo-MCSPARSE.html) | 2.36 (2.36) | 52%|
|[📊 Biqbin](qubo-BIQBIN.html) | 5.40 (5.40) | 39%|
|[📊 SCIP-8.1](qubo-SCIP.html) | 5.46 (5.46) | 35%|


<details><summary>previous benchmarks 🔽</summary>
<br>

<ul>
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


## [Discrete Non-Convex QPLIB Benchmark (non-binary) (6 Dec 2023)](http://plato.asu.edu/ftp/nonbinary.html)
Choose base solver for comparison:

| solver | score (as reported) | solved of 108|
| :--- | ---:  | ---:   |
|[⭐ virtual best](nonbinary-vbest.html) | 0.36  | 98%|
|[🥇 Gurobi-11.0.0](nonbinary-GUROBI.html) | 1.00 (1.00) | 86%|
|[🥈 SHOT-1.1](nonbinary-SHOT.html) | 2.48 (2.48) | 75%|
|[🥉 OCTERACT-4.7.1](nonbinary-OCTERACT.html) | 6.31 (6.31) | 73%|
|[📊 Baron-23.6.22](nonbinary-BARON.html) | 13.58 (13.60) | 52%|
|[📊 SCIP-8.0.0](nonbinary-SCIP.html) | 33.24 (33.20) | 34%|
|[📊 ANTIGONE-1.1](nonbinary-ANTIGONE.html) | 53.92 (53.90) | 27%|
|[📊 MINOTAUR-0.3.0](nonbinary-MINOTAUR.html) | 64.13 (64.10) | 14%|


<details><summary>previous benchmarks 🔽</summary>
<br>

<ul>
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


## [Continuous Non-Convex QPLIB Benchmark (5 Dec 2023)](http://plato.asu.edu/ftp/cnconv.html)
Choose base solver for comparison:

| solver | score (as reported) | solved of 67|
| :--- | ---:  | ---:   |
|[⭐ virtual best](cnconv-vbest.html) | 0.23  | 94%|
|[🥇 GUROBI-11.0.0](cnconv-GUROBI.html) | 1.00 (1.00) | 66%|
|[🥈 OCTERACT-4.7.1](cnconv-OCTERACT.html) | 1.55 (1.55) | 69%|
|[🥉 Baron-23.6.22](cnconv-BARON.html) | 3.08 (3.08) | 51%|
|[📊 ANTIGONE-1.1](cnconv-ANTIGONE.html) | 5.73 (5.73) | 42%|
|[📊 MINOTAUR-0.3.0](cnconv-MINOTAUR.html) | 9.99 (9.99) | 19%|
|[📊 SCIP-8.0.0](cnconv-SCIP.html) | 11.63 (11.60) | 19%|
|[📊 COUENNE-0.5](cnconv-COUENNE.html) | 13.25 (13.30) | 12%|
|[📊 RAPOSa-4.0.2](cnconv-RAPOSA.html) | 16.78 (16.80) | 6%|


<details><summary>previous benchmarks 🔽</summary>
<br>

<ul>
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


## [Convex Continuous QPLIB Benchmark (ext) (9 Dec 2023)](http://plato.asu.edu/ftp/cconvex.html)
Choose base solver for comparison:

| solver | score (as reported) | solved of 42|
| :--- | ---:  | ---:   |
|[⭐ virtual best](cconvex-vbest.html) | 0.55  | 100%|
|[🥇 OptVerse-0.7.0](cconvex-OPTVERS.html) | 1.00 (1.00) | 98%|
|[🥈 COPT-7.0.1](cconvex-COPT.html) | 1.18 (1.18) | 95%|
|[🥉 KNITRO-13.2.0](cconvex-KNITRO.html) | 1.19 (1.19) | 95%|
|[📊 Gurobi-11.0.0](cconvex-Gurobi.html) | 1.24 (1.24) | 98%|
|[📊 MOSEK-10.1.21](cconvex-MOSEK.html) | 1.24 (1.24) | 98%|
|[📊 MindOpt-1.0.0](cconvex-MINDOPT.html) | 4.48 (4.23) | 81%|
|[📊 IPOPT-3.14.5](cconvex-IPOPT.html) | 6.98 (6.98) | 83%|


<details><summary>previous benchmarks 🔽</summary>
<br>

<ul>
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


## [Convex Discrete QPLIB Benchmark (10 Jan 2024)](http://plato.asu.edu/ftp/convex.html)
Choose base solver for comparison:

| solver | score (as reported) | solved of 31|
| :--- | ---:  | ---:   |
|[⭐ virtual best](convex-vbest.html) | 0.68  | 87%|
|[🥇 GUROBI-11.0.0](convex-GUROBI.html) | 1.00 (1.00) | 81%|
|[🥈 COPT-7.0.0](convex-COPT.html) | 1.00 (1.00) | 77%|
|[🥉 Shot-1.1](convex-SHOT.html) | 1.18 (1.18) | 81%|
|[📊 OCTERACT-4.7.1](convex-OCTACT.html) | 2.44 (2.44) | 77%|
|[📊 Baron-23.6.22](convex-BARON.html) | 7.31 (7.30) | 61%|
|[📊 MOSEK-10.1.9](convex-MOSEK.html) | 10.04 (10.00) | 58%|
|[📊 KNITRO-13.1.0](convex-KNITRO.html) | 13.39 (13.40) | 52%|
|[📊 SCIP-8.1.0](convex-SCIP.html) | 26.71 (26.70) | 42%|
|[📊 MNTAUR](convex-MNTAUR.html) | 42.32 (42.30) | 45%|
|[📊 Bonmin-1.8.7](convex-BONMIN.html) | 54.64 (54.60) | 23%|


<details><summary>previous benchmarks 🔽</summary>
<br>

<ul>
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


## [Mixed Integer Nonlinear Programming Benchmark (MINLPLIB) (21 Oct 2023)](http://plato.asu.edu/ftp/minlp.html)
Choose base solver for comparison:

| solver | score (as reported) | solved of 87|
| :--- | ---:  | ---:   |
|[⭐ virtual best](minlp-vbest.html) | 0.43  | 100%|
|[🥇 OCTERACT](minlp-OCTERACT.html) | 1.00 (1.00) | 100%|
|[🥈 BARON](minlp-BARON.html) | 2.34 (2.30) | 89%|
|[🥉 SHOT](minlp-SHOT.html) | 7.17 (7.20) | 60%|
|[📊 SCIP](minlp-SCIP.html) | 10.34 (10.30) | 74%|
|[📊 LINDO](minlp-LINDO.html) | 32.85 (32.80) | 48%|
|[📊 ANTIGONE](minlp-ANTIGONE.html) | 39.32 (39.30) | 61%|
|[📊 COUENNE](minlp-COUENNE.html) | 89.78 (89.80) | 28%|


<details><summary>previous benchmarks 🔽</summary>
<br>

<ul>
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


## [MPEC Benchmark (Math. Progr. w. Equilibrium Constraints) (12 Apr 2022)](http://plato.asu.edu/ftp/mpec.html)
Choose base solver for comparison:

| solver | score (as reported) | solved of 29|
| :--- | ---:  | ---:   |
|[⭐ virtual best](mpec-vbest.html) | 1.00  | 83%|
|[🥇 KNITRO-13.0](mpec-KNITRO.html) | 1.00 (1.00) | 83%|
|[🥈 filter-MPEC](mpec-filter.html) | 7.82 (8.90) | 62%|
|[🥉 LOQO-7.03](mpec-LOQO.html) | 16.69 (19.50) | 21%|

---

