# Q1
# students = [
#     {"name": "Alice", "grade": 88},
#     {"name": "Bob", "grade": 75},
#     {"name": "Charlie", "grade": 93},
# ]

# # sorted_spells = list(sorted(spells, key=lambda spell: spell[1], reverse=True))

# sorted_students = list(
#     sorted(students, key=lambda student: student["grade"], reverse=True)
# )
# for i in range(len(sorted_students)):
#     sorted_students[i]["rank"] = i + 1


# # Way 1
# # rank = 1

# # for student in sorted_students:
# #     student["rank"] = rank
# #     rank += 1

# print(sorted_students)

# -----------------------------------------------------------------------------------------------
# Q2:

# employees = [{"id": 1, "name": "Alice"}, {"id": 2, "name": "Bob"}]
# salaries = [{"id": 1, "salary": 50000}, {"id": 2, "salary": 60000}]


# def merge_list_dict():
#     new_list = []

#     for employee in employees:
#         new_dict = {}
#         for salary in salaries:
#             if employee["id"] == salary["id"]:
#                 new_dict["id"] = employee["id"]
#                 new_dict["name"] = employee["name"]
#                 new_dict["salary"] = salary["salary"]
#                 new_list.append(new_dict)

#     return new_list


# print(merge_list_dict())

# -----------------------------------------------------------------------------------------------
# Q3

# products = [
#     {"id": 1, "category": "Electronics", "price": 850},
#     {"id": 2, "category": "Furniture", "price": 1200},
#     {"id": 3, "category": "Electronics", "price": 400},
# ]


# def electronics1():
#     for product in products:
#         if product["category"] == "Electronics" and product["price"] < 500:
#             print(product)


# electronics1()


# def electronics2():
#     elect = [
#         product
#         for product in products
#         if product["category"] == "Electronics" and product["price"] < 500
#     ]
#     return elect


# print(electronics2())

# -----------------------------------------------------------------------------------------------
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

# product_qty = {}

# for item in orders:
#     for product in item["items"]:
#         prod_name = product["product"]
#         qty = product["quantity"]

#         if prod_name in product_qty:
#             product_qty[prod_name] += qty
#         else:
#             product_qty[prod_name] = qty

# print(product_qty)

# -----------------------------------------------------------------------------------------------
# Q5
# transactions = [
#     {"date": "2021-01-01", "amount": 100, "category": "Food"},
#     {"date": "2021-01-01", "amount": 200, "category": "Transport"},
#     {"date": "2021-01-02", "amount": 150, "category": "Food"},
# ]

# category_totals = {}

# for transaction in transactions:
#     category = transaction["category"]
#     amount = transaction["amount"]

#     if category in category_totals:
#         category_totals[category] += amount
#     else:
#         category_totals[category] = amount

# print(category_totals)

# -----------------------------------------------------------------------------------------------
# Q6

# sales = [
#     {"salesperson": "Alice", "amount": 200},
#     {"salesperson": "Bob", "amount": 150},
#     {"salesperson": "Alice", "amount": 100},
# ]

# sales_amount = {}

# for sale in sales:
#     salesperson = sale["salesperson"]
#     amount = sale["amount"]

#     if salesperson in sales_amount.keys():
#         sales_amount[salesperson] += amount
#     else:
#         sales_amount[salesperson] = amount


# print(sales_amount)

# -----------------------------------------------------------------------------------------------
# Q7
# spells = [("Lumos", 5), ("Obliviate", 10), ("Expelliarmus", 7)]

# sorted_spells = list(sorted(spells, key=lambda spell: spell[1], reverse=True))

# print(sorted_spells)

# -----------------------------------------------------------------------------------------------
# Q8
# ingredients = ["Wolfsbane", "Eye of Newt", "Dragon Scale"]

# formatted_ingredients = list(map(lambda name: name + ": 3 grams", ingredients))
# print(formatted_ingredients)

# -----------------------------------------------------------------------------------------------
# Q9
# books = [
#     {"title": "A History of Magic", "pages": 100},
#     {"title": "Magical Drafts and Potions", "pages": 150},
# ]
# # Expected Task: Filter books with more than 120 pages and format their titles to uppercase.

# filtered_titles = list(filter(lambda book: book["pages"] > 120, books))
# formatted_titles = list(map(lambda book: book["title"].upper(), filtered_titles))

# print(formatted_titles)

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

### Expected Output
# After a duel between Harry and Draco, Harry wins with 10 health points left.

# -----------------------------------------------------------------------------------------------
# # Q11
# class PotionError(Exception):
#     pass


# def brew_potion(potion_name, ingredients):
#     correct_ingredients = ["Rose Petal", "Unicorn Hair"]

#     for ingredient in ingredients:
#         if ingredient not in correct_ingredients:
#             raise PotionError(
#                 f"'{ingredient}' is not a valid ingredient for the Love Potion."
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
# # Expected Task: Use a list comprehension to select books written by Bathilda Bagshot.


# bagshot_books = [book for book in library if book["author"] == "Bathilda Bagshot"]
# print(bagshot_books)

