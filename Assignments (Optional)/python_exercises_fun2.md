# 🧩 Python Day 05 Exercises: Data Structures & Advanced Manipulation

These exercises are designed to help you practice using Python's data structures (tuples, dictionaries), transforming between data types, and using advanced data manipulation techniques. Each exercise includes a difficulty rating, instructions, minimal setup code, and expected output.

<details>
<summary> 📋 Exercise 1: Tuple Time! (Difficulty: ⭐)</summary>

**Task**: Create and manipulate tuples to store information about movies.

**Setup Code**:
```python
# Create a tuple for each movie with (title, year, rating)
# Then access and display different elements
```

**Expected Output**:
```
Movie 1: ('The Shawshank Redemption', 1994, 9.3)
Movie 2: ('The Dark Knight', 2008, 9.0)
First movie title: The Shawshank Redemption
Second movie year: 2008
All movie ratings: [9.3, 9.0]
```

**Hint**: Remember that tuples are immutable, but you can access their elements using indexing.
</details>

<details>
<summary>📋 Exercise 2: Dictionary Basics (Difficulty: ⭐⭐)</summary>

**Task**: Create a dictionary to store information about a user profile and access specific elements.

**Setup Code**:
```python
# Create a user profile dictionary with name, age, email, and favorite_colors (list)
# Then access and display different elements
```

**Expected Output**:
```
User Profile:
Name: John Doe
Age: 28
Email: john@example.com
Favorite Colors: ['blue', 'green', 'black']

John's first favorite color is blue
```

**Hint**: Use dictionary keys to access values and list indexing for nested lists.
</details>

<details>
<summary>📋 Exercise 3: List to String Conversion (Difficulty: ⭐⭐)</summary>

**Task**: Convert a list of strings into a single comma-separated string and vice versa.

**Setup Code**:
```python
# Convert between list and string formats
technologies = ["Python", "JavaScript", "HTML", "CSS", "SQL"]

# Convert the list to a comma-separated string
# Then convert that string back to a list
```

**Expected Output**:
```
Original list: ['Python', 'JavaScript', 'HTML', 'CSS', 'SQL']
As a string: Python, JavaScript, HTML, CSS, SQL
Back to a list: ['Python', 'JavaScript', 'HTML', 'CSS', 'SQL']
```

**Hint**: Use `join()` for list-to-string and `split()` for string-to-list conversion.
</details>

<details>
<summary>📋 Exercise 4: Variable Unpacking (Difficulty: ⭐⭐)</summary>

**Task**: Use variable unpacking to extract values from a list and a tuple.

**Setup Code**:
```python
# Use variable unpacking to assign values from collections to individual variables
coordinates = (35.6895, 139.6917, "Tokyo")  # (latitude, longitude, city)
user_data = ["JohnDoe", "john@example.com", 28, ["Python", "JavaScript"]]
```

**Expected Output**:
```
Coordinates:
Latitude: 35.6895
Longitude: 139.6917
City: Tokyo

User Data:
Username: JohnDoe
Email: john@example.com
Age: 28
Skills: ['Python', 'JavaScript']
```

**Hint**: Use unpacking syntax `variable1, variable2, ... = collection`.
</details>

<details>
<summary>📋 Exercise 5: Dictionary Operations (Difficulty: ⭐⭐)</summary>

**Task**: Perform various operations on a dictionary including adding, updating, and removing items.

**Setup Code**:
```python
# Create and modify a dictionary representing a shopping cart
shopping_cart = {
    "apple": 5,
    "banana": 3,
    "orange": 2
}

# Add new items, update quantities, remove items, and calculate total
```

**Expected Output**:
```
Initial cart: {'apple': 5, 'banana': 3, 'orange': 2}
After adding grapes: {'apple': 5, 'banana': 3, 'orange': 2, 'grape': 4}
After updating bananas: {'apple': 5, 'banana': 6, 'orange': 2, 'grape': 4}
After removing oranges: {'apple': 5, 'banana': 6, 'grape': 4}
Total items in cart: 15
```

**Hint**: Use dictionary methods like `update()`, assignment, `pop()` or `del`.
</details>

<details>
<summary>📋 Exercise 6: Dictionary Comprehension (Difficulty: ⭐⭐⭐)</summary>

**Task**: Use dictionary comprehension to create dictionaries from existing data.

**Setup Code**:
```python
# Create dictionaries using comprehension
numbers = [1, 2, 3, 4, 5]
fruits = ["apple", "banana", "orange", "grape", "mango"]

# Create a dictionary mapping numbers to their squares
# Create a dictionary mapping fruits to their lengths
```

**Expected Output**:
```
Number squares: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
Fruit lengths: {'apple': 5, 'banana': 6, 'orange': 6, 'grape': 5, 'mango': 5}
```

