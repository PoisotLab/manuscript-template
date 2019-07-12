# The model

This is a citation: @HampAnde15.

# Methods

There is an equation, which we can cite with {@eq:eq1}.

$$J'(p) = \frac{1}{\text{log}(S)}\times\left(-\sum p \text{log}(p)\right)$$ {#eq:eq1}

# Tables

We can do tables:

| Column 1 | Column 2 |
| -------- | --------:|
| c1       |       c2 |

# Figures

![This is the legend of the figure](figures/biomes.png){#fig:biomes}

We can refer to @fig:biomes.

# Code?

Yes

~~~ julia
for i in eachindex(x)
  x[i] = zero(eltype(x)) # Don't do that
end
~~~

# References
