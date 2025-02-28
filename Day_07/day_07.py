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


# guests = [
#     {"name": "Alice", "age": 25, "code": "VIP123"},
#     {"name": "Bob", "age": 17, "code": "VIP123"},
#     {"name": "Charlie", "age": 30, "code": "VIP123"},
#     {"name": "Dave", "age": 22, "code": "GUEST"},
#     {"name": "Eve", "age": 29, "code": "VIP123"},
# ]


# blacklist = ["Dave", "Eve"]

# # Task
# # People who are 21 or above and VIP123
# # Blacklist are not allowed


# PASS_CODE = "VIP123"

# guestlist = []  # ?

# # for guest in guests:
# #     if (
# #         guest["age"] >= 21
# #         and guest["code"] == "VIP123"
# #         and guest["name"] not in blacklist
# #     ):
# #         guestlist.append(guest["name"])
# # print(guestlist)


# print(
#     [
#         guest["name"]
#         for guest in guests
#         if guest["age"] >= 21
#         and guest["code"] == "VIP123"
#         and guest["name"] not in blacklist
#     ]
# )


# Use nested dictionary comprehension to create a dictionary of restaurants with items under $10
restaurant_menus = [
    {
        "restaurant": "Italian Place",
        "menu": {"🍕": 12.99, "🍝": 10.99, "🥖": 3.99, "🥗": 7.99},
    },
    {
        "restaurant": "Burger Joint",
        "menu": {"🍔": 8.99, "🍟": 3.99, "🥤": 1.99, "🍦": 4.99},
    },
    {
        "restaurant": "Sushi Bar",
        "menu": {"🍣": 15.99, "🍜": 12.99, "🍙": 6.99, "🍶": 9.99},
    },
    {
        "restaurant": "Health Spot",
        "menu": {"🥗": 9.99, "🥙": 8.99, "🥑": 4.99, "🥝": 3.99},
    },
]

# Expected output
# Output
# {
#     "Italian Place": {"🥖": 3.99, "🥗": 7.99},
#     "Burger Joint": {"🍔": 8.99, "🍟": 3.99, "🥤": 1.99, "🍦": 4.99},
#     "Sushi Bar": {"🍙": 6.99},
#     "Health Spot": {"🥙": 8.99, "🥑": 4.99, "🥝": 3.99},
# }

# r_menu = {}
# for menu in restaurant_menus:
#     key = menu["restaurant"]
#     value = {}

#     for i in menu["menu"]:
#         if menu["menu"][i] < 10:
#             value[i] = menu["menu"][i]
#     r_menu[key] = value

# print(r_menu)

# output = {}
# prices = {}
# for item in restaurant_menus:
#     restaurant = item["restaurant"]

#     for key, val in item["menu"].items():
#         if val < 10:
#             prices = {key, val}
#         output[restaurant] = prices

# print(output)

affordable_menu = {}

for place in restaurant_menus:
    affordable_menu[place["restaurant"]] = place["menu"]

    cheap_items = {}

    for item, price in place["menu"].items():
        if price <= 10:
            cheap_items[item] = price
    affordable_menu[place["restaurant"]] = cheap_items

print(affordable_menu)
