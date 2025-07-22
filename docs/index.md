Interactive charts comparing the results of [Hans Mittelmann's benchmarks](http://plato.asu.edu/bench.html).
Each solver can be selected to show pairwise running time factors for every other solver in the respective benchmark.
These plots should make browsing the results easier.
The score ([scaled shifted geometric mean](http://plato.asu.edu/ftp/shgeom.html)) is recomputed using the reported solving times.
We also calculate a "virtual best" or "ensemble" solver that picks the best performance over all solvers for every single problem
instance. This might reveal how much potential the individual solvers still have.
[Please let me know](https://github.com/mattmilten/mittelmann-plots/issues/new) if you have a question or if there is an error.

    
## [LPfeas Benchmark (find PD feasible point) + ADDENDUM (18 Jul 2025)](http://plato.asu.edu/ftp/lpfeas.html)
Choose base solver for comparison:

| solver | score (as reported) | solved of 65|
| :--- | ---:  | ---:   |
|[⭐ virtual best](lpfeas-vbest.html) | 0.30  | 100%|
|[🥇 COPT 7.2.0](lpfeas-COPT.html) | 1.00 (1.00) | 100%|
|[🥈 Optverse 1.0.0](lpfeas-OPTV.html) | 1.54 (1.54) | 100%|
|[🥉 cuOpt-H100](lpfeas-CUOPT-H100.html) | 1.86 (1.54) | 89%|
|[📊 cuPDLP-C-H100](lpfeas-CUPDL-H100.html) | 2.22 (1.80) | 88%|
|[📊 cuPDLP-C](lpfeas-CUPDL.html) | 3.05 (2.43) | 86%|
|[📊 MOSEK 11.0.5](lpfeas-MOSEK.html) | 3.29 (3.29) | 91%|
|[📊 cuOpt 25.05](lpfeas-CUOPT.html) | 3.31 (2.36) | 86%|
|[📊 XOPT 0.0.8](lpfeas-XOPT.html) | 5.77 (5.77) | 91%|
|[📊 HPR-LP 0.1.0](lpfeas-HPR-LP.html) | 13.24 (9.00) | 74%|
|[📊 PDLP](lpfeas-PDLP.html) | 16.67 (16.70) | 77%|
|[📊 KNITRO 14.2.0](lpfeas-KNITRO.html) | 21.60 (21.60) | 75%|
|[📊 HiGHS 1.11.0](lpfeas-HiGHS.html) | 22.01 (22.00) | 75%|


<details><summary>previous benchmarks 🔽</summary>
<br>

<ul>
<li><a href="/mittelmann-plots/lpfeas-11-Sep-2024.html">11 Sep 2024</a></li>
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


## [LPopt Benchmark (find optimal basic solution) (16 Jun 2025)](http://plato.asu.edu/ftp/lpopt.html)
Choose base solver for comparison:

| solver | score (as reported) | solved of 65|
| :--- | ---:  | ---:   |
|[⭐ virtual best](lpopt-vbest.html) | 0.90  | 100%|
|[🥇 COPT 7.2.0](lpopt-COPT.html) | 1.00 (1.00) | 100%|
|[🥈 Optverse 1.0.0](lpopt-OPTV.html) | 1.68 (1.68) | 97%|
|[🥉 XOPT 0.0.8](lpopt-XOPT.html) | 6.60 (6.60) | 80%|
|[📊 MOSEK 11.0.13](lpopt-MOSEK.html) | 7.45 (7.45) | 80%|
|[📊 HiGHS 1.11.0](lpopt-HiGHS.html) | 17.04 (17.00) | 78%|
|[📊 CLP 1.17.7](lpopt-CLP.html) | 27.23 (27.20) | 62%|
|[📊 Google-GLOP](lpopt-GLOP.html) | 59.38 (59.40) | 51%|
|[📊 SOPLEX 7.1.2](lpopt-SPLX.html) | 93.53 (93.50) | 49%|


<details><summary>previous benchmarks 🔽</summary>
<br>

<ul>
<li><a href="/mittelmann-plots/lpopt-11-Sep-2024.html">11 Sep 2024</a></li>
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


## [Large Network-LP Benchmark (commercial vs free) (26 Jun 2025)](http://plato.asu.edu/ftp/network.html)
Choose base solver for comparison:

| solver | score (as reported) | solved of 25|
| :--- | ---:  | ---:   |
|[⭐ virtual best](network-vbest.html) | 0.99  | 100%|
|[🥇 OptVerse 1.0.0](network-OPTV.html) | 1.00 (1.00) | 100%|
|[🥈 COPT 7.2.0](network-COPT.html) | 2.15 (2.15) | 100%|
|[🥉 Clp 1.17.7](network-CLP.html) | 5.97 (5.97) | 100%|
|[📊 HiGHS 1.11.0](network-HGHS.html) | 14.07 (14.10) | 80%|
|[📊 MOSEK 11.0.16](network-MOSEK.html) | 27.20 (27.20) | 84%|
|[📊 QSopt 1.01](network-QSOPT.html) | 34.89 (34.90) | 68%|
|[📊 SOPLEX 7.1.2](network-SPLX.html) | 65.43 (65.40) | 64%|


<details><summary>previous benchmarks 🔽</summary>
<br>

<ul>
<li><a href="/mittelmann-plots/network-11-Sep-2024.html">11 Sep 2024</a></li>
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


## [The MIPLIB2017 Benchmark Instances (preprocessed data) - 8 threads (20 Jun 2025)](http://plato.asu.edu/ftp/milp.html)
Choose base solver for comparison:

| solver | score (as reported) | solved of 240|
| :--- | ---:  | ---:   |
|[⭐ virtual best](milp_8threads-vbest.html) | 0.75  | 93%|
|[🥇 COPT](milp_8threads-COPT.html) | 1.00 (1.00) | 90%|
|[🥈 optverse](milp_8threads-optverse.html) | 1.89 (1.89) | 85%|
|[🥉 XOPT](milp_8threads-XOPT.html) | 5.05 (5.05) | 67%|
|[📊 HiGHS](milp_8threads-HiGHS.html) | 6.56 (6.56) | 65%|
|[📊 LEOPT](milp_8threads-LEOPT.html) | 6.69 (6.69) | 62%|
|[📊 SCIPC](milp_8threads-SCIPC.html) | 6.97 (6.97) | 60%|
|[📊 SCIP](milp_8threads-SCIP.html) | 8.76 (8.76) | 53%|


<details><summary>previous benchmarks 🔽</summary>
<br>

<ul>
<li><a href="/mittelmann-plots/milp_8threads-15-Sep-2024.html">15 Sep 2024</a></li>
<li><a href="/mittelmann-plots/milp_8threads-13-Sep-2024.html">13 Sep 2024</a></li>
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


## [MILP cases that are slightly pathological (preprocessed data) (23 Jun 2025)](http://plato.asu.edu/ftp/path.html)
Choose base solver for comparison:

| solver | score (as reported) | solved of 45|
| :--- | ---:  | ---:   |
|[⭐ virtual best](path-vbest.html) | 0.70  | 93%|
|[🥇 COPT 7.2.0](path-COPT.html) | 1.00 (1.00) | 531%|
|[🥈 OptVerse 1.0.0](path-optverse.html) | 2.59 (2.59) | 1376%|
|[🥉 TAYLORMIP 0.8](path-Taylor.html) | 3.57 (3.57) | 1893%|
|[📊 HiGHS 1.11.0](path-HiGHS.html) | 9.03 (9.03) | 4791%|
|[📊 XOPT 0.0.8](path-XOPT.html) | 9.90 (9.90) | 5253%|
|[📊 LEOPT 0.5.1](path-LEOPT.html) | 11.21 (11.20) | 5951%|
|[📊 SCIPC](path-SCIPC.html) | 12.13 (12.10) | 6436%|
|[📊 SCIP 9.2.1](path-SCIP.html) | 17.54 (17.60) | 9311%|


<details><summary>previous benchmarks 🔽</summary>
<br>

<ul>
<li><a href="/mittelmann-plots/path-11-Sep-2024.html">11 Sep 2024</a></li>
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


## [Infeasibility Detection for MILP Problems (25 Jun 2025)](http://plato.asu.edu/ftp/infeas.html)
Choose base solver for comparison:

| solver | score (as reported) | solved of 32|
| :--- | ---:  | ---:   |
|[⭐ virtual best](infeas-vbest.html) | 0.95  | 94%|
|[🥇 COPT 7.2.0](infeas-COPT.html) | 1.00 (1.00) | 94%|
|[🥈 OptVerse 1.0.0](infeas-optverse.html) | 1.21 (1.21) | 94%|
|[🥉 XOPT 0.0.8](infeas-XOPT.html) | 5.08 (6.06) | 78%|
|[📊 SCIPC](infeas-SCIPC.html) | 5.17 (5.17) | 81%|
|[📊 HiGHS 1.11.0](infeas-HiGHS.html) | 6.60 (6.60) | 78%|
|[📊 SCIP 9.2.1](infeas-SCIP.html) | 7.35 (7.35) | 69%|
|[📊 CBC 2.10.5](infeas-CBC.html) | 16.19 (16.20) | 62%|


<details><summary>previous benchmarks 🔽</summary>
<br>

<ul>
<li><a href="/mittelmann-plots/infeas-11-Sep-2024.html">11 Sep 2024</a></li>
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


## [Several SDP-codes on sparse and other SDP problems (also on GPUs) (20 Jul 2025)](http://plato.asu.edu/ftp/sparse_sdp.html)
Choose base solver for comparison:

| solver | score (as reported) | solved of 75|
| :--- | ---:  | ---:   |
|[⭐ virtual best](sparse_sdp-vbest.html) | 0.38  | 100%|
|[🥇 COPT 7.2.0](sparse_sdp-COPT.html) | 1.00 (1.00) | 100%|
|[🥈 MOSEK 11.0.16](sparse_sdp-MOSEK.html) | 2.69 (2.69) | 97%|
|[🥉 cuLoRADS 1.0.0](sparse_sdp-cuLoRAD.html) | 3.97 (3.97) | 95%|
|[📊 SDPT3 4.0](sparse_sdp-SDPT3.html) | 5.34 (5.34) | 92%|
|[📊 CSDP 6.2.0](sparse_sdp-CSDP.html) | 5.41 (5.41) | 93%|
|[📊 SDPA 7.4.2](sparse_sdp-SDPA.html) | 10.85 (10.90) | 81%|
|[📊 SeDuMi 1.3.5](sparse_sdp-SeDuMi.html) | 29.99 (30.00) | 83%|


<details><summary>previous benchmarks 🔽</summary>
<br>

<ul>
<li><a href="/mittelmann-plots/sparse_sdp-28-Aug-2024.html">28 Aug 2024</a></li>
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


## [Large Second Order Cone Benchmark (5 Apr 2025)](http://plato.asu.edu/ftp/socp.html)
Choose base solver for comparison:

| solver | score (as reported) | solved of 18|
| :--- | ---:  | ---:   |
|[⭐ virtual best](socp-vbest.html) | 0.88  | 100%|
|[🥇 COPT 7.2.0       COPT ](socp-COPT.html) | 1.00 (1.00) | 100%|
|[🥈 Optverse 1.0.0   OPTVERSE](socp-OPTVERSE.html) | 1.10 (1.10) | 100%|
|[🥉 MOSEK 11.0.13    MOSEK ](socp-MOSEK.html) | 1.24 (1.24) | 100%|
|[📊 KNITRO 14.0.0    Knitro ](socp-KNITRO.html) | 11.11 (11.10) | 94%|
|[📊 ECOS 2.0.4       ECOS ](socp-ECOS.html) | 116.88 (117.00) | 61%|


<details><summary>previous benchmarks 🔽</summary>
<br>

<ul>
<li><a href="/mittelmann-plots/socp-11-Sep-2024.html">11 Sep 2024</a></li>
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


## [Mixed-integer SOCP Benchmark (9 Apr 2025)](http://plato.asu.edu/ftp/misocp.html)
Choose base solver for comparison:

| solver | score (as reported) | solved of 47|
| :--- | ---:  | ---:   |
|[⭐ virtual best](misocp-vbest.html) | 0.98  | 98%|
|[🥇 COPT 7.2.0](misocp-COPT.html) | 1.00 (1.00) | 98%|
|[🥈 MOSEK 11.0.13](misocp-MOSEK.html) | 6.36 (5.47) | 77%|
|[🥉 SCIP 9.2.1](misocp-SCIP.html) | 12.26 (9.81) | 66%|


<details><summary>previous benchmarks 🔽</summary>
<br>

<ul>
<li><a href="/mittelmann-plots/misocp-21-Aug-2024.html">21 Aug 2024</a></li>
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


## [Binary Non-Convex QPLIB Benchmark (26 Jun 2025)](http://plato.asu.edu/ftp/qplib.html)
Choose base solver for comparison:

| solver | score (as reported) | solved of 97|
| :--- | ---:  | ---:   |
|[⭐ virtual best](qplib-vbest.html) | 0.67  | 98%|
|[🥇 SHOT 1.1](qplib-SHOT.html) | 1.00 (1.00) | 94%|
|[🥈 Baron 25.3.19](qplib-BARON.html) | 7.11 (7.11) | 67%|
|[🥉 RAPOSa 4.4.1](qplib-RAPOSa.html) | 10.26 (10.30) | 71%|
|[📊 SCIP 9.2.1](qplib-SCIP.html) | 31.72 (31.70) | 36%|
|[📊 ANTIGONE 1.1](qplib-ANTIGONE.html) | 63.08 (63.10) | 16%|
|[📊 COUENNE 0.5](qplib-COUENNE.html) | 74.93 (74.90) | 6%|


<details><summary>previous benchmarks 🔽</summary>
<br>

<ul>
<li><a href="/mittelmann-plots/qplib-21-Aug-2024.html">21 Aug 2024</a></li>
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


## [Nonconvex QUBO-QPLIB Benchmark (12 Jul 2025)](http://plato.asu.edu/ftp/qubo.html)
Choose base solver for comparison:

| solver | score (as reported) | solved of 23|
| :--- | ---:  | ---:   |
|[⭐ virtual best](qubo-vbest.html) | 0.96  | 70%|
|[🥇 QuBowl](qubo-QUBOWL.html) | 1.00 (1.00) | 65%|
|[🥈 Baron 25.3.19](qubo-BARON.html) | 1.80 (1.80) | 57%|
|[🥉 SHOT 1.1](qubo-SHOT.html) | 1.84 (1.84) | 52%|
|[📊 McSparse 2.0](qubo-MCSPARSE.html) | 2.89 (2.89) | 52%|
|[📊 SCIP 9.2.1](qubo-SCIP.html) | 6.82 (6.82) | 30%|
|[📊 Biqbin](qubo-BIQBIN.html) | 9.33 (6.60) | 39%|


<details><summary>previous benchmarks 🔽</summary>
<br>

<ul>
<li><a href="/mittelmann-plots/qubo-21-Aug-2024.html">21 Aug 2024</a></li>
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


## [Discrete Non-Convex QPLIB Benchmark (non-binary) (13 Jul 2025)](http://plato.asu.edu/ftp/nonbinary.html)
Choose base solver for comparison:

| solver | score (as reported) | solved of 104|
| :--- | ---:  | ---:   |
|[⭐ virtual best](nonbinary-vbest.html) | 0.75  | 96%|
|[🥇 SHOT 1.1](nonbinary-SHOT.html) | 1.00 (1.00) | 91%|
|[🥈 Baron 25.3.19](nonbinary-BARON.html) | 7.95 (7.95) | 66%|
|[🥉 SCIP 9.2.1](nonbinary-SCIP.html) | 36.96 (37.00) | 38%|
|[📊 ANTIGONE 1.1](nonbinary-ANTIGONE.html) | 84.87 (84.90) | 27%|


<details><summary>previous benchmarks 🔽</summary>
<br>

<ul>
<li><a href="/mittelmann-plots/nonbinary-21-Aug-2024.html">21 Aug 2024</a></li>
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


## [Continuous Non-Convex QPLIB Benchmark (11 Jul 2025)](http://plato.asu.edu/ftp/cnconv.html)
Choose base solver for comparison:

| solver | score (as reported) | solved of 52|
| :--- | ---:  | ---:   |
|[⭐ virtual best](cnconv-vbest.html) | 0.23  | 100%|
|[🥇 Baron 25.3.19](cnconv-BARON.html) | 1.00 (1.00) | 67%|
|[🥈 MINOTAUR 0.4.1](cnconv-MINOTAUR.html) | 4.49 (4.49) | 48%|
|[🥉 ANTIGONE 1.1](cnconv-ANTIGONE.html) | 5.23 (5.23) | 52%|
|[📊 SCIP 9.2.1](cnconv-SCIP.html) | 11.39 (11.40) | 27%|


<details><summary>previous benchmarks 🔽</summary>
<br>

<ul>
<li><a href="/mittelmann-plots/cnconv-21-Aug-2024.html">21 Aug 2024</a></li>
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


## [Convex Continuous QPLIB Benchmark (also on GPUs) (17 Jul 2025)](http://plato.asu.edu/ftp/cconvex.html)
Choose base solver for comparison:

| solver | score (as reported) | solved of 42|
| :--- | ---:  | ---:   |
|[⭐ virtual best](cconvex-vbest.html) | 0.82  | 100%|
|[🥇 COPT 7.2.0](cconvex-COPT.html) | 1.00 (1.00) | 100%|
|[🥈 OptVerse 1.0.0](cconvex-OPTVERS.html) | 1.08 (1.08) | 100%|
|[🥉 KNITRO 15.0.0](cconvex-KNITRO.html) | 1.90 (1.90) | 98%|
|[📊 MOSEK 11.0.16](cconvex-MOSEK.html) | 2.32 (2.32) | 98%|
|[📊 IPOPT 3.14.5](cconvex-IPOPT.html) | 11.92 (11.90) | 83%|
|[📊 Mnotaur](cconvex-Mnotaur.html) | 60.35 (60.30) | 60%|


<details><summary>previous benchmarks 🔽</summary>
<br>

<ul>
<li><a href="/mittelmann-plots/cconvex-11-Sep-2024.html">11 Sep 2024</a></li>
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


## [Convex Discrete QPLIB Benchmark (6 Jul 2025)](http://plato.asu.edu/ftp/convex.html)
Choose base solver for comparison:

| solver | score (as reported) | solved of 32|
| :--- | ---:  | ---:   |
|[⭐ virtual best](convex-vbest.html) | 0.53  | 91%|
|[🥇 COPT 7.2.0](convex-COPT.html) | 1.00 (1.00) | 75%|
|[🥈 Shot 1.1](convex-SHOT.html) | 1.03 (1.03) | 78%|
|[🥉 Baron 25.3.19](convex-BARON.html) | 2.15 (2.15) | 72%|
|[📊 MOSEK 11.0.16](convex-MOSEK.html) | 6.79 (6.79) | 62%|
|[📊 KNITRO 15.0.0](convex-KNITRO.html) | 11.16 (11.20) | 47%|
|[📊 SCIP 9.2.1](convex-SCIP.html) | 18.92 (18.90) | 44%|
|[📊 Bonmin 1.8.7](convex-BONMIN.html) | 45.69 (45.70) | 22%|
|[📊 MNTAUR](convex-MNTAUR.html) | 53.24 (53.20) | 25%|


<details><summary>previous benchmarks 🔽</summary>
<br>

<ul>
<li><a href="/mittelmann-plots/convex-21-Aug-2024.html">21 Aug 2024</a></li>
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


## [Mixed Integer Nonlinear Programming Benchmark (MINLPLIB) (24 Jun 2025)](http://plato.asu.edu/ftp/minlp.html)
Choose base solver for comparison:

| solver | score (as reported) | solved of 200|
| :--- | ---:  | ---:   |
|[⭐ virtual best](minlp-vbest.html) | 0.28  | 92%|
|[🥇 BARON](minlp-BARON.html) | 1.00 (1.00) | 80%|
|[🥈 SCIP](minlp-SCIP.html) | 1.59 (1.50) | 76%|
|[🥉 LINDO](minlp-LINDO.html) | 4.95 (4.80) | 58%|
|[📊 SHOT](minlp-SHOT.html) | 5.23 (5.10) | 48%|


<details><summary>previous benchmarks 🔽</summary>
<br>

<ul>
<li><a href="/mittelmann-plots/minlp-6-Sep-2024.html">6 Sep 2024</a></li>
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


## [MPEC Benchmark (Math. Progr. w. Equilibrium Constraints) (14 Apr 2025)](http://plato.asu.edu/ftp/mpec.html)
Choose base solver for comparison:

| solver | score (as reported) | solved of 29|
| :--- | ---:  | ---:   |
|[⭐ virtual best](mpec-vbest.html) | 1.00  | 97%|
|[🥇 KNITRO 14.2](mpec-KNITRO.html) | 1.00 (1.00) | 97%|
|[🥈 filter-MPEC](mpec-filter.html) | 18.15 (18.10) | 62%|
|[🥉 LOQO 7.03](mpec-LOQO.html) | 39.84 (39.80) | 21%|


<details><summary>previous benchmarks 🔽</summary>
<br>

<ul>
<li><a href="/mittelmann-plots/mpec-9-Feb-2024.html">9 Feb 2024</a></li>
<li><a href="/mittelmann-plots/mpec-2-Feb-2024.html">2 Feb 2024</a></li>
<li><a href="/mittelmann-plots/mpec-12-Apr-2022.html">12 Apr 2022</a></li>
</ul></details>

---