**Hint**: Dictionary comprehension syntax is `{key:value for item in iterable}`.
</details>

<details>
<summary>📋 Exercise 7: Nested Data Structures (Difficulty: ⭐⭐⭐)</summary>

**Task**: Work with nested data structures (dictionaries containing lists and other dictionaries).

**Setup Code**:
```python
# Access and modify nested data structures
student_records = {
    "Alice": {
        "student_id": "A001",
        "courses": ["Math", "Science", "History"],
        "grades": {"Math": 85, "Science": 92, "History": 78}
    },
    "Bob": {
        "student_id": "B002",
        "courses": ["Math", "English", "Art"],
        "grades": {"Math": 90, "English": 88, "Art": 95}
    }
}

# Access specific data and make modifications
```

**Expected Output**:
```
Alice's student ID: A001
Bob's courses: ['Math', 'English', 'Art']
Alice's Science grade: 92

After adding Physics for Alice:
Alice's courses: ['Math', 'Science', 'History', 'Physics']
```

**Hint**: Use multiple levels of keys/indexes to access nested elements.
</details>

<details>
<summary>📋 Exercise 8: Contact List Manager (Difficulty: ⭐⭐⭐)</summary>

**Task**: Create a simple contact list manager using dictionaries.

**Setup Code**:
```python
# Create a contact list manager with functions to add, update, delete and search
contacts = {}

# Implement functions to:
# 1. Add a new contact with name, phone, and email
# 2. Update an existing contact
# 3. Delete a contact
# 4. Search for a contact by name
```

**Expected Output**:
```
After adding contacts:
{'John': {'phone': '555-1234', 'email': 'john@example.com'}, 'Alice': {'phone': '555-5678', 'email': 'alice@example.com'}}

After updating John's contact:
John: {'phone': '555-9876', 'email': 'john.doe@example.com'}

Searching for Alice:
Contact found: {'phone': '555-5678', 'email': 'alice@example.com'}

After deleting John:
{'Alice': {'phone': '555-5678', 'email': 'alice@example.com'}}
```

**Hint**: Implement each function separately, using dictionary operations you've learned.
</details>

<details>
<summary>📋 Exercise 9: Tuple Operations and Methods (Difficulty: ⭐⭐)</summary>

**Task**: Explore different operations and methods available for tuples.

**Setup Code**:
```python
# Create tuples and explore operations
numbers_a = (1, 2, 3, 4, 5)
numbers_b = (5, 6, 7, 8, 9)
repeated = (3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5)

# Perform concatenation, counting, and other operations
```

**Expected Output**:
```
Concatenated tuple: (1, 2, 3, 4, 5, 5, 6, 7, 8, 9)
Number of 5s in repeated: 3
Index of first 5 in repeated: 4
Sorted repeated tuple: (1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9)
```

**Hint**: While tuples are immutable, you can still perform operations like concatenation with `+` and use methods like `count()` and `index()`.
</details>

<details>
<summary>📋 Exercise 10: Dictionary Methods Explorer (Difficulty: ⭐⭐⭐)</summary>

**Task**: Explore and use various dictionary methods.

**Setup Code**:
```python
# Explore dictionary methods
student_scores = {
    "Alice": 92,
    "Bob": 85,
    "Charlie": 78,
    "David": 90,
    "Eve": 88
}

# Use methods like keys(), values(), items(), get(), etc.
```

**Expected Output**:
```
Student names: dict_keys(['Alice', 'Bob', 'Charlie', 'David', 'Eve'])
All scores: dict_values([92, 85, 78, 90, 88])
Name-score pairs: dict_items([('Alice', 92), ('Bob', 85), ('Charlie', 78), ('David', 90), ('Eve', 88)])

Score for Bob: 85
Score for Frank (not in dictionary): Not found
Score for Frank (with default): 0

Average score: 86.6
```

**Hint**: Explore methods like `keys()`, `values()`, `items()`, and `get()` with a default value.
</details>

<details>
<summary>📋 Exercise 11: Inventory Management System (Difficulty: ⭐⭐⭐⭐)</summary>

**Task**: Create a simple inventory management system using dictionaries.

**Setup Code**:
```python
# Create an inventory management system
inventory = {
    "apple": {"price": 1.20, "quantity": 50},
    "banana": {"price": 0.50, "quantity": 75},
    "orange": {"price": 0.80, "quantity": 60},
    "grape": {"price": 2.00, "quantity": 45}
}

# Implement functions to:
# 1. Add a new product with price and quantity
# 2. Update product price or quantity
# 3. Calculate the total value of the inventory
# 4. Check if a product is low in stock (below 30 units)
```

