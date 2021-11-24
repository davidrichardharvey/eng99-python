import json


class Film:
    def __init__(self, filepath):
        self.filepath = filepath
        film_info = self._open_json_file()
        self.title = film_info.get("title")
        self.year = film_info.get("release_year")
        self.box_office_usd = film_info.get("box_office_usd_million") * 10**6
        self.ratings = film_info.get("ratings")

    def _open_json_file(self) -> dict:
        with open(self.filepath) as film_file:
            return json.load(film_file)

    def get_average_rating(self) -> float:
        # return the average of all ratings in self.ratings
        # this should work no matter the number of ratings
        # or who they're from
        total = 0
        count = 0
        for rating in self.ratings.values():
            total += rating
            count += 1
        return total / count
        # return sum(rating for rating in self.ratings.values()) / len(self.ratings)


shrek = Film("shrek.json")
print(shrek.title)
print(shrek.year)
print(shrek.get_average_rating())
