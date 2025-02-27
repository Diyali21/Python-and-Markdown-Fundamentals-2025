# movies = [
#     {"title": "Inception", "ratings": [5, 4, 5, 4, 5]},
#     {"title": "Interstellar", "ratings": [5, 5, 4, 5, 4]},
#     {"title": "Dunkirk", "ratings": [4, 4, 4, 3, 4]},
#     {"title": "The Dark Knight", "ratings": [5, 5, 5, 5, 5]},
#     {"title": "Memento", "ratings": [4, 5, 4, 5, 4]},
# ]

# # [{**movies, *movie.get("average_rating", sum(movie["ratings"]) / len(movies))} for movie in movies]

# # print(
# #     [{**movie, "avg_rating": sum(movie["ratings"]) / len(movies)} for movie in movies]
# # )

# print(
#     [movie["title"] for movie in movies if sum(movie["ratings"]) / len(movies) >= 4.6]
# )

# Task
# Creating the below dictionary with for loop

# {"1": 1, "2": 4, "3": 9, "4": 16, "5": 25}

for i in range(1, 6):
    square = {f"{i}": i * i}
    print(square)
