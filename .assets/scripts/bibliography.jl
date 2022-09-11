import JSON

references = JSON.parsefile(joinpath(pwd(), "references.json"))

fields_to_drop = [
    "source",
    "abstract",
    "language",
    "accessed",
    "container-title-short",
    "title-short",
    "ISSN",
    "call-number",
    "number-of-pages",
    "ISBN",
    "note",
    "annote",
]

for reference in references
    for field in fields_to_drop
        delete!(reference, field)
    end
end

open("references.json", "w") do json_file
    return JSON.print(json_file, references, 4)
end