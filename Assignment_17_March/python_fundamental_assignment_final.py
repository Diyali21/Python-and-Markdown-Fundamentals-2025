# Exercise 1: Data Sorting and Ranking
students = [
    {"name": "Alice", "grade": 88},
    {"name": "Bob", "grade": 75},
    {"name": "Charlie", "grade": 93},
]


# def sort_students(students):
#     sorted_students = list(
#         sorted(students, key=lambda student: student["grade"], reverse=True)
#     )

#     rank = 1

#     for student in sorted_students:
#         student["rank"] = rank
#         rank += 1

#     print(sorted_students)


# sort_students(students)


# Way 1
# sorted_students = list(
#     sorted(students, key=lambda student: student["grade"], reverse=True)
# )

# rank = 1

# for student in sorted_students:
#     student["rank"] = rank
#     rank += 1

# --------------------------------------------------------------------------------------------------------
# Ex 2
# employees = [{"id": 1, "name": "Alice"}, {"id": 2, "name": "Bob"}]
# salaries = [{"id": 1, "salary": 50000}, {"id": 2, "salary": 60000}]


# def merge_list_dict():
#     merged_data = []

#     for employee in employees:
#         merged_dict = {}
#         for salary in salaries:
#             if employee["id"] == salary["id"]:
#                 merged_dict["id"] = employee["id"]
#                 merged_dict["name"] = employee["name"]
#                 merged_dict["salary"] = salary["salary"]
#                 merged_data.append(merged_dict)

#     return merged_data


# print(merge_list_dict())
# --------------------------------------------------------------------------------------------------------

# Ex 3
# products = [
#     {"id": 1, "category": "Electronics", "price": 850},
#     {"id": 2, "category": "Furniture", "price": 1200},
#     {"id": 3, "category": "Electronics", "price": 400},
# ]

# # First way
# def electronics1():
#     for product in products:
#         if product["category"] == "Electronics" and product["price"] < 500:
#             print(product)


# electronics1()

# # Second way (Simplified)
# def electronics2():
#     filtered_products = [
#         product
#         for product in products
#         if product["category"] == "Electronics" and product["price"] < 500
#     ]
#     return filtered_products


# print(electronics2())

# --------------------------------------------------------------------------------------------------------
# Ex 4
# Q4

# orders = [
#     {
#         "order_id": 1,
#         "items": [{"product": "A", "quantity": 2}, {"product": "B", "quantity": 3}],
#     },
#     {
#         "order_id": 2,
#         "items": [{"product": "A", "quantity": 1}, {"product": "C", "quantity": 1}],
#     },
# ]


# def prod_qty(orders):
#     product_quantities = {}

#     for item in orders:
#         for product in item["items"]:
#             prod_name = product["product"]
#             qty = product["quantity"]

#             if prod_name in product_quantities.keys():
#                 product_quantities[prod_name] += qty
#             else:
#                 product_quantities[prod_name] = qty
#     print(product_quantities)


# prod_qty(orders)


# --------------------------------------------------------------------------------------------------------
# Ex 5
# transactions = [
#     {"date": "2021-01-01", "amount": 100, "category": "Food"},
#     {"date": "2021-01-01", "amount": 200, "category": "Transport"},
#     {"date": "2021-01-02", "amount": 150, "category": "Food"},
# ]


# def cat_total(transactions):
#     category_totals = {}

#     for transaction in transactions:
#         category = transaction["category"]
#         amount = transaction["amount"]

#         if category in category_totals.keys():
#             category_totals[category] += amount
#         else:
#             category_totals[category] = amount
#     print(category_totals)


# cat_total(transactions)

# -----------------------------------------------------------------------------------------------
# Q6

# sales = [
#     {"salesperson": "Alice", "amount": 200},
#     {"salesperson": "Bob", "amount": 150},
#     {"salesperson": "Alice", "amount": 100},
# ]


# def sales_person(sales):
#     sales_by_person = {}

#     for sale in sales:
#         salesperson = sale["salesperson"]
#         amount = sale["amount"]

