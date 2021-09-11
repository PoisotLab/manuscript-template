import json

with open("metadata.json") as mdfile:
    metadata = json.load(mdfile)

abstract = {}
abstract["abstractdata"] = {}

if type(metadata["abstract"]) == dict:
    abstract["abstractdata"]["structured"] = True
    abstract["abstractdata"]["content"] = [{"key": header, "value": metadata["abstract"][header]} for header in metadata["abstract"]]

if type(metadata["abstract"]) == list:
    abstract["abstractdata"]["itemized"] = True
    abstract["abstractdata"]["content"] = [header for header in metadata["abstract"]]

if type(metadata["abstract"]) == str:
    abstract["abstractdata"]["regular"] = True
    abstract["abstractdata"]["content"] = metadata["abstract"]

with open("abstract.json", "w") as outfile:
    json.dump(abstract, outfile, sort_keys=False,
              indent=4, separators=(',', ': '))
    outfile.write('\n')