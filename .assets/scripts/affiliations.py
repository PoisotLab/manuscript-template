import subprocess
import json
import os

with open("metadata.json") as jsfile:
    metadata = json.load(jsfile)

biorxiv = open("author_template.tsv", "w")
biorxiv.write("Email	Institution	First Name	Middle Name(s)/Initial(s)	Last Name	Suffix	Corresponding Author	Home Page URL	Collaborative Group/Consortium	ORCiD\n")

# Fields to remove
authors = metadata["authors"]
affiliation_to_number = {}

for author in authors:
    affiliations = author["affiliations"]
    for affiliation in affiliations:
        if not (affiliation in affiliation_to_number.keys()):
            affiliation_to_number[affiliation] = len(affiliation_to_number) + 1
    # BIORXIV info block
    if "email" in author.keys():
        biorxiv.write(author["email"])
    biorxiv.write("\t")
    # Institution
    biorxiv.write(affiliations[0])
    biorxiv.write("\t")
    # Name
    biorxiv.write(author["givennames"])
    biorxiv.write("\t")
    biorxiv.write("\t")
    biorxiv.write(author["familyname"])
    biorxiv.write("\t")
    biorxiv.write("\t")
    biorxiv.write("\t")
    biorxiv.write("\t")
    biorxiv.write("\t")
    if "orcid" in author.keys():
        biorxiv.write(author["orcid"])
    biorxiv.write("\n")
    
biorxiv.close()

for author in authors:
    author["affilcode"] = [affiliation_to_number[affiliation]
                            for affiliation in author["affiliations"]]
    author.pop("affiliations", None)

affiliations = {}
affiliations["authors"] = authors
affiliations["institutions"] = [{"id": v, "name": k} for k, v in sorted(
    affiliation_to_number.items(), key=lambda item: item[1])]

affiliations["metadata"] = {}
affiliations["metadata"]["corresponding"] = []

# Check authorship and correspondance
toadd = True
for author in affiliations["authors"]:
    if "status" in author.keys():
        if "equal" in author["status"]:
            author["affilcode"].append("‡")
            if toadd:
                affiliations["metadata"]["equalcontributions"] = {"id": "‡", "name": "These authors contributed equally to the work"}
                toadd = False
        if "corresponding" in author["status"]:
            affiliations["metadata"]["corresponding"].append({"given": author["givennames"], "family": author["familyname"], "email": author["email"]})

with open("affiliations.json", "w") as outfile:
    json.dump(affiliations, outfile, sort_keys=False,
              indent=4, separators=(',', ': '))
    outfile.write('\n')