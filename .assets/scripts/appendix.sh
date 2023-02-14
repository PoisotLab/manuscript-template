for file in appendix/*.md; do
    pandoc "$file" -s -o dist/"${file%.md}".pdf --citeproc --bibliography=references.json --csl .assets/citationstyle.csl --metadata-file=manuscript-metadata.json --template=.assets/templates/appendix.tex
done