# -----------------------------------------------------------------------------------------------
# Q13
# house_points = [
#     {"house": "Gryffindor", "points": 35},
#     {"house": "Slytherin", "points": 50},
#     {"house": "Gryffindor", "points": 60},
#     {"house": "Slytherin", "points": 40},
# ]
# Expected Task: Aggregate points for each house and print the total.

# Your solution here:
# house_totals = ...

# print(house_totals)

# house_total_points = {}

# for house_point in house_points:
#     house = house_point["house"]
#     points = house_point["points"]

#     if house in house_total_points:
#         house_total_points[house] += points
#     else:
#         house_total_points[house] = points

# print(house_total_points)


### Expected Output
# {
#     "Gryffindor": 95,
#     "Slytherin": 90
# }

# -----------------------------------------------------------------------------------------------
# Q14

# Implement a class hierarchy for magical creatures where each subclass overrides a common method.

# Setup Code
# class MagicalCreature:
#     # Your implementation here
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
# dragon.sound()  # Should print "Roar" output - Norwegian Ridgeback the Dragon says: Roar!
# unicorn.sound()  # Should print "Neigh" output - Silver-maned the Unicorn says: Neigh!

# -----------------------------------------------------------------------------------------------
# Q15
# artifacts = [
#     {"name": "Cloak of Invisibility", "age": 657, "power": 9.5},
#     {"name": "Elder Wand", "age": 1000, "power": 10},
#     {"name": "Resurrection Stone", "age": 800, "power": 7},
# ]
# Expected Task: Sort the artifacts first by age, then by power, using a lambda function.

# Your solution here:
# sorted_artifacts = ...

# Expected Output
# print(sorted_artifacts)

# sorted_artifacts = list(sorted(artifacts, key=lambda artifact: artifact["age"]))
# print(sorted_artifacts)

# [
#     {"name": "Cloak of Invisibility", "age": 657, "power": 9.5},
#     {"name": "Resurrection Stone", "age": 800, "power": 7},
#     {"name": "Elder Wand", "age": 1000, "power": 10}
# ]

# -----------------------------------------------------------------------------------------------
# Q16
# wizard = {"name": "Albus Dumbledore", "title": "Headmaster", "house": "Gryffindor"}

# profile = f"{wizard['name']}, the {wizard['title']} of {wizard['house']}"
# print(profile)

# -----------------------------------------------------------------------------------------------
# Q17
# adopters = [("Harry", "Phoenix"), ("Hermione", "House Elf")]
# creatures = [("Fawkes", "Phoenix"), ("Dobby", "House Elf"), ("Buckbeak", "Hippogriff")]

# adopt_creature = []

# for adopter in adopters:
#     filtered = filter(lambda creature: adopter[1] == creature[1], creatures)
#     map_ac = " ".join(list(map(lambda creature: creature[0], filtered)))

#     adopt_creature.append((adopter[0], map_ac))

# print(adopt_creature)
# -----------------------------------------------------------------------------------------------

# Q18
# ingredients = ["Moonstone", "Silver Dust", "Dragon Blood"]
# Expected Task: For each pair of ingredients, print out the unique potion they produce.

# Your solution here:
# potential_potions = ...

# Combining Moonstone and Silver Dust produces a unique potion.
# Combining Moonstone and Dragon Blood produces a unique potion.
# Combining Silver Dust and Dragon Blood produces a unique potion.

# potential_potions = f"""Combining {ingredients[0]} and {ingredients[1]} produces a unique potion
# Combining {ingredients[0]} and {ingredients[2]} produces a unique potion
# Combining {ingredients[1]} and {ingredients[2]} produces a unique potion
# """

# print(potential_potions)

# -----------------------------------------------------------------------------------------------
# Q19
# data = [
#     {"id": 1, "name": "Item 1", "tags": ["tag1", "tag2"]},
#     {"id": 2, "name": "Item 2", "tags": ["tag2", "tag3"]},
#     {"id": 3, "name": "Item 3", "tags": ["tag1", "tag3"]},
# ]
# # Expected Task: For each item, add a new tag "tag4" only if "tag1" is present in the tags list.


# for info in data:
#     if "tag1" in info["tags"]:
#         info["tags"].append("tag4")
#     print(info)

# -----------------------------------------------------------------------------------------------
# Q20
# tasks = [
#     {"id": 1, "priority": "High", "completed": False},
#     {"id": 2, "priority": "Low", "completed": True},
#     {"id": 3, "priority": "Medium", "completed": False},
# ]
# Expected Task: Sort the tasks by "completed" status (False first) and then by priority ("High", "Medium", "Low").

# Your solution here:
# sorted_tasks = ...

# Expected Output
# print(sorted_tasks)

# sorted_false = list(sorted(tasks, key=lambda task: task["completed"]))
# print(sorted_false)

# [
#     {"id": 1, "priority": "High", "completed": False},
#     {"id": 3, "priority": "Medium", "completed": False},
#     {"id": 2, "priority": "Low", "completed": True}
# ]
