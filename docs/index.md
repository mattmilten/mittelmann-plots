Interactive charts comparing the results of [Hans Mittelmann's benchmarks](http://plato.asu.edu/bench.html).
Each solver can be selected to show pairwise running time factors for every other solver in the respective benchmark.
These plots should make browsing the results easier.
The score ([scaled shifted geometric mean](http://plato.asu.edu/ftp/shgeom.html)) is recomputed using the reported solving times.
We also calculate a "virtual best" or "ensemble" solver that picks the best performance over all solvers for every single problem
instance. This might reveal how much potential the individual solvers still have.
[Please let me know](https://github.com/mattmilten/mittelmann-plots/issues/new) if you have a question or if there is an error.

    
## [LPfeas Benchmark (find PD feasible point) (11 Sep 2024)](http://plato.asu.edu/ftp/lpfeas.html)
Choose base solver for comparison:

| solver | score (as reported) | solved of 65|
| :--- | ---:  | ---:   |
|[⭐ virtual best](lpfeas-vbest.html) | 0.76  | 100%|
|[🥇 COPT 7.1.0](lpfeas-COPT.html) | 1.00 (1.00) | 100%|
|[🥈 Optverse 1.0.0](lpfeas-OPTV.html) | 1.45 (1.45) | 100%|
|[🥉 MindOpt 1.0.0](lpfeas-MDOPT.html) | 1.81 (1.81) | 97%|
|[📊 MOSEK 10.1.9](lpfeas-MOSEK.html) | 2.62 (2.62) | 98%|
|[📊 XOPT 0.0.6](lpfeas-XOPT.html) | 5.41 (5.41) | 91%|
|[📊 ORTOOLS 9.10](lpfeas-PDLP%.html) | 15.66 (15.70) | 77%|
|[📊 HiGHS 1.6.0](lpfeas-HiGHS.html) | 19.35 (19.30) | 80%|
|[📊 KNITRO 14.1.0](lpfeas-KNITRO.html) | 21.52 (21.50) | 74%|
|[📊 MATLAB R2023a](lpfeas-MATL.html) | 27.07 (27.10) | 77%|
|[📊 Tulip 0.9.4](lpfeas-TULIP.html) | 66.89 (66.90) | 55%|


<details><summary>previous benchmarks 🔽</summary>
<br>

<ul>
<li><a href="/mittelmann-plots/lpfeas-21-Aug-2024.html">21 Aug 2024</a></li>
<li><a href="/mittelmann-plots/lpfeas-6-Aug-2024.html">6 Aug 2024</a></li>
<li><a href="/mittelmann-plots/lpfeas-25-Jul-2024.html">25 Jul 2024</a></li>
<li><a href="/mittelmann-plots/lpfeas-9-Jun-2024.html">9 Jun 2024</a></li>
<li><a href="/mittelmann-plots/lpfeas-22-May-2024.html">22 May 2024</a></li>
<li><a href="/mittelmann-plots/lpfeas-20-May-2024.html">20 May 2024</a></li>
<li><a href="/mittelmann-plots/lpfeas-28-Mar-2024.html">28 Mar 2024</a></li>
<li><a href="/mittelmann-plots/lpfeas-8-Feb-2024.html">8 Feb 2024</a></li>
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


## [LPopt Benchmark (find optimal basic solution) (11 Sep 2024)](http://plato.asu.edu/ftp/lpopt.html)
Choose base solver for comparison:

| solver | score (as reported) | solved of 65|
| :--- | ---:  | ---:   |
|[⭐ virtual best](lpopt-vbest.html) | 0.85  | 100%|
|[🥇 COPT 7.1.0](lpopt-COPT.html) | 1.00 (1.00) | 100%|
|[🥈 Optverse 1.0.0](lpopt-OPTV.html) | 1.61 (1.61) | 97%|
|[🥉 MindOpt 1.0.0](lpopt-MDOPT.html) | 1.89 (1.89) | 97%|
|[📊 MOSEK 10.1.9](lpopt-MOSEK.html) | 5.61 (5.61) | 80%|
|[📊 XOPT 0.0.6](lpopt-XOPT.html) | 6.33 (6.33) | 80%|
|[📊 HiGHS 1.6.0](lpopt-HiGHS.html) | 17.44 (17.40) | 78%|
|[📊 CLP 1.17.7](lpopt-CLP.html) | 26.13 (26.10) | 62%|
|[📊 Google-GLOP](lpopt-GLOP.html) | 56.97 (57.00) | 51%|
|[📊 SOPLEX 6.0.0](lpopt-SPLX.html) | 87.20 (87.20) | 49%|


<details><summary>previous benchmarks 🔽</summary>
<br>

<ul>
<li><a href="/mittelmann-plots/lpopt-21-Aug-2024.html">21 Aug 2024</a></li>
<li><a href="/mittelmann-plots/lpopt-30-Jul-2024.html">30 Jul 2024</a></li>
<li><a href="/mittelmann-plots/lpopt-25-Jul-2024.html">25 Jul 2024</a></li>
<li><a href="/mittelmann-plots/lpopt-20-May-2024.html">20 May 2024</a></li>
<li><a href="/mittelmann-plots/lpopt-18-Apr-2024.html">18 Apr 2024</a></li>
<li><a href="/mittelmann-plots/lpopt-13-Apr-2024.html">13 Apr 2024</a></li>
<li><a href="/mittelmann-plots/lpopt-27-Mar-2024.html">27 Mar 2024</a></li>
<li><a href="/mittelmann-plots/lpopt-8-Feb-2024.html">8 Feb 2024</a></li>
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


## [Large Network-LP Benchmark (commercial vs free) (11 Sep 2024)](http://plato.asu.edu/ftp/network.html)
Choose base solver for comparison:

| solver | score (as reported) | solved of 25|
| :--- | ---:  | ---:   |
|[⭐ virtual best](network-vbest.html) | 0.86  | 100%|
|[🥇 OptVerse 1.0.0](network-OPTV.html) | 1.00 (1.00) | 100%|
|[🥈 MDPT](network-MDPT.html) | 1.16 (1.16) | 100%|
|[🥉 COPT 7.1.0](network-COPT.html) | 2.12 (2.12) | 100%|
|[📊 Clp 1.17.7](network-CLP.html) | 5.97 (5.97) | 100%|
|[📊 HiGHS 1.7.0](network-HGHS.html) | 12.71 (12.70) | 80%|
|[📊 MOSEK 10.1.9](network-MOSEK.html) | 26.41 (26.40) | 88%|
|[📊 QSopt 1.01](network-QSOPT.html) | 34.89 (34.90) | 68%|
|[📊 SOPLEX 6.0.0](network-SPLX.html) | 66.34 (66.30) | 64%|


<details><summary>previous benchmarks 🔽</summary>
<br>

<ul>
<li><a href="/mittelmann-plots/network-21-Aug-2024.html">21 Aug 2024</a></li>
<li><a href="/mittelmann-plots/network-18-Apr-2024.html">18 Apr 2024</a></li>
<li><a href="/mittelmann-plots/network-13-Apr-2024.html">13 Apr 2024</a></li>
<li><a href="/mittelmann-plots/network-31-Mar-2024.html">31 Mar 2024</a></li>
<li><a href="/mittelmann-plots/network-6-Feb-2024.html">6 Feb 2024</a></li>
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


## [The MIPLIB2017 Benchmark Instances - 8 threads (13 Sep 2024)](http://plato.asu.edu/ftp/milp.html)
Choose base solver for comparison:

| solver | score (as reported) | solved of 240|
| :--- | ---:  | ---:   |
|[⭐ virtual best](milp_8threads-vbest.html) | 0.59  | 96%|
|[🥇 optverse](milp_8threads-optverse.html) | 1.00 (1.00) | 92%|
|[🥈 COPT](milp_8threads-COPT.html) | 1.05 (1.04) | 92%|
|[🥉 LEOPT](milp_8threads-LEOPT.html) | 3.04 (3.04) | 75%|
|[📊 MindOpt](milp_8threads-MindOpt.html) | 3.04 (3.04) | 82%|
|[📊 XOPT](milp_8threads-XOPT.html) | 4.62 (4.62) | 78%|
|[📊 HiGHS](milp_8threads-HiGHS.html) | 7.27 (7.27) | 66%|
|[📊 SCIPC](milp_8threads-SCIPC.html) | 7.71 (7.71) | 63%|
|[📊 SCIP](milp_8threads-SCIP.html) | 9.03 (9.03) | 58%|
|[📊 CBC](milp_8threads-CBC.html) | 13.42 (13.40) | 45%|


<details><summary>previous benchmarks 🔽</summary>
<br>

<ul>
<li><a href="/mittelmann-plots/milp_8threads-20-Aug-2024.html">20 Aug 2024</a></li>
<li><a href="/mittelmann-plots/milp_8threads-16-Aug-2024.html">16 Aug 2024</a></li>
<li><a href="/mittelmann-plots/milp_8threads-12-Aug-2024.html">12 Aug 2024</a></li>
<li><a href="/mittelmann-plots/milp_8threads-9-Aug-2024.html">9 Aug 2024</a></li>
<li><a href="/mittelmann-plots/milp_8threads-14-Jul-2024.html">14 Jul 2024</a></li>
<li><a href="/mittelmann-plots/milp_8threads-5-Jul-2024.html">5 Jul 2024</a></li>
<li><a href="/mittelmann-plots/milp_8threads-7-May-2024.html">7 May 2024</a></li>
<li><a href="/mittelmann-plots/milp_8threads-17-Apr-2024.html">17 Apr 2024</a></li>
<li><a href="/mittelmann-plots/milp_8threads-5-Apr-2024.html">5 Apr 2024</a></li>
<li><a href="/mittelmann-plots/milp_8threads-27-Mar-2024.html">27 Mar 2024</a></li>
<li><a href="/mittelmann-plots/milp_8threads-4-Mar-2024.html">4 Mar 2024</a></li>
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


## [MILP cases that are slightly pathological (11 Sep 2024)](http://plato.asu.edu/ftp/path.html)
Choose base solver for comparison:

| solver | score (as reported) | solved of 45|
| :--- | ---:  | ---:   |
|[⭐ virtual best](path-vbest.html) | 0.58  | 100%|
|[🥇 OptVerse 1.0.0](path-optverse.html) | 1.00 (1.00) | 91%|
|[🥈 COPT 7.1.0](path-COPT.html) | 1.11 (1.11) | 91%|
|[🥉 XOPT 0.0.6](path-XOPT.html) | 7.88 (7.90) | 69%|
|[📊 MindOpt 1.0.0](path-MindOpt.html) | 10.44 (10.40) | 53%|
|[📊 HiGHS 1.7.0](path-HiGHS.html) | 11.79 (11.80) | 64%|
|[📊 LEOPT 0.5.1](path-LEOPT.html) | 12.45 (12.40) | 60%|
|[📊 SCIPC](path-SCIPC.html) | 12.99 (13.00) | 62%|
|[📊 SCIP 9.0.0](path-SCIP.html) | 22.40 (22.40) | 44%|
|[📊 CBC 2.10.7](path-CBC.html) | 39.28 (39.30) | 22%|
|[📊 GLPK 5.0](path-GLPK.html) | 41.63 (41.60) | 13%|


<details><summary>previous benchmarks 🔽</summary>
<br>

<ul>
<li><a href="/mittelmann-plots/path-20-Aug-2024.html">20 Aug 2024</a></li>
<li><a href="/mittelmann-plots/path-17-Jul-2024.html">17 Jul 2024</a></li>
<li><a href="/mittelmann-plots/path-7-Jul-2024.html">7 Jul 2024</a></li>
<li><a href="/mittelmann-plots/path-13-May-2024.html">13 May 2024</a></li>
<li><a href="/mittelmann-plots/path-11-May-2024.html">11 May 2024</a></li>
<li><a href="/mittelmann-plots/path-5-Apr-2024.html">5 Apr 2024</a></li>
<li><a href="/mittelmann-plots/path-7-Mar-2024.html">7 Mar 2024</a></li>
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


## [Infeasibility Detection for MILP Problems (11 Sep 2024)](http://plato.asu.edu/ftp/infeas.html)
Choose base solver for comparison:

| solver | score (as reported) | solved of 32|
| :--- | ---:  | ---:   |
|[⭐ virtual best](infeas-vbest.html) | 0.91  | 94%|
|[🥇 COPT 7.1.0](infeas-COPT.html) | 1.00 (1.00) | 94%|
|[🥈 OptVerse 1.0.0](infeas-optverse.html) | 1.23 (1.23) | 94%|
|[🥉 MindOpt 1.0.0](infeas-MindOpt.html) | 5.71 (5.71) | 84%|
|[📊 XOPT 0.0.6](infeas-XOPT.html) | 5.72 (5.72) | 78%|
|[📊 SCIPC](infeas-SCIPC.html) | 5.82 (5.82) | 78%|
|[📊 HiGHS 1.7.0](infeas-HiGHS.html) | 6.04 (6.04) | 78%|
|[📊 SCIP 9.0.0](infeas-SCIP.html) | 7.80 (7.80) | 81%|
|[📊 CBC 2.10.5](infeas-CBC.html) | 16.46 (16.50) | 62%|


<details><summary>previous benchmarks 🔽</summary>
<br>

<ul>
<li><a href="/mittelmann-plots/infeas-20-Aug-2024.html">20 Aug 2024</a></li>
<li><a href="/mittelmann-plots/infeas-5-Apr-2024.html">5 Apr 2024</a></li>
<li><a href="/mittelmann-plots/infeas-31-Mar-2024.html">31 Mar 2024</a></li>
<li><a href="/mittelmann-plots/infeas-29-Feb-2024.html">29 Feb 2024</a></li>
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


## [Several SDP-codes on sparse and other SDP problems (28 Aug 2024)](http://plato.asu.edu/ftp/sparse_sdp.html)
Choose base solver for comparison:

| solver | score (as reported) | solved of 75|
| :--- | ---:  | ---:   |
|[⭐ virtual best](sparse_sdp-vbest.html) | 0.58  | 100%|
|[🥇 COPT 7.1.0](sparse_sdp-COPT.html) | 1.00 (1.00) | 100%|
|[🥈 MindOpt 1.0.0](sparse_sdp-MDOPT.html) | 1.45 (1.45) | 100%|
|[🥉 MOSEK 10.2.3](sparse_sdp-MOSEK.html) | 2.85 (2.85) | 97%|
|[📊 SDPT3 4.0](sparse_sdp-SDPT3.html) | 5.18 (5.18) | 92%|
|[📊 CSDP 6.2.0](sparse_sdp-CSDP.html) | 5.25 (5.25) | 93%|
|[📊 HDSDP 1.0.0](sparse_sdp-HDSDP.html) | 7.91 (7.91) | 93%|
|[📊 SDPA 7.4.2](sparse_sdp-SDPA.html) | 10.52 (10.50) | 81%|
|[📊 SeDuMi 1.3.5](sparse_sdp-SeDuMi.html) | 29.06 (29.10) | 83%|


<details><summary>previous benchmarks 🔽</summary>
<br>

<ul>
<li><a href="/mittelmann-plots/sparse_sdp-8-Feb-2024.html">8 Feb 2024</a></li>
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


## [Large Second Order Cone Benchmark (11 Sep 2024)](http://plato.asu.edu/ftp/socp.html)
Choose base solver for comparison:

| solver | score (as reported) | solved of 18|
| :--- | ---:  | ---:   |
|[⭐ virtual best](socp-vbest.html) | 0.85  | 100%|
|[🥇 Optverse 1.0.0   OPTVERSE](socp-OPTVERSE.html) | 1.00 (1.00) | 100%|
|[🥈 COPT 7.1.0       COPT ](socp-COPT.html) | 1.09 (1.09) | 100%|
|[🥉 MOSEK 10.1.28    MOSEK ](socp-MOSEK.html) | 1.14 (1.14) | 100%|
|[📊 KNITRO 14.0.0    Knitro ](socp-KNITRO.html) | 10.12 (10.10) | 94%|
|[📊 ECOS 2.0.4       ECOS ](socp-ECOS.html) | 106.44 (106.00) | 61%|


<details><summary>previous benchmarks 🔽</summary>
<br>

<ul>
<li><a href="/mittelmann-plots/socp-21-Aug-2024.html">21 Aug 2024</a></li>
<li><a href="/mittelmann-plots/socp-8-Apr-2024.html">8 Apr 2024</a></li>
<li><a href="/mittelmann-plots/socp-7-Feb-2024.html">7 Feb 2024</a></li>
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


## [Mixed-integer SOCP Benchmark (21 Aug 2024)](http://plato.asu.edu/ftp/misocp.html)
Choose base solver for comparison:

| solver | score (as reported) | solved of 47|
| :--- | ---:  | ---:   |
|[⭐ virtual best](misocp-vbest.html) | 0.92  | 98%|
|[🥇 COPT 7.1.0](misocp-COPT.html) | 1.00 (1.00) | 98%|
|[🥈 MOSEK 10.1.28](misocp-MOSEK.html) | 4.94 (4.17) | 77%|
|[🥉 SCIP 9.0.0](misocp-SCIP.html) | 11.63 (9.31) | 66%|


<details><summary>previous benchmarks 🔽</summary>
<br>

<ul>
<li><a href="/mittelmann-plots/misocp-9-Apr-2024.html">9 Apr 2024</a></li>
<li><a href="/mittelmann-plots/misocp-9-Feb-2024.html">9 Feb 2024</a></li>
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


## [Binary Non-Convex QPLIB Benchmark (21 Aug 2024)](http://plato.asu.edu/ftp/qplib.html)
Choose base solver for comparison:

| solver | score (as reported) | solved of 97|
| :--- | ---:  | ---:   |
|[⭐ virtual best](qplib-vbest.html) | 0.65  | 98%|
|[🥇 SHOT 1.1](qplib-SHOT.html) | 1.00 (1.00) | 94%|
|[🥈 Baron 24.5.8](qplib-BARON.html) | 5.91 (5.91) | 66%|
|[🥉 RAPOSa 4.4.1](qplib-RAPOSa.html) | 10.26 (10.30) | 71%|
|[📊 SCIP 9.0.0](qplib-SCIP.html) | 31.66 (31.70) | 35%|
|[📊 ANTIGONE 1.1](qplib-ANTIGONE.html) | 63.08 (63.10) | 16%|
|[📊 COUENNE 0.5](qplib-COUENNE.html) | 74.93 (74.90) | 6%|


<details><summary>previous benchmarks 🔽</summary>
<br>

<ul>
<li><a href="/mittelmann-plots/qplib-28-Jun-2024.html">28 Jun 2024</a></li>
<li><a href="/mittelmann-plots/qplib-13-Jun-2024.html">13 Jun 2024</a></li>
<li><a href="/mittelmann-plots/qplib-15-May-2024.html">15 May 2024</a></li>
<li><a href="/mittelmann-plots/qplib-29-Apr-2024.html">29 Apr 2024</a></li>
<li><a href="/mittelmann-plots/qplib-11-Apr-2024.html">11 Apr 2024</a></li>
<li><a href="/mittelmann-plots/qplib-11-Feb-2024.html">11 Feb 2024</a></li>
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


## [Nonconvex QUBO-QPLIB Benchmark (21 Aug 2024)](http://plato.asu.edu/ftp/qubo.html)
Choose base solver for comparison:

| solver | score (as reported) | solved of 23|
| :--- | ---:  | ---:   |
|[⭐ virtual best](qubo-vbest.html) | 0.94  | 70%|
|[🥇 QuBowl](qubo-QUBOWL.html) | 1.00 (1.00) | 65%|
|[🥈 Baron 24.5.8](qubo-BARON.html) | 1.82 (1.82) | 52%|
|[🥉 SHOT 1.1](qubo-SHOT.html) | 1.92 (1.76) | 52%|
|[📊 McSparse 2.0](qubo-MCSPARSE.html) | 2.36 (2.36) | 52%|
|[📊 SCIP 9.0](qubo-SCIP.html) | 5.73 (5.73) | 30%|
|[📊 Biqbin](qubo-BIQBIN.html) | 7.63 (5.40) | 39%|


<details><summary>previous benchmarks 🔽</summary>
<br>

<ul>
<li><a href="/mittelmann-plots/qubo-9-Jun-2024.html">9 Jun 2024</a></li>
<li><a href="/mittelmann-plots/qubo-10-Apr-2024.html">10 Apr 2024</a></li>
<li><a href="/mittelmann-plots/qubo-10-Feb-2024.html">10 Feb 2024</a></li>
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


## [Discrete Non-Convex QPLIB Benchmark (non-binary) (21 Aug 2024)](http://plato.asu.edu/ftp/nonbinary.html)
Choose base solver for comparison:

| solver | score (as reported) | solved of 101|
| :--- | ---:  | ---:   |
|[⭐ virtual best](nonbinary-vbest.html) | 0.60  | 100%|
|[🥇 SHOT 1.1](nonbinary-SHOT.html) | 1.00 (1.00) | 94%|
|[🥈 Baron 24.5.8](nonbinary-BARON.html) | 5.19 (5.19) | 71%|
|[🥉 SCIP 9.0.0](nonbinary-SCIP.html) | 30.29 (30.30) | 41%|
|[📊 ANTIGONE 1.1](nonbinary-ANTIGONE.html) | 74.47 (74.50) | 28%|


<details><summary>previous benchmarks 🔽</summary>
<br>

<ul>
<li><a href="/mittelmann-plots/nonbinary-1-Jul-2024.html">1 Jul 2024</a></li>
<li><a href="/mittelmann-plots/nonbinary-7-Jun-2024.html">7 Jun 2024</a></li>
<li><a href="/mittelmann-plots/nonbinary-21-May-2024.html">21 May 2024</a></li>
<li><a href="/mittelmann-plots/nonbinary-22-Feb-2024.html">22 Feb 2024</a></li>
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


## [Continuous Non-Convex QPLIB Benchmark (21 Aug 2024)](http://plato.asu.edu/ftp/cnconv.html)
Choose base solver for comparison:

| solver | score (as reported) | solved of 50|
| :--- | ---:  | ---:   |
|[⭐ virtual best](cnconv-vbest.html) | 0.23  | 100%|
|[🥇 Baron 24.5.8](cnconv-BARON.html) | 1.00 (1.00) | 70%|
|[🥈 MINOTAUR 0.4.0](cnconv-MINOTAUR.html) | 3.58 (3.58) | 50%|
|[🥉 ANTIGONE 1.1](cnconv-ANTIGONE.html) | 3.92 (3.92) | 52%|
|[📊 SCIP 9.0.0](cnconv-SCIP.html) | 6.97 (6.97) | 30%|


<details><summary>previous benchmarks 🔽</summary>
<br>

<ul>
<li><a href="/mittelmann-plots/cnconv-6-Jul-2024.html">6 Jul 2024</a></li>
<li><a href="/mittelmann-plots/cnconv-20-Jun-2024.html">20 Jun 2024</a></li>
<li><a href="/mittelmann-plots/cnconv-9-Mar-2024.html">9 Mar 2024</a></li>
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


## [Convex Continuous QPLIB Benchmark (ext) (11 Sep 2024)](http://plato.asu.edu/ftp/cconvex.html)
Choose base solver for comparison:

| solver | score (as reported) | solved of 42|
| :--- | ---:  | ---:   |
|[⭐ virtual best](cconvex-vbest.html) | 0.84  | 100%|
|[🥇 OptVerse 1.0.0](cconvex-OPTVERS.html) | 1.00 (1.00) | 100%|
|[🥈 COPT 7.1.0](cconvex-COPT.html) | 1.23 (1.23) | 100%|
|[🥉 MOSEK 10.1.21](cconvex-MOSEK.html) | 1.97 (1.97) | 98%|
|[📊 KNITRO 14.1.0](cconvex-KNITRO.html) | 2.37 (2.37) | 95%|
|[📊 MindOpt 1.0.0](cconvex-MINDOPT.html) | 7.09 (6.70) | 81%|
|[📊 IPOPT 3.14.5](cconvex-IPOPT.html) | 11.05 (11.10) | 83%|
|[📊 Mnotaur](cconvex-Mnotaur.html) | 55.95 (55.90) | 60%|


<details><summary>previous benchmarks 🔽</summary>
<br>

<ul>
<li><a href="/mittelmann-plots/cconvex-21-Aug-2024.html">21 Aug 2024</a></li>
<li><a href="/mittelmann-plots/cconvex-9-Aug-2024.html">9 Aug 2024</a></li>
<li><a href="/mittelmann-plots/cconvex-12-Mar-2024.html">12 Mar 2024</a></li>
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


## [Convex Discrete QPLIB Benchmark (21 Aug 2024)](http://plato.asu.edu/ftp/convex.html)
Choose base solver for comparison:

| solver | score (as reported) | solved of 31|
| :--- | ---:  | ---:   |
|[⭐ virtual best](convex-vbest.html) | 0.72  | 87%|
|[🥇 COPT 7.1.0](convex-COPT.html) | 1.00 (1.00) | 77%|
|[🥈 Shot 1.1](convex-SHOT.html) | 1.07 (1.07) | 81%|
|[🥉 Baron 24.5.8](convex-BARON.html) | 4.28 (4.28) | 65%|
|[📊 MOSEK 10.2.2](convex-MOSEK.html) | 10.03 (10.00) | 58%|
|[📊 KNITRO 14.1.0](convex-KNITRO.html) | 12.75 (13.60) | 52%|
|[📊 SCIP 9.0.0](convex-SCIP.html) | 21.82 (21.80) | 45%|
|[📊 Bonmin 1.8.7](convex-BONMIN.html) | 54.63 (54.60) | 23%|
|[📊 MNTAUR](convex-MNTAUR.html) | 63.98 (64.00) | 26%|


<details><summary>previous benchmarks 🔽</summary>
<br>

<ul>
<li><a href="/mittelmann-plots/convex-13-Aug-2024.html">13 Aug 2024</a></li>
<li><a href="/mittelmann-plots/convex-10-Aug-2024.html">10 Aug 2024</a></li>
<li><a href="/mittelmann-plots/convex-11-Jun-2024.html">11 Jun 2024</a></li>
<li><a href="/mittelmann-plots/convex-28-Apr-2024.html">28 Apr 2024</a></li>
<li><a href="/mittelmann-plots/convex-13-Apr-2024.html">13 Apr 2024</a></li>
<li><a href="/mittelmann-plots/convex-11-Apr-2024.html">11 Apr 2024</a></li>
<li><a href="/mittelmann-plots/convex-11-Mar-2024.html">11 Mar 2024</a></li>
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


## [Mixed Integer Nonlinear Programming Benchmark (MINLPLIB) (6 Sep 2024)](http://plato.asu.edu/ftp/minlp.html)
Choose base solver for comparison:

| solver | score (as reported) | solved of 87|
| :--- | ---:  | ---:   |
|[⭐ virtual best](minlp-vbest.html) | 0.28  | 94%|
|[🥇 BARON](minlp-BARON.html) | 1.00 (1.00) | 86%|
|[🥈 SHOT](minlp-SHOT.html) | 1.90 (1.90) | 61%|
|[🥉 SCIP](minlp-SCIP.html) | 3.89 (3.90) | 75%|
|[📊 ANTIGONE](minlp-ANTIGONE.html) | 15.96 (16.00) | 60%|
|[📊 LINDO](minlp-LINDO.html) | 18.77 (18.80) | 32%|


<details><summary>previous benchmarks 🔽</summary>
<br>

<ul>
<li><a href="/mittelmann-plots/minlp-8-Jun-2024.html">8 Jun 2024</a></li>
<li><a href="/mittelmann-plots/minlp-12-Apr-2024.html">12 Apr 2024</a></li>
<li><a href="/mittelmann-plots/minlp-7-Feb-2024.html">7 Feb 2024</a></li>
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
|[🥇 KNITRO 14.0](mpec-KNITRO.html) | 1.00 (1.00) | 93%|
|[🥈 filter MPEC](mpec-filter.html) | 16.90 (16.90) | 62%|
|[🥉 LOQO 7.03](mpec-LOQO.html) | 37.10 (37.10) | 21%|


<details><summary>previous benchmarks 🔽</summary>
<br>

<ul>
<li><a href="/mittelmann-plots/mpec-2-Feb-2024.html">2 Feb 2024</a></li>
<li><a href="/mittelmann-plots/mpec-12-Apr-2022.html">12 Apr 2022</a></li>
</ul></details>

---

