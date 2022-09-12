import JSON

# Read the metadata
metadata = JSON.parsefile(joinpath(pwd(), "metadata.json"))

authors = metadata["authors"]
affiliation_to_number = Dict{String, String}()

for author in authors
    affiliations = author["affiliations"]
    for affiliation in affiliations
        if ~haskey(affiliation_to_number, affiliation)
            affiliation_to_number[affiliation] = "$(length(affiliation_to_number) + 1)"
        end
    end
end

for author in authors
    author["affiliation"] =
        sort(
            String[
                "$(affiliation_to_number[affiliation])" for affiliation in author["affiliations"]
            ],
        )
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

affiliations["metadata"] = Dict()
affiliations["metadata"]["corresponding"] = []

add_equal_sign = true
for author in affiliations["authors"]
    if haskey(author, "status")
        if "equal" in author["status"]
            push!(author["affiliation"], "‡")
            if add_equal_sign
                affiliations["metadata"]["equal"] =
                    Dict(["id" => "‡", "name" => "Equal contributions"])
                global add_equal_sign = false
            end
        end
        if "corresponding" in author["status"]
            push!(affiliations["metadata"]["corresponding"],
                Dict([
                    "given" => author["givennames"],
                    "family" => author["familyname"],
                    "email" => author["email"],
                ]),
            )
        end
    end
end

# Write the file
open("affiliations.json", "w") do json_file
    return JSON.print(json_file, affiliations, 4)
end
