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
