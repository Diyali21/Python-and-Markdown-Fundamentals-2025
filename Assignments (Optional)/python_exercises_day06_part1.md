# Python Day 6: Exercises (Part 1) 🐍

These exercises cover several Python concepts from Day 6:
- Advanced Dictionary Operations
- Inventory Management System
- Safe Dictionary Access

## Exercise Difficulty Legend
- ⭐ - Basic
- ⭐⭐ - Straightforward 
- ⭐⭐⭐ - Moderate
- ⭐⭐⭐⭐ - Challenging
- ⭐⭐⭐⭐⭐ - Complex

## Advanced Dictionary Operations 📚

<details>
<summary>Exercise 1: Book Database Queries (⭐⭐)</summary>

### Task
Given a list of dictionaries containing book information, extract various pieces of information.

```python
books = [
    {"title": "Infinite Jest", "rating": 4.5, "genre": "Fiction"},
    {"title": "The Catcher in the Rye", "rating": 3.9, "genre": "Fiction"},
    {"title": "Sapiens", "rating": 4.9, "genre": "History"},
    {"title": "A Brief History of Time", "rating": 4.8, "genre": "Science"},
    {"title": "Clean Code", "rating": 4.7, "genre": "Technology"},
]

# 1. Extract all book titles into a list

# 2. Extract only Fiction book titles

# 3. Find the highest rated books (rating >= 4.7)
```

### Expected Output
```
# Output for task 1:
['Infinite Jest', 'The Catcher in the Rye', 'Sapiens', 'A Brief History of Time', 'Clean Code']

# Output for task 2:
['Infinite Jest', 'The Catcher in the Rye']

# Output for task 3:
Highest rated books are: Sapiens, A Brief History of Time and Clean Code
```

</details>

<details>
<summary>Exercise 2: Dictionary Value Transformation (⭐⭐⭐)</summary>

### Task
Given a dictionary of student scores, implement functions to:
1. Convert all scores to a 5-point GPA scale (90-100 = 5.0, 80-89 = 4.0, etc.)
2. Create a new dictionary with course codes as keys and lists of student names who scored above 85 as values

```python
student_scores = {
    "Alice": {"CS101": 92, "MATH201": 87, "ENG101": 78},
    "Bob": {"CS101": 85, "MATH201": 92, "ENG101": 91},
    "Charlie": {"CS101": 78, "MATH201": 69, "ENG101": 84},
    "Diana": {"CS101": 95, "MATH201": 88, "ENG101": 92}
}

def convert_to_gpa(scores_dict):
    # Your code here
    pass

def group_high_performers(scores_dict):
    # Your code here
    pass
```

### Expected Output
```
# GPA conversion:
{
    "Alice": {"CS101": 5.0, "MATH201": 4.0, "ENG101": 3.0},
    "Bob": {"CS101": 4.0, "MATH201": 5.0, "ENG101": 5.0},
    "Charlie": {"CS101": 3.0, "MATH201": 2.0, "ENG101": 3.0},
    "Diana": {"CS101": 5.0, "MATH201": 4.0, "ENG101": 5.0}
}

# High performers by course:
{
    "CS101": ["Alice", "Diana"],
    "MATH201": ["Alice", "Bob", "Diana"],
    "ENG101": ["Bob", "Diana"]
}
```

</details>

<details>
<summary>Exercise 3: Advanced Dictionary Manipulation (⭐⭐⭐⭐)</summary>

### Task
Create a function that takes a list of product dictionaries and performs the following operations:
1. Groups products by category
2. For each category, calculates the average price
3. Identifies the most expensive and least expensive product in each category
4. Returns a summary dictionary with all this information

```python
products = [
    {"id": 1, "name": "Laptop", "price": 1200, "category": "Electronics"},
    {"id": 2, "name": "Smartphone", "price": 800, "category": "Electronics"},
    {"id": 3, "name": "T-shirt", "price": 25, "category": "Clothing"},
    {"id": 4, "name": "Jeans", "price": 60, "category": "Clothing"},
    {"id": 5, "name": "Coffee Machine", "price": 150, "category": "Kitchen"},
    {"id": 6, "name": "Blender", "price": 80, "category": "Kitchen"},
    {"id": 7, "name": "Headphones", "price": 100, "category": "Electronics"},
    {"id": 8, "name": "Sweater", "price": 45, "category": "Clothing"}
]

def analyze_products(product_list):
    # Your code here
    pass
```

