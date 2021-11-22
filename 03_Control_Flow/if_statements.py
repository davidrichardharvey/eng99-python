film_rating = "12a"
# U, PG, 12, 12A, 15, 18
# Treat 12 and 12A as the same

if film_rating.upper() == "U":
    print("Suitable for all ages")
elif film_rating.upper() == "PG":
    print("Parental Guidance advised")
elif film_rating.upper() in ("12", "12A"):
    print("You should be older than 12 years old to watch")
elif film_rating == "15":
    print("You need to be 15 or older")
else:
    print("Please check the film rating is correct")