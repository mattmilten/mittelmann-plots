Interactive charts comparing the results of [Hans Mittelmann's benchmarks](http://plato.asu.edu/bench.html).
Each solver can be selected to show pairwise running time factors for every other solver in the respective benchmark.
These plots should make browsing the results easier.
The score ([scaled shifted geometric mean](http://plato.asu.edu/ftp/shgeom.html)) is recomputed using the reported solving times.
We also calculate a "virtual best" or "ensemble" solver that picks the best performance over all solvers for every single problem
instance. This might reveal how much potential the individual solvers still have.
[Please let me know](https://github.com/mattmilten/mittelmann-plots/issues/new) if you have a question or if there is an error.

    
## [LPfeas Benchmark (find PD feasible point) + ADDENDUM (12 Jun 2026)](http://plato.asu.edu/ftp/lpfeas.html)
Choose base solver for comparison:

| solver | score (as reported) | solved of 65|
| :--- | ---:  | ---:   |
|[⭐ virtual best](lpfeas-vbest.html) | 0.47  | 100%|
|[🥇 COPTG](lpfeas-COPTG.html) | 1.00 (1.00) | 98%|
|[🥈 cuOpt 26.06](lpfeas-CUOPT.html) | 1.07 (1.07) | 95%|
|[🥉 HPRLP](lpfeas-HPRLP.html) | 1.36 (1.36) | 89%|
|[📊 COPT 8.0.0/3](lpfeas-COPT.html) | 1.67 (1.67) | 100%|
|[📊 CUPDX](lpfeas-CUPDX.html) | 1.88 (1.88) | 88%|
|[📊 MOSEK 11.1.11](lpfeas-MOSEK.html) | 5.28 (4.93) | 88%|
|[📊 XOPT 0.0.8](lpfeas-XOPT.html) | 9.63 (9.63) | 91%|
|[📊 HiGHS 1.14.0](lpfeas-HiGHS.html) | 17.24 (17.20) | 86%|
|[📊 PDLP](lpfeas-PDLP.html) | 27.85 (27.80) | 77%|
|[📊 KNTRO](lpfeas-KNTRO.html) | 28.49 (28.50) | 75%|


<details><summary>previous benchmarks 🔽</summary>
<br>

<ul>
<li><a href="/mittelmann-plots/lpfeas-10-Apr-2026.html">10 Apr 2026</a></li>
<li><a href="/mittelmann-plots/lpfeas-18-Feb-2026.html">18 Feb 2026</a></li>
<li><a href="/mittelmann-plots/lpfeas-12-Feb-2026.html">12 Feb 2026</a></li>
<li><a href="/mittelmann-plots/lpfeas-13-Jan-2026.html">13 Jan 2026</a></li>
<li><a href="/mittelmann-plots/lpfeas-19-Dec-2025.html">19 Dec 2025</a></li>
<li><a href="/mittelmann-plots/lpfeas-11-Nov-2025.html">11 Nov 2025</a></li>
<li><a href="/mittelmann-plots/lpfeas-3-Nov-2025.html">3 Nov 2025</a></li>
<li><a href="/mittelmann-plots/lpfeas-29-Oct-2025.html">29 Oct 2025</a></li>
<li><a href="/mittelmann-plots/lpfeas-20-Oct-2025.html">20 Oct 2025</a></li>
<li><a href="/mittelmann-plots/lpfeas-31-Jul-2025.html">31 Jul 2025</a></li>
<li><a href="/mittelmann-plots/lpfeas-18-Jul-2025.html">18 Jul 2025</a></li>
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


## [LPopt Benchmark (find optimal basic solution) (29 Apr 2026)](http://plato.asu.edu/ftp/lpopt.html)
Choose base solver for comparison:

| solver | score (as reported) | solved of 65|
| :--- | ---:  | ---:   |
|[⭐ virtual best](lpopt-vbest.html) | 0.97  | 100%|
|[🥇 COPT 8.0.0](lpopt-COPT.html) | 1.00 (1.00) | 100%|
|[🥈 MOSEK 11.1.11](lpopt-MOSEK.html) | 6.24 (6.24) | 80%|
|[🥉 XOPT 0.0.8](lpopt-XOPT.html) | 6.63 (6.63) | 80%|
|[📊 HiGHS 1.14.0](lpopt-HiGHS.html) | 13.07 (13.10) | 82%|
|[📊 CLP 1.17.7](lpopt-CLP.html) | 27.38 (27.40) | 62%|
|[📊 Google-GLOP](lpopt-GLOP.html) | 59.71 (59.70) | 51%|
|[📊 SOPLEX 8.0.0](lpopt-SPLX.html) | 103.92 (104.00) | 48%|


<details><summary>previous benchmarks 🔽</summary>
<br>

<ul>
<li><a href="/mittelmann-plots/lpopt-10-Apr-2026.html">10 Apr 2026</a></li>
<li><a href="/mittelmann-plots/lpopt-10-apr-2026.html">10 apr 2026</a></li>
<li><a href="/mittelmann-plots/lpopt-8-Feb-2026.html">8 Feb 2026</a></li>
<li><a href="/mittelmann-plots/lpopt-10-Dec-2025.html">10 Dec 2025</a></li>
<li><a href="/mittelmann-plots/lpopt-13-Nov-2025.html">13 Nov 2025</a></li>
<li><a href="/mittelmann-plots/lpopt-3-Nov-2025.html">3 Nov 2025</a></li>
<li><a href="/mittelmann-plots/lpopt-29-Oct-2025.html">29 Oct 2025</a></li>
<li><a href="/mittelmann-plots/lpopt-18-Oct-2025.html">18 Oct 2025</a></li>
<li><a href="/mittelmann-plots/lpopt-16-Jun-2025.html">16 Jun 2025</a></li>
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


## [Large Network-LP Benchmark (commercial vs free) (28 Apr 2026)](http://plato.asu.edu/ftp/network.html)
Choose base solver for comparison:

| solver | score (as reported) | solved of 25|
| :--- | ---:  | ---:   |
|[⭐ virtual best](network-vbest.html) | 1.00  | 100%|
|[🥇 COPT 8.0.0](network-COPT.html) | 1.00 (1.00) | 100%|
|[🥈 Clp 1.17.7](network-CLP.html) | 2.74 (2.74) | 100%|
|[🥉 HiGHS 1.14.0](network-HGHS.html) | 6.59 (6.59) | 80%|
|[📊 MOSEK 11.1.11](network-MOSEK.html) | 13.46 (13.50) | 84%|
|[📊 QSopt 1.01](network-QSOPT.html) | 16.04 (16.00) | 68%|
|[📊 SOPLEX 8.0.0](network-SPLX.html) | 33.03 (33.00) | 64%|


<details><summary>previous benchmarks 🔽</summary>
<br>

<ul>
<li><a href="/mittelmann-plots/network-11-Apr-2026.html">11 Apr 2026</a></li>
<li><a href="/mittelmann-plots/network-16-Feb-2026.html">16 Feb 2026</a></li>
<li><a href="/mittelmann-plots/network-8-Dec-2025.html">8 Dec 2025</a></li>
<li><a href="/mittelmann-plots/network-29-Oct-2025.html">29 Oct 2025</a></li>
<li><a href="/mittelmann-plots/network-18-Oct-2025.html">18 Oct 2025</a></li>
<li><a href="/mittelmann-plots/network-26-Jun-2025.html">26 Jun 2025</a></li>
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


## [The MIPLIB2017 Benchmark Instances (preprocessed data) - 8 threads (27 Apr 2026)](http://plato.asu.edu/ftp/milp.html)
Choose base solver for comparison:

| solver | score (as reported) | solved of 240|
| :--- | ---:  | ---:   |
|[⭐ virtual best](milp_8threads-vbest.html) | 0.76  | 94%|
|[🥇 COPT](milp_8threads-COPT.html) | 1.00 (1.00) | 91%|
|[🥈 optverse](milp_8threads-optverse.html) | 1.72 (1.72) | 88%|
|[🥉 XSMOO](milp_8threads-XSMOO.html) | 5.15 (5.15) | 72%|
|[📊 HiGHS](milp_8threads-HiGHS.html) | 7.36 (7.36) | 68%|
|[📊 SCIPC](milp_8threads-SCIPC.html) | 8.45 (8.45) | 62%|
|[📊 SCIP](milp_8threads-SCIP.html) | 9.93 (9.93) | 57%|


<details><summary>previous benchmarks 🔽</summary>
<br>

<ul>
<li><a href="/mittelmann-plots/milp_8threads-9-Feb-2026.html">9 Feb 2026</a></li>
<li><a href="/mittelmann-plots/milp_8threads-30-Nov-2025.html">30 Nov 2025</a></li>
<li><a href="/mittelmann-plots/milp_8threads-29-Oct-2025.html">29 Oct 2025</a></li>
<li><a href="/mittelmann-plots/milp_8threads-18-Oct-2025.html">18 Oct 2025</a></li>
<li><a href="/mittelmann-plots/milp_8threads-20-Jun-2025.html">20 Jun 2025</a></li>
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


## [MILP cases that are slightly pathological (preprocessed data) (1 Mar 2026)](http://plato.asu.edu/ftp/path.html)
Choose base solver for comparison:

| solver | score (as reported) | solved of 45|
| :--- | ---:  | ---:   |
|[⭐ virtual best](path-vbest.html) | 0.57  | 98%|
|[🥇 COPT 8.0.3](path-COPT.html) | 1.00 (1.00) | 89%|
|[🥈 Optverse 2.0.1](path-optverse.html) | 1.41 (1.41) | 84%|
|[🥉 XSMO](path-XSMO.html) | 7.19 (7.19) | 73%|
|[📊 SMOO](path-SMOO.html) | 8.74 (8.74) | 64%|
|[📊 HiGHS 1.13.0](path-HiGHS.html) | 10.26 (10.30) | 53%|
|[📊 XOPT 0.0.8](path-XOPT.html) | 10.60 (10.60) | 53%|
|[📊 SCIPC](path-SCIPC.html) | 11.10 (11.10) | 62%|
|[📊 SCIP 10.0.0](path-SCIP.html) | 19.49 (19.50) | 44%|


<details><summary>previous benchmarks 🔽</summary>
<br>

<ul>
<li><a href="/mittelmann-plots/path-12-Feb-2026.html">12 Feb 2026</a></li>
<li><a href="/mittelmann-plots/path-29-Nov-2025.html">29 Nov 2025</a></li>
<li><a href="/mittelmann-plots/path-29-Oct-2025.html">29 Oct 2025</a></li>
<li><a href="/mittelmann-plots/path-19-Sep-2025.html">19 Sep 2025</a></li>
<li><a href="/mittelmann-plots/path-23-Jun-2025.html">23 Jun 2025</a></li>
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


## [Infeasibility Detection for MILP Problems (5 May 2026)](http://plato.asu.edu/ftp/infeas.html)
Choose base solver for comparison:

| solver | score (as reported) | solved of 32|
| :--- | ---:  | ---:   |
|[⭐ virtual best](infeas-vbest.html) | 0.99  | 94%|
|[🥇 COPT 8.0.0](infeas-COPT.html) | 1.00 (1.00) | 94%|
|[🥈 XSMOO](infeas-XSMOO.html) | 4.94 (4.94) | 88%|
|[🥉 XOPT 0.0.8](infeas-XOPT.html) | 6.32 (6.32) | 94%|
|[📊 SCIPC](infeas-SCIPC.html) | 7.56 (7.56) | 84%|
|[📊 HiGHS 1.13.0](infeas-HiGHS.html) | 8.65 (8.65) | 78%|
|[📊 SCIP 10.0.0](infeas-SCIP.html) | 9.22 (9.22) | 69%|
|[📊 CBC 2.10.5](infeas-CBC.html) | 20.16 (20.20) | 62%|


<details><summary>previous benchmarks 🔽</summary>
<br>

<ul>
<li><a href="/mittelmann-plots/infeas-15-Feb-2026.html">15 Feb 2026</a></li>
<li><a href="/mittelmann-plots/infeas-2-Dec-2025.html">2 Dec 2025</a></li>
<li><a href="/mittelmann-plots/infeas-29-Oct-2025.html">29 Oct 2025</a></li>
<li><a href="/mittelmann-plots/infeas-19-Oct-2025.html">19 Oct 2025</a></li>
<li><a href="/mittelmann-plots/infeas-25-Jun-2025.html">25 Jun 2025</a></li>
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


## [Several SDP-codes on sparse and other SDP problems (also on GPUs) (25 Apr 2026)](http://plato.asu.edu/ftp/sparse_sdp.html)
Choose base solver for comparison:

| solver | score (as reported) | solved of 75|
| :--- | ---:  | ---:   |
|[⭐ virtual best](sparse_sdp-vbest.html) | 0.31  | 100%|
|[🥇 COPT 8.0.3](sparse_sdp-COPT.html) | 1.00 (1.00) | 100%|
|[🥈 cuLoRADS 1.0.0](sparse_sdp-cuLoRAD.html) | 3.01 (3.01) | 95%|
|[🥉 MOSEK 11.1.2](sparse_sdp-MOSEK.html) | 3.67 (3.67) | 97%|
|[📊 SDPT3 4.0](sparse_sdp-SDPT3.html) | 5.32 (5.32) | 92%|
|[📊 CSDP 6.2.0](sparse_sdp-CSDP.html) | 5.40 (5.40) | 93%|
|[📊 SDPA 7.4.4](sparse_sdp-SDPA.html) | 7.99 (7.99) | 81%|
|[📊 SeDuMi 1.3.5](sparse_sdp-SeDuMi.html) | 29.90 (29.90) | 83%|


<details><summary>previous benchmarks 🔽</summary>
<br>

<ul>
<li><a href="/mittelmann-plots/sparse_sdp-22-Jan-2026.html">22 Jan 2026</a></li>
<li><a href="/mittelmann-plots/sparse_sdp-27-Sep-2025.html">27 Sep 2025</a></li>
<li><a href="/mittelmann-plots/sparse_sdp-9-Aug-2025.html">9 Aug 2025</a></li>
<li><a href="/mittelmann-plots/sparse_sdp-20-Jul-2025.html">20 Jul 2025</a></li>
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


## [Large Second Order Cone Benchmark (9 Jan 2026)](http://plato.asu.edu/ftp/socp.html)
Choose base solver for comparison:

| solver | score (as reported) | solved of 18|
| :--- | ---:  | ---:   |
|[⭐ virtual best](socp-vbest.html) | 0.95  | 100%|
|[🥇 COPT 8.0.1       COPT ](socp-COPT.html) | 1.00 (1.00) | 100%|
|[🥈 MOSEK 11.1.2     MOSEK ](socp-MOSEK.html) | 1.41 (1.35) | 100%|
|[🥉 KNITRO 15.0.1    Knitro ](socp-KNITRO.html) | 7.94 (7.94) | 94%|
|[📊 ECOS 2.0.4       ECOS ](socp-ECOS.html) | 127.61 (128.00) | 61%|


<details><summary>previous benchmarks 🔽</summary>
<br>

<ul>
<li><a href="/mittelmann-plots/socp-29-Oct-2025.html">29 Oct 2025</a></li>
<li><a href="/mittelmann-plots/socp-22-Oct-2025.html">22 Oct 2025</a></li>
<li><a href="/mittelmann-plots/socp-18-Oct-2025.html">18 Oct 2025</a></li>
<li><a href="/mittelmann-plots/socp-4-Sep-2025.html">4 Sep 2025</a></li>
<li><a href="/mittelmann-plots/socp-5-Apr-2025.html">5 Apr 2025</a></li>
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


## [Mixed-integer SOCP Benchmark (29 Apr 2026)](http://plato.asu.edu/ftp/misocp.html)
Choose base solver for comparison:

| solver | score (as reported) | solved of 47|
| :--- | ---:  | ---:   |
|[⭐ virtual best](misocp-vbest.html) | 0.98  | 100%|
|[🥇 COPT 8.0.0](misocp-COPT.html) | 1.00 (1.00) | 100%|
|[🥈 MOSEK 11.1.11](misocp-MOSEK.html) | 7.47 (6.41) | 79%|
|[🥉 SCIP 10.0.0](misocp-SCIP.html) | 8.36 (7.40) | 83%|


<details><summary>previous benchmarks 🔽</summary>
<br>

<ul>
<li><a href="/mittelmann-plots/misocp-9-Jan-2026.html">9 Jan 2026</a></li>
<li><a href="/mittelmann-plots/misocp-1-Dec-2025.html">1 Dec 2025</a></li>
<li><a href="/mittelmann-plots/misocp-19-Sep-2025.html">19 Sep 2025</a></li>
<li><a href="/mittelmann-plots/misocp-9-Apr-2025.html">9 Apr 2025</a></li>
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


## [Binary Non-Convex QPLIB Benchmark (9 May 2026)](http://plato.asu.edu/ftp/qplib.html)
Choose base solver for comparison:

| solver | score (as reported) | solved of 97|
| :--- | ---:  | ---:   |
|[⭐ virtual best](qplib-vbest.html) | 0.63  | 99%|
|[🥇 SHOT 1.1](qplib-SHOT.html) | 1.00 (1.00) | 94%|
|[🥈 COPT 8.0.4](qplib-COPT.html) | 2.39 (2.42) | 86%|
|[🥉 Baron 25.11.17](qplib-BARON.html) | 3.95 (4.03) | 76%|
|[📊 RAPOSa 4.4.1](qplib-RAPOSa.html) | 10.85 (10.60) | 71%|
|[📊 SCIP 10.0.0](qplib-SCIP.html) | 29.53 (30.80) | 37%|
|[📊 ANTIGONE 1.1](qplib-ANTIGONE.html) | 63.08 (66.40) | 16%|
|[📊 COUENNE 0.5](qplib-COUENNE.html) | 74.93 (79.00) | 6%|


<details><summary>previous benchmarks 🔽</summary>
<br>

<ul>
<li><a href="/mittelmann-plots/qplib-5-Dec-2025.html">5 Dec 2025</a></li>
<li><a href="/mittelmann-plots/qplib-21-Sep-2025.html">21 Sep 2025</a></li>
<li><a href="/mittelmann-plots/qplib-26-Jun-2025.html">26 Jun 2025</a></li>
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


## [Nonconvex QUBO-QPLIB Benchmark (8 May 2026)](http://plato.asu.edu/ftp/qubo.html)
Choose base solver for comparison:

| solver | score (as reported) | solved of 23|
| :--- | ---:  | ---:   |
|[⭐ virtual best](qubo-vbest.html) | 1.00  | 70%|
|[🥇 QuBowl](qubo-QUBOWL.html) | 1.00 (1.00) | 70%|
|[🥈 Baron 25.11.17](qubo-BARON.html) | 2.59 (2.59) | 57%|
|[🥉 SHOT 1.1](qubo-SHOT.html) | 2.64 (2.64) | 52%|
|[📊 COPT 8.0.4](qubo-COPT.html) | 3.13 (3.13) | 57%|
|[📊 McSparse 2.0](qubo-MCSPARSE.html) | 4.15 (4.15) | 52%|
|[📊 SCIP 10.0.0](qubo-SCIP.html) | 9.60 (9.60) | 35%|
|[📊 Biqbin](qubo-BIQBIN.html) | 13.40 (9.48) | 39%|


<details><summary>previous benchmarks 🔽</summary>
<br>

<ul>
<li><a href="/mittelmann-plots/qubo-11-Apr-2026.html">11 Apr 2026</a></li>
<li><a href="/mittelmann-plots/qubo-10-Dec-2025.html">10 Dec 2025</a></li>
<li><a href="/mittelmann-plots/qubo-19-Sep-2025.html">19 Sep 2025</a></li>
<li><a href="/mittelmann-plots/qubo-12-Jul-2025.html">12 Jul 2025</a></li>
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


## [Discrete Non-Convex QPLIB Benchmark (non-binary) (12 May 2026)](http://plato.asu.edu/ftp/nonbinary.html)
Choose base solver for comparison:

| solver | score (as reported) | solved of 113|
| :--- | ---:  | ---:   |
|[⭐ virtual best](nonbinary-vbest.html) | 0.49  | 96%|
|[🥇 SHOT 1.1](nonbinary-SHOT.html) | 1.00 (1.00) | 88%|
|[🥈 COPT 8.0.4](nonbinary-COPT.html) | 2.01 (2.01) | 78%|
|[🥉 Baron 25.3.19](nonbinary-BARON.html) | 7.92 (7.92) | 58%|
|[📊 SCIP 10.0.0](nonbinary-SCIP.html) | 24.84 (24.80) | 35%|


<details><summary>previous benchmarks 🔽</summary>
<br>

<ul>
<li><a href="/mittelmann-plots/nonbinary-3-Jan-2026.html">3 Jan 2026</a></li>
<li><a href="/mittelmann-plots/nonbinary-28-Sep-2025.html">28 Sep 2025</a></li>
<li><a href="/mittelmann-plots/nonbinary-13-Jul-2025.html">13 Jul 2025</a></li>
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


## [Continuous Non-Convex QPLIB Benchmark (17 May 2026)](http://plato.asu.edu/ftp/cnconv.html)
Choose base solver for comparison:

| solver | score (as reported) | solved of 55|
| :--- | ---:  | ---:   |
|[⭐ virtual best](cnconv-vbest.html) | 0.12  | 95%|
|[🥇 Baron 25.12.10](cnconv-BARON.html) | 1.00 (1.00) | 56%|
|[🥈 COPT 8.0.4](cnconv-COPT.html) | 1.39 (1.39) | 51%|
|[🥉 ANTIGONE 1.1](cnconv-ANTIGONE.html) | 1.65 (1.65) | 64%|
|[📊 MINOTAUR 0.4.1](cnconv-MINOTAUR.html) | 3.12 (3.12) | 40%|
|[📊 SCIP 10.0.1](cnconv-SCIP.html) | 5.28 (5.28) | 27%|


<details><summary>previous benchmarks 🔽</summary>
<br>

<ul>
<li><a href="/mittelmann-plots/cnconv-17-Mar-2026.html">17 Mar 2026</a></li>
<li><a href="/mittelmann-plots/cnconv-28-Sep-2025.html">28 Sep 2025</a></li>
<li><a href="/mittelmann-plots/cnconv-11-Jul-2025.html">11 Jul 2025</a></li>
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


## [Convex Continuous QPLIB Benchmark (also on GPUs) (14 May 2026)](http://plato.asu.edu/ftp/cconvex.html)
Choose base solver for comparison:

| solver | score (as reported) | solved of 42|
| :--- | ---:  | ---:   |
|[⭐ virtual best](cconvex-vbest.html) | 0.88  | 100%|
|[🥇 COPT 8.0.4](cconvex-COPT.html) | 1.00 (1.00) | 100%|
|[🥈 KNITRO 15.0.0](cconvex-KNITRO.html) | 1.96 (1.96) | 98%|
|[🥉 MOSEK 11.1.11](cconvex-MOSEK.html) | 2.42 (2.42) | 95%|
|[📊 IPOPT 3.14.5](cconvex-IPOPT.html) | 12.29 (12.30) | 83%|
|[📊 Mnotaur](cconvex-Mnotaur.html) | 62.22 (62.20) | 60%|


<details><summary>previous benchmarks 🔽</summary>
<br>

<ul>
<li><a href="/mittelmann-plots/cconvex-18-Feb-2026.html">18 Feb 2026</a></li>
<li><a href="/mittelmann-plots/cconvex-31-Dec-2025.html">31 Dec 2025</a></li>
<li><a href="/mittelmann-plots/cconvex-29-Oct-2025.html">29 Oct 2025</a></li>
<li><a href="/mittelmann-plots/cconvex-19-Oct-2025.html">19 Oct 2025</a></li>
<li><a href="/mittelmann-plots/cconvex-17-Jul-2025.html">17 Jul 2025</a></li>
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


## [Convex Discrete QPLIB Benchmark (11 May 2026)](http://plato.asu.edu/ftp/convex.html)
Choose base solver for comparison:

| solver | score (as reported) | solved of 31|
| :--- | ---:  | ---:   |
|[⭐ virtual best](convex-vbest.html) | 0.67  | 87%|
|[🥇 COPT 8.0.4](convex-COPT.html) | 1.00 (1.00) | 77%|
|[🥈 Shot 1.1](convex-SHOT.html) | 1.06 (1.06) | 81%|
|[🥉 Baron 25.12.10](convex-BARON.html) | 3.76 (3.76) | 71%|
|[📊 MOSEK 11.1.11](convex-MOSEK.html) | 7.32 (7.32) | 68%|
|[📊 KNITRO 15.1.0](convex-KNITRO.html) | 12.63 (12.60) | 48%|
|[📊 SCIP 10.0.0](convex-SCIP.html) | 20.98 (21.00) | 45%|
|[📊 Bonmin 1.8.7](convex-BONMIN.html) | 54.07 (54.10) | 23%|
|[📊 MNTAUR](convex-MNTAUR.html) | 63.33 (63.30) | 26%|


<details><summary>previous benchmarks 🔽</summary>
<br>

<ul>
<li><a href="/mittelmann-plots/convex-2-Jan-2026.html">2 Jan 2026</a></li>
<li><a href="/mittelmann-plots/convex-27-Dec-2025.html">27 Dec 2025</a></li>
<li><a href="/mittelmann-plots/convex-20-Sep-2025.html">20 Sep 2025</a></li>
<li><a href="/mittelmann-plots/convex-6-Jul-2025.html">6 Jul 2025</a></li>
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


## [Mixed Integer Nonlinear Programming Benchmark (MINLPLIB) (26 Feb 2026)](http://plato.asu.edu/ftp/minlp.html)
Choose base solver for comparison:

| solver | score (as reported) | solved of 200|
| :--- | ---:  | ---:   |
|[⭐ virtual best](minlp-vbest.html) | 0.29  | 92%|
|[🥇 BARON](minlp-BARON.html) | 1.00 (1.00) | 79%|
|[🥈 SCIP](minlp-SCIP.html) | 1.43 (1.40) | 77%|
|[🥉 LINDO](minlp-LINDO.html) | 4.46 (4.80) | 58%|
|[📊 SHOT](minlp-SHOT.html) | 5.02 (5.60) | 48%|


<details><summary>previous benchmarks 🔽</summary>
<br>

<ul>
<li><a href="/mittelmann-plots/minlp-28-Dec-2025.html">28 Dec 2025</a></li>
<li><a href="/mittelmann-plots/minlp-11-Oct-2025.html">11 Oct 2025</a></li>
<li><a href="/mittelmann-plots/minlp-18-Aug-2025.html">18 Aug 2025</a></li>
<li><a href="/mittelmann-plots/minlp-24-Jun-2025.html">24 Jun 2025</a></li>
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


## [MPEC Benchmark (Math. Progr. w. Equilibrium Constraints) (11 Sep 2025)](http://plato.asu.edu/ftp/mpec.html)
Choose base solver for comparison:

| solver | score (as reported) | solved of 29|
| :--- | ---:  | ---:   |
|[⭐ virtual best](mpec-vbest.html) | 0.85  | 86%|
|[🥇 KNITRO 15.0.1](mpec-KNITRO.html) | 1.00 (1.00) | 86%|
|[🥈 filter-MPEC](mpec-filter.html) | 10.40 (10.40) | 62%|
|[🥉 LOQO 7.03](mpec-LOQO.html) | 22.85 (22.80) | 21%|


<details><summary>previous benchmarks 🔽</summary>
<br>

<ul>
<li><a href="/mittelmann-plots/mpec-14-Apr-2025.html">14 Apr 2025</a></li>
<li><a href="/mittelmann-plots/mpec-9-Feb-2024.html">9 Feb 2024</a></li>
<li><a href="/mittelmann-plots/mpec-2-Feb-2024.html">2 Feb 2024</a></li>
<li><a href="/mittelmann-plots/mpec-12-Apr-2022.html">12 Apr 2022</a></li>
</ul></details>

---

