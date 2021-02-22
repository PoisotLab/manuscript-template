import subprocess
import json
import os

with open("metadata.json") as jsfile:
    metadata = json.load(jsfile)

biorxiv = open("author_template.tsv", "w")
biorxiv.write("Email	Institution	First Name	Middle Name(s)/Initial(s)	Last Name	Suffix	Corresponding Author	Home Page URL	Collaborative Group/Consortium	ORCiD\n")

# Fields to remove
creators = metadata["creators"]
affiliation_to_number = {}

for creator in creators:
    affiliations = creator["affiliations"]
    for affiliation in affiliations:
        if not (affiliation in affiliation_to_number.keys()):
            affiliation_to_number[affiliation] = len(affiliation_to_number) + 1
    # BIORXIV info block
    if "email" in creator.keys():
        biorxiv.write(creator["email"])
    biorxiv.write("\t")
    # Institution
    biorxiv.write(affiliations[0])
    biorxiv.write("\t")
    # Name
    biorxiv.write(creator["givennames"])
    biorxiv.write("\t")
    biorxiv.write("\t")
    biorxiv.write(creator["familyname"])
    biorxiv.write("\t")
    biorxiv.write("\t")
    biorxiv.write("\t")
    biorxiv.write("\t")
    biorxiv.write("\t")
    if "orcid" in creator.keys():
        biorxiv.write(creator["orcid"])
    biorxiv.write("\n")
    
biorxiv.close()

for creator in creators:
    creator["affilcode"] = [affiliation_to_number[affiliation]
                            for affiliation in creator["affiliations"]]
    creator.pop("affiliations", None)

affiliations = {}
affiliations["authors"] = creators
affiliations["institutions"] = [{"id": v, "name": k} for k, v in sorted(
    affiliation_to_number.items(), key=lambda item: item[1])]

affiliations["metadata"] = {}
affiliations["metadata"]["corresponding"] = []

# Check authorship and correspondance
toadd = True
for creator in affiliations["authors"]:
    if "status" in creator.keys():
        if "equal" in creator["status"]:
            creator["affilcode"].append("‡")
            if toadd:
                affiliations["metadata"]["equalcontributions"] = {"id": "‡", "name": "These authors contributed equally to the work"}
                toadd = False
        if "corresponding" in creator["status"]:
            affiliations["metadata"]["corresponding"].append({"given": creator["givennames"], "family": creator["familyname"], "email": creator["email"]})

with open("affiliations.json", "w") as outfile:
    json.dump(affiliations, outfile, sort_keys=False,
              indent=4, separators=(',', ': '))
    outfile.write('\n')