# Python Day 6: Exercises (Part 3) 🐍

These exercises focus on list comprehensions, a powerful Python feature for creating and transforming lists in a concise and readable way.

## Exercise Difficulty Legend
- ⭐ - Basic
- ⭐⭐ - Straightforward 
- ⭐⭐⭐ - Moderate
- ⭐⭐⭐⭐ - Challenging
- ⭐⭐⭐⭐⭐ - Complex

## List Comprehensions 📋

<details>
<summary>Exercise 1: Basic List Comprehensions (⭐)</summary>

### Task
Convert the following traditional for loops to list comprehensions.

```python
# 1. Square all numbers in a list
numbers = [1, 2, 3, 4, 5]
squares = []
for num in numbers:
    squares.append(num ** 2)

# 2. Get all even numbers from a list
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = []
for num in numbers:
    if num % 2 == 0:
        evens.append(num)

# 3. Convert all strings to uppercase
words = ["apple", "banana", "cherry", "date"]
uppercase = []
for word in words:
    uppercase.append(word.upper())

# Convert to list comprehensions:
# squares = ...
# evens = ...
# uppercase = ...
```

### Expected Output
```
squares: [1, 4, 9, 16, 25]
evens: [2, 4, 6, 8, 10]
uppercase: ['APPLE', 'BANANA', 'CHERRY', 'DATE']
```

</details>

<details>
<summary>Exercise 2: Filtering with List Comprehensions (⭐⭐)</summary>

### Task
Use list comprehensions with conditional filtering to solve the following problems.

```python
# 1. Get all numbers divisible by 3 or 5
numbers = list(range(1, 31))

# 2. Filter out strings shorter than 4 characters
fruits = ["apple", "banana", "kiwi", "fig", "orange", "mango", "pear"]

# 3. Find all palindromes in a list
words = ["level", "hello", "radar", "python", "madam", "civic", "code"]

# Your list comprehensions here:
# divisible_by_3_or_5 = ...
# long_fruits = ...
# palindromes = ...
```

### Expected Output
```
divisible_by_3_or_5: [3, 5, 6, 9, 10, 12, 15, 18, 20, 21, 24, 25, 27, 30]
long_fruits: ['apple', 'banana', 'orange', 'mango']
palindromes: ['level', 'radar', 'madam', 'civic']
```

</details>

<details>
<summary>Exercise 3: Nested List Comprehensions (⭐⭐⭐)</summary>

### Task
Use nested list comprehensions to solve the following problems.

```python
# 1. Flatten a 2D matrix (list of lists)
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# 2. Generate a multiplication table (10x10)
# Should create a 2D list where cell [i][j] contains i*j

# 3. Filter an array of tuples based on two criteria
# Get pairs where both elements are even
pairs = [(1, 2), (2, 3), (2, 4), (4, 6), (5, 7), (6, 8)]

# Your nested list comprehensions here:
# flattened = ...
# mult_table = ...
# even_pairs = ...
```

### Expected Output
```
flattened: [1, 2, 3, 4, 5, 6, 7, 8, 9]
mult_table: (10x10 multiplication table)
even_pairs: [(2, 4), (4, 6), (6, 8)]
```

</details>

<details>
<summary>Exercise 4: Transforming Data with List Comprehensions (⭐⭐⭐)</summary>

### Task
Use list comprehensions to transform data in the following scenarios.

```python
# 1. Calculate the square root of each number (use math.sqrt)
import math
numbers = [4, 9, 16, 25, 36, 49, 64, 81, 100]

# 2. Extract the domain from email addresses
emails = ["user@example.com", "admin@test.org", "info@company.net", "support@website.io"]

# 3. Convert temperatures from Celsius to Fahrenheit
# Formula: F = C * 9/5 + 32
celsius_temps = [0, 10, 20, 30, 40]

# Your list comprehensions here:
# square_roots = ...
# domains = ...
# fahrenheit_temps = ...
```

### Expected Output
```
square_roots: [2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0]
domains: ['example.com', 'test.org', 'company.net', 'website.io']
fahrenheit_temps: [32.0, 50.0, 68.0, 86.0, 104.0]
```

</details>

<details>
<summary>Exercise 5: List Comprehensions with Conditional Expressions (⭐⭐⭐⭐)</summary>

### Task
Combine list comprehensions with ternary conditional expressions to solve the following problems.

```python
# 1. Classify numbers as 'even' or 'odd'
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# 2. Replace vowels with '*' and consonants with '+'
word = "comprehension"

# 3. Normalize values: values < 0 become 0, values > 100 become 100, others stay the same
values = [-20, 15, 60, 150, 0, 120, 75]

# Your list comprehensions with ternary expressions here:
# even_odd = ...
# replaced_chars = ...
# normalized = ...
```

### Expected Output
```
even_odd: ['odd', 'even', 'odd', 'even', 'odd', 'even', 'odd', 'even', 'odd', 'even']
replaced_chars: ['+', '*', '+', '+', '*', '+', '*', '+', '*', '+', '+', '*', '+']
normalized: [0, 15, 60, 100, 0, 100, 75]
```

</details>

<details>
<summary>Exercise 6: Dictionary Comprehensions (⭐⭐⭐)</summary>

### Task
Use dictionary comprehensions to create dictionaries in the following scenarios.

