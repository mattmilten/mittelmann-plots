# [📊 Interactive Visualizations of Mittelmann benchmarks](https://mattmilten.github.io/mittelmann-plots/)

We generate interactive [Plotly](https://plotly.com/python/) graphs comparing the results of [Hans Mittelmann's benchmarks](http://plato.asu.edu/bench.html). Each solver can be selected for pairwise running time comparisons with every other solver in the respective benchmark. The times are compared using shifted factors on a logarithmic scale. Additionally, the absolute times of the selected base solver are also plotted on a secondary logarithmic axis on the right.

We also calculate a "virtual best" or "ensemble" solver that picks the best performance over all solvers for every single problem instance. This might reveal show how much potential the individual solvers still have.

These plots should make browsing the results easier. Please let me know if you have a question or if there is an error.

Click on the solver name in the legend to enable or disable it in the plot.

Plots are updated daily.

[![Update plots](https://github.com/mattmilten/mittelmann-plots/workflows/Update%20plots/badge.svg)](https://github.com/mattmilten/mittelmann-plots/actions/workflows/run-python.yml)
