import subprocess
import json
import os

with open("references.json") as jsfile:
    references = json.load(jsfile)

# Fields to remove
fields = ["source", "abstract", "language", "accessed", "container-title-short",
          "title-short", "ISSN", "call-number", "number-of-pages", "ISBN", "note", "annote"]
for reference in references:
    for field in fields:
        reference.pop(field, None)

with open("references.json", "w") as outfile:
    json.dump(references, outfile, sort_keys=True,
              indent=4, separators=(',', ': '))
    outfile.write('\n')
