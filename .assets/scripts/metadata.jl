import JSON

metadata = JSON.parsefile(joinpath(pwd(), "metadata.json"))

delete!(metadata, "abstract")
abstract = JSON.parsefile(joinpath(pwd(), "abstract.json"))
metadata["abstract"] = abstract

delete!(metadata, "authors")
affiliations = JSON.parsefile(joinpath(pwd(), "affiliations.json"))
metadata["authors"] = affiliations["authors"]
metadata["authorship"] = affiliations["metadata"]
metadata["institutions"] = affiliations["institutions"]

metadata["filename"] = JSON.parsefile(joinpath(pwd(), "filename.json"))["filename"]

# Write the file
open("manuscript-metadata.json", "w") do json_file
    return JSON.print(json_file, metadata, 4)
end