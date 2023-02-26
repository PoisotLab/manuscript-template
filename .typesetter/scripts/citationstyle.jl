import Downloads
import JSON

metadata = JSON.parsefile(joinpath(pwd(), "metadata.json"))

local_file = joinpath(pwd(), ".assets", "citationstyle.csl")

try
    remote_url = "https://raw.githubusercontent.com/citation-style-language/styles/master/$(metadata["citationstyle"]).csl"
    Downloads.download(remote_url, local_file)
catch err
    remote_url = "https://raw.githubusercontent.com/citation-style-language/styles/master/dependent/$(metadata["citationstyle"]).csl"
    Downloads.download(remote_url, local_file)
end