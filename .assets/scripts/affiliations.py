import subprocess
import json
import os

with open("metadata.json") as jsfile:
    metadata = json.load(jsfile)

# Fields to remove
creators = metadata["creators"]
affiliation_to_number = {}

for creator in creators:
    affiliations = creator["affiliations"]
    for affiliation in affiliations:
        if not (affiliation in affiliation_to_number.keys()):
            affiliation_to_number[affiliation] = len(affiliation_to_number)+1

for creator in creators:
    creator["affilcode"] = [affiliation_to_number[affiliation]
                            for affiliation in creator["affiliations"]]
    creator.pop("affiliations", None)

affiliations = {}
affiliations["authors"] = creators
affiliations["institutions"] = [{"id": v, "name": k} for k, v in sorted(
    affiliation_to_number.items(), key=lambda item: item[1])]

with open("affiliations.json", "w") as outfile:
    json.dump(affiliations, outfile, sort_keys=False,
              indent=4, separators=(',', ': '))
    outfile.write('\n')
