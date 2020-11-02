---
bibliography: [references.bib]
---

This template uses recent versions of `pandoc` and `pandoc-crossref` to
faciltate the referencing of equations, figures, and tables within the text. For
example, the following equation

$$J'(p) = \frac{1}{\text{log}(S)}\times\left(-\sum p \times \text{log}(p)\right)$$ {#eq:eq1}

is produced using

~~~latex
$$J'(p) = \frac{1}{\text{log}(S)}\times\left(-\sum p \times \text{log}(p)\right)$$ {#eq:eq1}
~~~

and can be referenced using `@eq:eq1`, which will result in @eq:eq1.

All documents will be deployed to `gh-pages` *only* on push events from the `master`
All of the artifacts will be built when doing pull requests, so you can check that
merging a branch is *not* going to cause the compilation of the documents to fail.

# Using references

The references are managed by the `citeproc` filter for `pandoc`. Note that we
*do not* use `pandoc-citeproc`, which was an external moduler for older `pandoc`
versions. References *have to* be stored in a `references.bib` file. We use
[Zotero](https://www.zotero.org/) for references management, and for the lab's
manuscripts, we work from folders in a shared library (with a folder for every
manuscript).


We use the [Better BibTeX](https://retorque.re/zotero-better-bibtex/) plugin for
citation key generations, and auto-export of the shared library to the
`references.bib` file. We use a citation key format meant to convey information
on the author, date, year, and title. It must be set in the Better BibTeX
preferences as

~~~
[auth:fold][year][title:fold:nopunctordash:skipwords:lower:select=1,1:substring=1,3:capitalize][title:fold:nopunctordash:skipwords:lower:select=2,2:substring=1,3:capitalize]
~~~

The citations are done using normal markdown, where `@Elton1927AniEco` produces
@Elton1927AniEco, and `[@Camerano1880EquViv]` produces [@Camerano1880EquViv].

# Tables

Tables are supported in their normal markdown way:

| Column 1 | Column 2 | Column 3 |
|----------|---------:|:--------:|
| c1       |       c2 |    c3    |
| c2       |       c3 |    c4    |
| c5       |       c6 |    c7    |

# Figures

Figures can have a legend -- all figures *must* be in the `figures/` folder of
the project:

~~~
![This is the legend of the figure](figures/biomes.png){#fig:biomes}
~~~

![This is the legend of the figure](figures/biomes.png){#fig:biomes}

We can now use `@fig:biomes` to refer to @fig:biomes.

# References
