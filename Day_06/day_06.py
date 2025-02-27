# inventory = [
#     {"name": "Apple 🍎", "quantity": 30, "price": 0.5},
#     {"name": "Banana 🍌", "quantity": 20, "price": 0.2},
# ]

# for i in range(len(inventory)):
#     print(inventory[i].get("name"))

# captain_america = {
#     "name": "Steve Rogers 🦸‍♂️",
#     "age": 100,
#     "height": 185,
#     "address": {"city": "Brooklyn", "country": "US"},
# }


# spiderman = {
#     "name": "Peter Parker",
#     "age": 18,
#     "team_name": "Avengers",
#     "team": ["Iron Man", "Thor", "Hulk", "Captain America"],
# }

# hulk = {
#     "name": "Bruce Banner",
#     "age": 35,
# }

# heroes = [captain_america, spiderman, hulk]

# for hero in heroes:
#     city = hero.get("address", {}).get("city")
#     if city != None:
#         print(f"{hero['name']} lives in {city}")
#     else:
#         print(f"{hero['name']} location is Top Secret 🔒")

# employees = [
#     {"name": "Chelo", "experience": 2},
#     {"name": "Diyali"},
#     {"name": "Luvuyo"},
#     {"name": "Jevan", "experience": 1},
# ]


# for employee in employees:
#     employee["experience"] = employee.get("experience", 0) + 1
# print(employees)

# Task 2.2
# # Senior 5 or more, Mid-Level 3 to 5, Junior < 3
# employees = [
#     {"name": "Chelo", "experience": 4},
#     {"name": "Diyali"},
#     {"name": "Luvuyo"},
#     {"name": "Jevan", "experience": 2},
# ]

# for employee in employees:
#     employee["experience"] = employee.get("experience", 0) + 1

#     if employee["experience"] >= 5:
#         employee["status"] = employee.get("status", "Senior")
#     elif 3 <= employee["experience"] < 5:
#         employee["status"] = employee.get("status", "Mid-Level")
#     else:
#         employee["status"] = employee.get("status", "Junior")

# print(employees)

# # Output
# # employees = [
# #     {"name": "Chelo", "experience": 5, "status": "Senior"},
# #     {"name": "Diyali", "status": "Junior", "experience": 1},
# #     {"name": "Luvuyo", "status": "Junior", "experience": 1},
# #     {"name": "Jevan", "status": "Mid-Level", "experience": 3},
# # ]


# avengers = [
#     "Hulk",
#     "Iron man",
#     "Black widow",
#     "Captain america",
#     "Spider man",
#     "Thor",
# ]

# avengers_letter_count = []

# # Loop list & method
# for i in range(len(avengers)):
#     avengers_letter_count.append(len(avengers[i]))
# print(avengers_letter_count)

# letter_count = [
#     avengers_letter_count.append(len(avengers[i])) for i in range(len(avengers))
# ]
# print(letter_count)

# points = [(3, 4), (6, 12), (10, 13)]

# distances = []
# # for x, y in points:  # unpacking
# #     distance = round((x**2 + y**2) ** 0.5, 2)
# #     distances.append(distance)

# distances = [round((x**2 + y**2) ** 0.5, 2) for x, y in points]

# print(distances)

# Task - With List Comp

# nums = [7, 44, 90, 6, 75, 10]

# # Output
# # ["Odd", "Even", "Even", "Even", "Odd", "Even"]


# print(["Odd" if num % 2 != 0 else "Even" for num in nums])


# - Prompt for the product name, additional quantity, and new price.
# - Loop through the inventory; if the product exists, update its quantity and price.

# **Example Scenario:**

# - **Initial Inventory:**

# inventory = [
#     {"name": "Apple 🍎", "quantity": 30, "price": 0.5},
#     {"name": "Banana 🍌", "quantity": 20, "price": 0.2},
# ]

# # - **User Input:**
# #   ```
# #   Enter product name to update: Apple 🍎
# #   Enter additional quantity: 40
# #   Enter new price: 0.4
# #   ```
# # - **Expected Output:**
# #   ```
# #   Updated Apple 🍎 successfully! 🎉
# #   Updated Inventory: [{'name': 'Apple 🍎', 'quantity': 70, 'price': 0.4}, {'name': 'Banana 🍌', 'quantity': 20, 'price': 0.2}]


# name = input("Enter product name to update: ")
# qty = int(input("Enter additional quantity: "))
# price = float(input("Enter new price: "))

# for product in inventory:
#     product_name = product.get("name")
#     if name == product_name:
#         print(f"Updated {product['name']} successfully! 🎉")
#         product["quantity"] += qty
#         product["price"] = price
# print(f"Updated Inventory: {inventory}")
