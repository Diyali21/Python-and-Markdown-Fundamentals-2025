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
# Q12
# library = [
#     {"title": "Unfogging the Future", "author": "Cassandra Vablatsky"},
#     {"title": "Magical Hieroglyphs and Logograms", "author": "Bathilda Bagshot"},
# ]
# # Expected Task: Use a list comprehension to select books written by Bathilda Bagshot.


# bagshot_books = [book for book in library if book["author"] == "Bathilda Bagshot"]
# print(bagshot_books)

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
# Q16
# wizard = {"name": "Albus Dumbledore", "title": "Headmaster", "house": "Gryffindor"}

# profile = f"{wizard['name']}, the {wizard['title']} of {wizard['house']}"
# print(profile)

# -----------------------------------------------------------------------------------------------
# Q18
ingredients = ["Moonstone", "Silver Dust", "Dragon Blood"]
# Expected Task: For each pair of ingredients, print out the unique potion they produce.

# Your solution here:
# potential_potions = ...

# Combining Moonstone and Silver Dust produces a unique potion.
# Combining Moonstone and Dragon Blood produces a unique potion.
# Combining Silver Dust and Dragon Blood produces a unique potion.

potential_potions = f"""Combining {ingredients[0]} and {ingredients[1]} produces a unique potion
Combining {ingredients[0]} and {ingredients[2]} produces a unique potion
Combining {ingredients[1]} and {ingredients[2]} produces a unique potion
"""

print(potential_potions)

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