**Expected Output**:
```
Total inventory value: R218.00

Low stock products:
None currently low in stock

After adding watermelon:
{'apple': {'price': 1.2, 'quantity': 50}, 'banana': {'price': 0.5, 'quantity': 75}, 'orange': {'price': 0.8, 'quantity': 60}, 'grape': {'price': 2.0, 'quantity': 45}, 'watermelon': {'price': 5.0, 'quantity': 20}}

After updating banana quantity:
Banana: {'price': 0.5, 'quantity': 25}

Low stock products after updates:
banana: 25 units
watermelon: 20 units

Total inventory value after changes: R183.00
```

**Hint**: Use nested dictionaries to store product details, and create functions for each operation.
</details>

<details>
<summary>📋 Exercise 12: Word Frequency Counter (Difficulty: ⭐⭐⭐)</summary>

**Task**: Count the frequency of words in a text using a dictionary.

**Setup Code**:
```python
# Count word frequencies in a text
text = """
Python is amazing and Python is easy to learn.
Python is widely used in data science, web development,
artificial intelligence, and many other fields.
"""

# Create a dictionary with words as keys and frequencies as values
```

**Expected Output**:
```
Word frequency:
python: 3
is: 4
amazing: 1
and: 2
easy: 1
to: 1
learn: 1
widely: 1
used: 1
in: 1
data: 1
science: 1
web: 1
development: 1
artificial: 1
intelligence: 1
many: 1
other: 1
fields: 1

Most frequent word: 'is' appears 4 times
```

**Hint**: Convert the text to lowercase, split into words, then count occurrences using a dictionary.
</details>

<details>
<summary>📋 Exercise 13: Data Transformation Pipeline (Difficulty: ⭐⭐⭐⭐)</summary>

**Task**: Create a data transformation pipeline that converts between different data formats.

**Setup Code**:
```python
# Create a pipeline for data transformation
# Start with a comma-separated string of values
data_string = "apple,30,1.2,fruit;banana,45,0.5,fruit;carrot,25,0.8,vegetable;spinach,15,1.5,vegetable"

# Convert to a list of tuples, then to a dictionary, then perform analysis
```

**Expected Output**:
```
Original data string:
apple,30,1.2,fruit;banana,45,0.5,fruit;carrot,25,0.8,vegetable;spinach,15,1.5,vegetable

List of tuples:
[('apple', '30', '1.2', 'fruit'), ('banana', '45', '0.5', 'fruit'), ('carrot', '25', '0.8', 'vegetable'), ('spinach', '15', '1.5', 'vegetable')]

Dictionary:
{'apple': {'quantity': 30, 'price': 1.2, 'category': 'fruit'},
 'banana': {'quantity': 45, 'price': 0.5, 'category': 'fruit'},
 'carrot': {'quantity': 25, 'price': 0.8, 'category': 'vegetable'},
 'spinach': {'quantity': 15, 'price': 1.5, 'category': 'vegetable'}}

Analysis:
Total fruit items: 75
Total vegetable items: 40
Average fruit price: R0.85
Average vegetable price: R1.15
```

**Hint**: Use string methods like `split()`, then convert to appropriate data structures, performing transformations at each step.
</details>

<details>
<summary>📋 Exercise 14: Multi-value Dictionary (Difficulty: ⭐⭐⭐)</summary>

**Task**: Create a dictionary where each key can have multiple values (using lists as values).

**Setup Code**:
```python
# Create a dictionary with lists as values to store multiple values per key
# Use it to track students and the courses they're enrolled in
```

**Expected Output**:
```
Course enrollments:
{'Math': ['Alice', 'Bob', 'Charlie', 'Eve'], 
 'Science': ['Alice', 'Bob', 'David'], 
 'History': ['Charlie', 'Eve', 'Frank'], 
 'English': ['David', 'Frank']}

Students in Math: ['Alice', 'Bob', 'Charlie', 'Eve']
Courses taken by Alice: ['Math', 'Science']
```

**Hint**: Create a dictionary with lists as values, then add students to the appropriate course lists.
</details>

<details>
<summary>📋 Exercise 15: Advanced Unpacking Techniques (Difficulty: ⭐⭐⭐⭐⭐)</summary>

**Task**: Use advanced unpacking techniques with the asterisk operator.

**Setup Code**:
```python
# Explore advanced unpacking techniques with * (asterisk)
# For both lists and dictionaries
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Use * to unpack in different scenarios
```

**Expected Output**:
```
First number: 1
Last number: 10
Middle numbers: [2, 3, 4, 5, 6, 7, 8, 9]

First two numbers: [1, 2]
Last two numbers: [9, 10]
Middle numbers: [3, 4, 5, 6, 7, 8]

Combined lists: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

Function with variable arguments:
Positional args: (1, 2, 3)
Keyword args: {'a': 10, 'b': 20, 'c': 30}
```

**Hint**: Use `*` for list unpacking in assignments and `**` for dictionary unpacking. Create functions that use `*args` and `**kwargs`.
</details>
