import JSON
import Languages
import Dates
import Unicode

metadata = JSON.parsefile(joinpath(pwd(), "metadata.json"))

title = filter(!Unicode.ispunct, lowercase(metadata["title"]))
title_tokens = setdiff(split(title, " "), Languages.stopwords(Languages.English()))
title_placeholder = join(title_tokens[1:min(2, length(title_tokens))], "_")

ms_year = Dates.year(Dates.today())

author_string = ""

if length(metadata["authors"]) == 1
    global author_string = only(metadata["authors"])["familyname"]
elseif length(metadata["authors"]) == 2
    global author_string =
        metadata["authors"][1]["familyname"] * "_and_" *
        metadata["authors"][2]["familyname"]
else
    global author_string =
        metadata["authors"][1]["familyname"] * "_et_al"
end

filename = join([author_string, ms_year, title_placeholder], "_")
filename = filter(x -> !isspace(x), filename)

open("filename", "w") do f
    return write(f, filename)
end

open("filename.json", "w") do f
    return JSON.print(f, Dict(["filename" => filename]), 4)
end
