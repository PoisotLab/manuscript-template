import JSON

# Read the metadata
metadata = JSON.parsefile(joinpath(pwd(), "metadata.json"))

# Dispatch on abstract type
function format_abstract(abstract::Dict{String, Any})
    data = Dict{String, Any}(["structured" => true])
    data["content"] = [Dict(["key" => key, "value" => value]) for (key, value) in abstract]
    return data
end

function format_abstract(abstract::String)
    data = Dict{String, Any}(["regular" => true])
    data["content"] = abstract
    return data
end

function format_abstract(abstract::Vector{T}) where {T}
    data = Dict{String, Any}(["itemized" => true])
    data["content"] = [element for element in abstract]
    return data
end

# Write the file
open("abstract.json", "w") do json_file
    return JSON.print(json_file, format_abstract(metadata["abstract"]), 4)
end
