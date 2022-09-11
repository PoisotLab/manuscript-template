import JSON

# Read the metadata
metadata = JSON.parsefile(joinpath(pwd(), "metadata.json"))

authors = metadata["authors"]
affiliation_to_number = Dict{String, Integer}()

for author in authors
    affiliations = author["affiliations"]
    for affiliation in affiliations
        if ~haskey(affiliation_to_number, affiliation)
            affiliation_to_number[affiliation] = length(affiliation_to_number) + 1
        end
    end
end

for author in authors
    author["affilcode"] =
        sort([affiliation_to_number[affiliation] for affiliation in author["affiliations"]])
    delete!(author, "affiliations")
end

affiliations = Dict{String, Any}()
affiliations["authors"] = authors
affiliations["institutions"] = []
while ~isempty(affiliation_to_number)
    id, idx = findmin(collect(values(affiliation_to_number)))
    name = collect(keys(affiliation_to_number))[idx]
    delete!(affiliation_to_number, name)
    push!(affiliations["institutions"], Dict(["id" => id, "name" => name]))
end