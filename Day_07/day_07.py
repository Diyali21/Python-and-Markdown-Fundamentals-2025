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

# for i in range(1, 6):
#     square = {f"{i}": i * i}
#     print(square)

# num = [{i: "odd" if i % 2 != 0 else "even"} for i in range(1,11)]

# fruits = {"apple": 1.2, "banana": 2.5, "orange": 3.0, "kiwi": 4.0}

# fruits_above_two = {key: val for key, val in fruits.items() if val > 2}
# print(fruits_above_two)

# employees = [
#     {"id": 101, "name": "Alice", "age": 30},
#     {"id": 102, "name": "Bob", "age": 25},
#     {"id": 103, "name": "Charlie", "age": 35},
# ]

# emp = {
#     employee["id"]: employee["age"] for employee in employees if employee["age"] > 28
# }

# print(emp)


# Task
# Remove the duplicates
# colors = ["🔴 red", "🔵 blue", "🔴 red", "🟢 green", "💗 pink", "🔵 blue"]


# "🔴 red", "🔵 blue", "🟢 green", "💗 pink"

# # Easy
# print(set(colors))

# # Hard
# c = set()
# for color in colors:
#     c.add(color)
# print(c)


guests = [
    {"name": "Alice", "age": 25, "code": "VIP123"},
    {"name": "Bob", "age": 17, "code": "VIP123"},
    {"name": "Charlie", "age": 30, "code": "VIP123"},
    {"name": "Dave", "age": 22, "code": "GUEST"},
    {"name": "Eve", "age": 29, "code": "VIP123"},
]


blacklist = ["Dave", "Eve"]

# Task
# People who are 21 or above and VIP123
# Blacklist are not allowed


PASS_CODE = "VIP123"

guestlist = []  # ?

# for guest in guests:
#     if (
#         guest["age"] >= 21
#         and guest["code"] == "VIP123"
#         and guest["name"] not in blacklist
#     ):
#         guestlist.append(guest["name"])
# print(guestlist)


print(
    [
        guest["name"]
        for guest in guests
        if guest["age"] >= 21
        and guest["code"] == "VIP123"
        and guest["name"] not in blacklist
    ]
)