#         if salesperson in sales_by_person.keys():
#             sales_by_person[salesperson] += amount
#         else:
#             sales_by_person[salesperson] = amount
#     print(sales_by_person)


# sales_person(sales)


# -----------------------------------------------------------------------------------------------
# Q7
# spells = [("Lumos", 5), ("Obliviate", 10), ("Expelliarmus", 7)]


# def spell_sort(spells):
#     sorted_spells = list(sorted(spells, key=lambda spell: spell[1], reverse=True))
#     print(sorted_spells)


# spell_sort(spells)

# -----------------------------------------------------------------------------------------------
# Q8
# ingredients = ["Wolfsbane", "Eye of Newt", "Dragon Scale"]


# def three_grams(ingredients):
#     formatted_ingredients = list(map(lambda name: name + ": 3 grams", ingredients))
#     print(formatted_ingredients)


# three_grams(ingredients)

# -----------------------------------------------------------------------------------------------
# Q9
# books = [
#     {"title": "A History of Magic", "pages": 100},
#     {"title": "Magical Drafts and Potions", "pages": 150},
# ]


# def format_titles(books):
#     filtered_titles = list(filter(lambda book: book["pages"] > 120, books))
#     formatted_titles = list(map(lambda book: book["title"].upper(), filtered_titles))

#     print(formatted_titles)


# format_titles(books)

# -----------------------------------------------------------------------------------------------
# Q10


# class WizardDuel:
#     def __init__(self, name1, name2, health1, health2):
#         self.name1 = name1
#         self.name2 = name2
#         self.health1 = health1
#         self.health2 = health2

#     def cast_spell(self, name, points):
#         if self.name1 == name:
#             self.health1 -= points

#         if self.name2 == name:
#             self.health2 -= points

#     def get_winner(self):
#         if self.health1 > self.health2:
#             return f"After a duel between {self.name1} and {self.name2}, {self.name1} wins with {self.health1} health points left."
#         elif self.health2 > self.health1:
#             return f"After a duel between {self.name1} and {self.name2}, {self.name2} wins with {self.health2} health points left."
#         else:
#             return (
#                 f"After a duel between {self.name1} and {self.name2}, there was a tie."
#             )


# # Example usage:
# duel = WizardDuel("Harry", "Draco", 50, 40)
# duel.cast_spell("Harry", 10)
# duel.cast_spell("Draco", 5)
# winner = duel.get_winner()
# print(winner)

# # Output: After a duel between Harry and Draco, Harry wins with 10 health points left.


# -----------------------------------------------------------------------------------------------
# # Q11
# class PotionError(Exception):
#     def __init__(self, *args: object):
#         super().__init__(*args)


# def brew_potion(potion_name, ingredients):
#     correct_ingredients = ["Rose Petal", "Unicorn Hair"]

#     for ingredient in ingredients:
#         if ingredient not in correct_ingredients:
#             raise PotionError(
#                 f"'{ingredient}' is not a valid ingredient for the {potion_name}."
#             )

#     print(f"All ingredients are valid ingredients")


# try:
#     brew_potion("Love Potion", ["Rose Petal", "Unicorn Hair", "Eye of Newt"])
# except PotionError as e:
#     print(f"Caught PotionError: {e}")

# -----------------------------------------------------------------------------------------------

# Q12

# library = [
#     {"title": "Unfogging the Future", "author": "Cassandra Vablatsky"},
#     {"title": "Magical Hieroglyphs and Logograms", "author": "Bathilda Bagshot"},
# ]


# def bathilda_books(library):
#     bagshot_books = [book for book in library if book["author"] == "Bathilda Bagshot"]
#     print(bagshot_books)


# bathilda_books(library)

# -----------------------------------------------------------------------------------------------
# Q13

# house_points = [
#     {"house": "Gryffindor", "points": 35},
#     {"house": "Slytherin", "points": 50},
#     {"house": "Gryffindor", "points": 60},
#     {"house": "Slytherin", "points": 40},
# ]