```python
# 1. Create a dictionary mapping numbers to their squares
numbers = range(1, 11)

# 2. Create a dictionary mapping words to their lengths
words = ["apple", "banana", "cherry", "date", "elderberry"]

# 3. Filter a dictionary to keep only pairs where the value is even
original_dict = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 6}

# Your dictionary comprehensions here:
# squares_dict = ...
# word_lengths = ...
# even_values = ...
```

### Expected Output
```
squares_dict: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100}
word_lengths: {'apple': 5, 'banana': 6, 'cherry': 6, 'date': 4, 'elderberry': 10}
even_values: {'b': 2, 'd': 4, 'f': 6}
```

</details>

<details>
<summary>Exercise 7: Set Comprehensions (⭐⭐⭐)</summary>

### Task
Use set comprehensions to create sets in the following scenarios.

```python
# 1. Create a set of all unique vowels in a string
text = "The quick brown fox jumps over the lazy dog"

# 2. Create a set of all unique factors of a number
number = 60

# 3. Create a set of all unique words from a text (case-insensitive)
sentence = "The rain in Spain stays mainly in the plain"

# Your set comprehensions here:
# vowels = ...
# factors = ...
# unique_words = ...
```

### Expected Output
```
vowels: {'a', 'e', 'i', 'o', 'u'}
factors: {1, 2, 3, 4, 5, 6, 10, 12, 15, 20, 30, 60}
unique_words: {'the', 'rain', 'in', 'spain', 'stays', 'mainly', 'plain'}
```

</details>

<details>
<summary>Exercise 8: Practical Applications (⭐⭐⭐⭐)</summary>

### Task
Use list comprehensions to solve real-world scenarios.

```python
# 1. Extract all URLs from a text
text = """
Visit our website at https://example.com for more information.
You can also find us at http://example.org or contact support@example.net.
For secure access, go to https://secure.example.com/login.
"""

# 2. Parse a CSV-like string into a list of dictionaries
csv_data = """
name,age,job
John,28,Developer
Lisa,24,Designer
Michael,32,Manager
Sarah,27,Engineer
"""

# 3. Generate a list of dates for the next 7 days
from datetime import datetime, timedelta
today = datetime.now()

# Your comprehensions here:
# urls = ...
# parsed_data = ...
# next_week = ...
```

### Expected Output
```
urls: ['https://example.com', 'http://example.org', 'https://secure.example.com/login']

parsed_data: [
    {'name': 'John', 'age': '28', 'job': 'Developer'},
    {'name': 'Lisa', 'age': '24', 'job': 'Designer'},
    {'name': 'Michael', 'age': '32', 'job': 'Manager'},
    {'name': 'Sarah', 'age': '27', 'job': 'Engineer'}
]

next_week: [list of 7 datetime objects representing the next 7 days]
```

</details>

## Bonus Challenge 🏆

<details>
<summary>Exercise 9: Data Analysis with Comprehensions (⭐⭐⭐⭐⭐)</summary>

### Task
Use comprehensions to analyze a dataset of student records and extract various insights.

```python
students = [
    {"id": 1, "name": "Alice", "grades": [85, 90, 92, 88], "major": "Computer Science", "year": 3},
    {"id": 2, "name": "Bob", "grades": [78, 82, 80, 85], "major": "Engineering", "year": 2},
    {"id": 3, "name": "Charlie", "grades": [92, 95, 89, 94], "major": "Mathematics", "year": 4},
    {"id": 4, "name": "David", "grades": [75, 70, 82, 78], "major": "Engineering", "year": 1},
    {"id": 5, "name": "Emma", "grades": [88, 84, 90, 92], "major": "Computer Science", "year": 3},
    {"id": 6, "name": "Fiona", "grades": [95, 98, 92, 96], "major": "Mathematics", "year": 2},
    {"id": 7, "name": "George", "grades": [70, 65, 72, 68], "major": "Engineering", "year": 4},
    {"id": 8, "name": "Hannah", "grades": [84, 86, 88, 90], "major": "Computer Science", "year": 1}
]

# 1. Calculate the average grade for each student
# avg_grades = ...

# 2. Group students by major
# students_by_major = ...

# 3. Find the top student in each year
# top_students_by_year = ...

# 4. Create a list of all students who have an A average (90 or above)
# honor_students = ...

# 5. Calculate the overall GPA distribution (how many As, Bs, Cs, etc.)
# Assume: A: 90-100, B: 80-89, C: 70-79, D: 60-69, F: below 60
# grade_distribution = ...

# Your solution using comprehensions (and helper functions if needed)
```

### Expected Output
```
avg_grades: {
    1: 88.75,
    2: 81.25,
    3: 92.5,
    4: 76.25,
    5: 88.5,
    6: 95.25,
    7: 68.75,
    8: 87.0
}

students_by_major: {
    'Computer Science': ['Alice', 'Emma', 'Hannah'],
    'Engineering': ['Bob', 'David', 'George'],
    'Mathematics': ['Charlie', 'Fiona']
}

top_students_by_year: {
    1: 'Hannah',
    2: 'Fiona',
    3: 'Alice',
    4: 'Charlie'
}

honor_students: ['Alice', 'Charlie', 'Emma', 'Fiona']

grade_distribution: {'A': 10, 'B': 9, 'C': 12, 'D': 1, 'F': 0}
```

</details>

---

Good luck with these list comprehension exercises! Remember that the goal of list comprehensions is to make your code more concise, readable, and Pythonic. 🚀