### Expected Output
```
{
    "Electronics": {
        "avg_price": 700.0,
        "most_expensive": {"name": "Laptop", "price": 1200},
        "least_expensive": {"name": "Headphones", "price": 100},
        "count": 3
    },
    "Clothing": {
        "avg_price": 43.33,
        "most_expensive": {"name": "Jeans", "price": 60},
        "least_expensive": {"name": "T-shirt", "price": 25},
        "count": 3
    },
    "Kitchen": {
        "avg_price": 115.0,
        "most_expensive": {"name": "Coffee Machine", "price": 150},
        "least_expensive": {"name": "Blender", "price": 80},
        "count": 2
    }
}
```

</details>

## Inventory Management System 🛒

<details>
<summary>Exercise 4: Simple Inventory System (⭐⭐⭐)</summary>

### Task
Create a simple inventory management system that allows users to:
1. Add new products to the inventory
2. Update product quantities
3. Calculate the total value of inventory
4. Display low stock items (quantity < 5)

```python
def add_product(inventory, name, quantity, price):
    # Your code here
    pass

def update_quantity(inventory, name, new_quantity):
    # Your code here
    pass

def calculate_inventory_value(inventory):
    # Your code here
    pass

def get_low_stock_items(inventory, threshold=5):
    # Your code here
    pass

# Test your functions with this starter inventory
inventory = [
    {"name": "Apple 🍎", "quantity": 30, "price": 0.50},
    {"name": "Banana 🍌", "quantity": 20, "price": 0.20},
    {"name": "Orange 🍊", "quantity": 15, "price": 0.70},
    {"name": "Grapes 🍇", "quantity": 4, "price": 2.50},
]
```

### Expected Output
```
# After adding Strawberry 🍓 (quantity: 10, price: 1.20)
[
    {"name": "Apple 🍎", "quantity": 30, "price": 0.50},
    {"name": "Banana 🍌", "quantity": 20, "price": 0.20},
    {"name": "Orange 🍊", "quantity": 15, "price": 0.70},
    {"name": "Grapes 🍇", "quantity": 4, "price": 2.50},
    {"name": "Strawberry 🍓", "quantity": 10, "price": 1.20}
]

# Total inventory value: $37.00

# Low stock items (quantity < 5):
[{"name": "Grapes 🍇", "quantity": 4, "price": 2.50}]
```

</details>

<details>
<summary>Exercise 5: Interactive Inventory Management (⭐⭐⭐⭐)</summary>

### Task
Extend the previous inventory system to create a command-line interactive inventory management application with the following features:
1. Add new products
2. Remove products
3. Update product details (name, quantity, price)
4. Search for products by name
5. Generate inventory reports (total value, low stock items, etc.)

```python
def main():
    inventory = [
        {"name": "Apple 🍎", "quantity": 30, "price": 0.50},
        {"name": "Banana 🍌", "quantity": 20, "price": 0.20},
    ]
    
    while True:
        # Display menu and handle user input
        # Implement the required functionality
        pass

# Implement your helper functions here
# ...

if __name__ == "__main__":
    main()
```

### Expected Output
```
# A sample interactive session might look like:

==== Inventory Management System ====
1. Add new product
2. Remove product
3. Update product
4. Search products
5. Generate reports
6. Exit
Enter your choice: 1

Adding new product:
Name: Mango 🥭
Quantity: 15
Price: 1.50
Product added successfully!

==== Inventory Management System ====
...
```

</details>

## Safe Dictionary Access 🛡️

<details>
<summary>Exercise 6: Error Prevention (⭐⭐)</summary>

### Task
Implement functions that safely access dictionary values without causing KeyError exceptions, with appropriate fallback values.

```python
hero = {
    "name": "Peter Parker",
    "age": 18,
    "team_name": "Avengers",
    "team": ["Iron Man", "Thor", "Hulk", "Captain America"]
}

def get_hero_attribute(hero_dict, attribute):
    # Safely access hero attributes with default value of "Unknown"
    pass

def get_team_members(hero_dict):
    # Safely access and return team members, or empty list if not available
    pass

def get_hero_detail(hero_dict, detail, default_value):
    # Safely access any hero detail with a user-specified default value
    pass
```