# def house_total(house_points):
#     house_totals = {}

#     for house_point in house_points:
#         house = house_point["house"]
#         points = house_point["points"]

#         if house in house_totals:
#             house_totals[house] += points
#         else:
#             house_totals[house] = points

#     print(house_totals)


# house_total(house_points)

# -----------------------------------------------------------------------------------------------
# Q14


# class MagicalCreature:
#     def __init__(self, creature):
#         self.creature = creature


# class Dragon(MagicalCreature):
#     def __init__(self, creature):
#         super().__init__(creature)

#     def sound(self):
#         print(f"{self.creature} the Dragon says: Roar!")


# class Unicorn(MagicalCreature):
#     def __init__(self, creature):
#         super().__init__(creature)

#     def sound(self):
#         print(f"{self.creature} the Unicorn says: Neigh!")


# # Example usage:
# dragon = Dragon("Norwegian Ridgeback")
# unicorn = Unicorn("Silver-maned")
# dragon.sound()
# unicorn.sound()

# -----------------------------------------------------------------------------------------------
# Q15
# artifacts = [
#     {"name": "Cloak of Invisibility", "age": 657, "power": 9.5},
#     {"name": "Elder Wand", "age": 1000, "power": 10},
#     {"name": "Resurrection Stone", "age": 800, "power": 7},
# ]


# def sort_artifact(artifacts):
#     sorted_artifacts = list(sorted(artifacts, key=lambda artifact: artifact["age"]))
#     print(sorted_artifacts)


# sort_artifact(artifacts)

# -----------------------------------------------------------------------------------------------
# Q16
# wizard = {"name": "Albus Dumbledore", "title": "Headmaster", "house": "Gryffindor"}


# def profile(wizard):
#     profile = f"{wizard['name']}, the {wizard['title']} of {wizard['house']}"
#     print(profile)


# profile(wizard)

# -----------------------------------------------------------------------------------------------
# Q17

# adopters = [("Harry", "Phoenix"), ("Hermione", "House Elf")]
# creatures = [("Fawkes", "Phoenix"), ("Dobby", "House Elf"), ("Buckbeak", "Hippogriff")]


# def match(adopters, creatures):
#     matches = []

#     for adopter in adopters:
#         filtered_creatures = filter(
#             lambda creature: adopter[1] == creature[1], creatures
#         )
#         map_creatures = " ".join(
#             list(map(lambda creature: creature[0], filtered_creatures))
#         )

#         matches.append((adopter[0], map_creatures))

#     print(matches)


# match(adopters, creatures)
# -----------------------------------------------------------------------------------------------

# Q18

# ingredients = ["Moonstone", "Silver Dust", "Dragon Blood"]


# def different_potions(ingredients):
#     for i in range(len(ingredients) - 1):
#         for j in range(i + 1, len(ingredients)):
#             potiential_potions = f"Combining {ingredients[i]} and {ingredients[j]} produces a unique potion"
#             print(potiential_potions)


# different_potions(ingredients)

# -----------------------------------------------------------------------------------------------
# Q19
# data = [
#     {"id": 1, "name": "Item 1", "tags": ["tag1", "tag2"]},
#     {"id": 2, "name": "Item 2", "tags": ["tag2", "tag3"]},
#     {"id": 3, "name": "Item 3", "tags": ["tag1", "tag3"]},
# ]


# def tag4(data, tag_no):
#     for info in data:
#         if tag_no in info["tags"]:
#             info["tags"].append("tag4")
#         print(info)


# tag4(data, "tag1")

# -----------------------------------------------------------------------------------------------
# # Q20
# tasks = [
#     {"id": 1, "priority": "High", "completed": False},
#     {"id": 2, "priority": "Low", "completed": True},
#     {"id": 3, "priority": "Medium", "completed": False},
# ]


# def sort_task(tasks, key_sort):
#     sorted_tasks = list(sorted(tasks, key=key_sort))
#     print(sorted_tasks)


# sort_task(tasks, lambda task: task["completed"])
