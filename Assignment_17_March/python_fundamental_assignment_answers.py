# Exercise 1: Data Sorting and Ranking
# Setup Code
from math import prod

students = [
    {"name": "Alice", "grade": 88},
    {"name": "Bob", "grade": 75},
    {"name": "Charlie", "grade": 93},
]
# Expected Task: Sort the list of dictionaries by grade in descending order and add a "rank" key to each dictionary based on the sorting.

# Your solution here:
# sorted_students = ...

# Expected Output
# print(sorted_students)


# Exercise 2: Merging Data from Two Lists
employees = [{"id": 1, "name": "Alice"}, {"id": 2, "name": "Bob"}]
salaries = [{"id": 1, "salary": 50000}, {"id": 2, "salary": 60000}]


def merge_list_dict(employees, salaries):
    new_list = []

    for employee in employees:
        new_dict = {}
        for salary in salaries:
            if employee["id"] == salary["id"]:
                new_dict["id"] = employee["id"]
                new_dict["name"] = employee["name"]
                new_dict["salary"] = salary["salary"]
                new_list.append(new_dict)


# Exercise 3: Advanced Filtering with Multiple Conditions

products = [
    {"id": 1, "category": "Electronics", "price": 850},
    {"id": 2, "category": "Furniture", "price": 1200},
    {"id": 3, "category": "Electronics", "price": 400},
]
# Expected Task: Filter the list to include only products in the "Electronics" category with a price less than 500.

# Your solution here:
# filtered_products = ...

# Expected Output
# print(filtered_products)

### Expected Output

# [
#     {"id": 3, "category": "Electronics", "price": 400}
# ]


for product in products:
    if product["category"] == "Electronics" and product["price"] < 500:
        print(product)


# Exercise 4: Complex Data Transformation
orders = [
    {
        "order_id": 1,
        "items": [{"product": "A", "quantity": 2}, {"product": "B", "quantity": 3}],
    },
    {
        "order_id": 2,
        "items": [{"product": "A", "quantity": 1}, {"product": "C", "quantity": 1}],
    },
]
# Expected Task: Transform this list into a dictionary where keys are product names and values are total quantities ordered across all orders.

# Your solution here:
# product_quantities = ...

# Expected Output
# print(product_quantities)


# Exercise 5: Data Consolidation and Summarization (⭐⭐⭐)</summary>

### 📊 Objective

# Consolidate and summarize data from a list of dictionaries.

# Setup Code
transactions = [
    {"date": "2021-01-01", "amount": 100, "category": "Food"},
    {"date": "2021-01-01", "amount": 200, "category": "Transport"},
    {"date": "2021-01-02", "amount": 150, "category": "Food"},
]
# Expected Task: Summarize the total amount spent per category.

# Your solution here:
# category_totals = ...

# Expected Output
# print(category_totals)


### Expected Output
# {
#     "Food": 250,
#     "Transport": 200
# }
