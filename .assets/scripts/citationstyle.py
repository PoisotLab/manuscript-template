import json

with open("metadata.json") as mdfile:
    metadata = json.load(mdfile)

# 

from urllib import request

local_file = '.assets/citationstyle.csl'

try:
    remote_url = "https://raw.githubusercontent.com/citation-style-language/styles/master/%s.csl" % metadata["citationstyle"]
    request.urlretrieve(remote_url, local_file)
except request.HTTPError:
    remote_url = "https://raw.githubusercontent.com/citation-style-language/styles/master/dependent/%s.csl" % metadata["citationstyle"]
    request.urlretrieve(remote_url, local_file)