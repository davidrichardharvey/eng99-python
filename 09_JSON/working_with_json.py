import json

# with open("demo.json") as jsonfile:
#     read_file = jsonfile.read()
#     print(read_file, type(read_file))
#     demo = json.loads(read_file)
#     print(demo)
#     print(type(demo))
#
#     print(demo["Objects"]["Key"])

# Create a Python dict
# with information about
# your favourite film / TV series
film = {
    "title": "Shrek",
    "release_year": 2001,
    "runtime_mins": 90,
    "box_office_usd_million": 487.9,
    "ratings": {
        "IMDb": 0.79,
        "Rotten Tomatoes": 0.88
    },
    "perfect": True,
    "flaws": None
}

# film_json_string = json.dumps(film)
# print(film_json_string)
# print(type(film_json_string))
#
# with open("shrek.json", "w") as shrekfile:
#     shrekfile.write(film_json_string)

with open("shrek2.json", "w") as shrekfile:
    json.dump(film, shrekfile)
