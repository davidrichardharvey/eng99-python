# d = {
#     "course": "Engineering 99",
#     "stream": "DevOps",
#     "number of trainees": 11
# }
#
# print(d, type(d))
#
# # Access a value
# print(d["stream"])
# print(d.get("stream"))
#
# # Change a value
# # d["stream"] = "Data Engineering"
# d["length_weeks"] = 8
# # d.update({"stream": "Data Eng", "length_weeks": 8})
# print(d)
#
# # Create a dictionary for your favourite film


pulp_fiction = {
    "director": "Quentin Tarantino",
    "release date": "21 October 1994",
    "budget": "8.5m"
}
print(pulp_fiction)

pulp_fiction["main cast"] = {}
print(pulp_fiction)

pulp_fiction["main cast"].update(
    {"Uma Thurman": "3.5m"}
)
print(pulp_fiction)

director = pulp_fiction.pop("director")
print(pulp_fiction)

print(director)