### Expected Output
```
# For get_hero_attribute:
Name: Peter Parker
Height: Unknown
Age: 18

# For get_team_members:
Team members: ['Iron Man', 'Thor', 'Hulk', 'Captain America']

# For get_hero_detail:
Power Level: Not specified (using default_value="Not specified")
```

</details>

<details>
<summary>Exercise 7: Nested Dictionary Access (⭐⭐⭐)</summary>

### Task
Create functions to safely access nested dictionary values without raising KeyError exceptions, even when intermediate keys don't exist.

```python
user_data = {
    "user123": {
        "personal": {
            "name": "Jane Smith",
            "age": 28,
            "contact": {
                "email": "jane@example.com",
                "phone": "555-1234"
            }
        },
        "preferences": {
            "theme": "dark",
            "notifications": True
        }
    },
    "user456": {
        "personal": {
            "name": "John Doe",
            "age": 34
        }
    }
}

def safe_get_nested(data, key_path, default=None):
    # Implement safe nested dictionary access
    # key_path can be a list or tuple of keys to traverse
    pass

def update_nested_safely(data, key_path, value):
    # Update a nested value, creating intermediate dictionaries if needed
    pass
```

### Expected Output
```
# Safe access examples:
print(safe_get_nested(user_data, ["user123", "personal", "contact", "email"]))
# Output: jane@example.com

print(safe_get_nested(user_data, ["user456", "personal", "contact", "email"], "No email found"))
# Output: No email found

# After updating:
update_nested_safely(user_data, ["user456", "personal", "contact", "email"], "john@example.com")
print(safe_get_nested(user_data, ["user456", "personal", "contact", "email"]))
# Output: john@example.com
```

</details>

<details>
<summary>Exercise 8: Advanced Dictionary Safety (⭐⭐⭐⭐)</summary>

### Task
Create a SafeDict class that extends the built-in dictionary functionality to make all operations safe by default, with appropriate default values and logging capabilities.

```python
class SafeDict(dict):
    def __init__(self, default_value=None, *args, **kwargs):
        # Initialize with default value and optional logging
        super().__init__(*args, **kwargs)
        self.default_value = default_value
        self.access_log = []
    
    # Override standard dictionary methods to make them "safe"
    # Implement __getitem__, get, etc.
    
    # Add logging capability
    
    # Add convenience methods for nested access
    
    # Your implementation here

# Test your SafeDict class
hero = SafeDict({
    "name": "Peter Parker",
    "age": 18,
    "team_name": "Avengers",
    "team": ["Iron Man", "Thor", "Hulk", "Captain America"]
}, default_value="Not Available")
```

### Expected Output
```
# Accessing existing key
print(hero["name"])  # Output: Peter Parker

# Accessing non-existent key should return default value, not raise KeyError
print(hero["power_level"])  # Output: Not Available

# Accessing logs
print(hero.access_log)
# Output might look like: [("name", True), ("power_level", False)]
# Indicating access attempts and whether the key existed

# Nested access should work similarly
nested_dict = SafeDict({"a": {"b": {"c": 42}}}, default_value="Not Found")
print(nested_dict.get_nested(["a", "b", "c"]))  # Output: 42
print(nested_dict.get_nested(["a", "b", "d"]))  # Output: Not Found
```

</details>

## Bonus Challenge 🏆

<details>
<summary>Exercise 9: E-commerce Inventory System (⭐⭐⭐⭐⭐)</summary>

### Task
Create a comprehensive e-commerce inventory system that combines all the concepts learned:
- Dictionary operations
- Safe access
- Data transformation

The system should:
1. Track products across multiple warehouses
2. Handle stock movements (transfers, additions, sales)
3. Generate reports on inventory status
4. Alert on low stock
5. Calculate inventory value
6. Support searching and filtering inventory

```python
# Your implementation here
```

### Expected Output
```
# Demonstrates all functionality working together
```

</details>

---

Good luck with these exercises! Remember to apply the concepts you've learned and focus on writing clean, efficient, and maintainable code. 🚀
