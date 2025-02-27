# Python Day 5: Additional Exercises 🐍

These exercises cover several additional Python concepts from Day 5:
- Multi-line strings
- Built-in functions like `sum()`
- Code quality principles
- Copy by reference vs. copy by value
- Advanced dictionary operations

## Exercise Difficulty Legend
- ⭐ - Basic
- ⭐⭐ - Straightforward 
- ⭐⭐⭐ - Moderate
- ⭐⭐⭐⭐ - Challenging
- ⭐⭐⭐⭐⭐ - Complex

## Multi-line Strings 📝

<details>
<summary>Exercise 1: Poetry Generator (⭐⭐)</summary>

### Task
Create a multi-line string poem about programming, then extract and print only the first and last lines.

```python
# Your code here
# Hint: Use triple quotes for multi-line strings
```

### Expected Output
```
Python is magical, powerful and fun
Happy coding to everyone!
```

</details>

<details>
<summary>Exercise 2: Formatted Invoice (⭐⭐⭐)</summary>

### Task
Create a function that generates a professional invoice using a multi-line f-string. The function should take customer name, items purchased (list of dictionaries with name, quantity, price), and date as parameters.

```python
def generate_invoice(customer_name, items, date):
    # Your code here
    # Use a multi-line f-string to format the invoice
    pass

# Test with
items = [
    {"name": "Laptop", "quantity": 1, "price": 1200},
    {"name": "Mouse", "quantity": 2, "price": 25},
    {"name": "Keyboard", "quantity": 1, "price": 45}
]
print(generate_invoice("John Smith", items, "2025-02-27"))
```

### Expected Output
```
INVOICE
Date: 2025-02-27
Customer: John Smith
------------------------
ITEMS:
Laptop x1 - $1200.00
Mouse x2 - $50.00
Keyboard x1 - $45.00
------------------------
TOTAL: $1295.00
```

</details>

<details>
<summary>Exercise 3: Code Documentation (⭐⭐)</summary>

### Task
Create a function with proper docstring documentation that calculates the area of a circle. The docstring should be a multi-line string including a description, parameters, returns, and an example.

```python
# Your code here
```

### Expected Output
```
Function: area_of_circle
Description: Calculates the area of a circle based on its radius.
Parameters: radius (float) - The radius of the circle
Returns: float - The area of the circle
Example: area_of_circle(2) returns 12.57
```

</details>

## Built-in Functions (sum) 🧮

<details>
<summary>Exercise 4: Grade Calculator (⭐⭐)</summary>

### Task
Create a function that calculates the average grade from a list of scores and returns a letter grade based on the following scale:
- 90-100: A
- 80-89: B
- 70-79: C
- 60-69: D
- Below 60: F

```python
def calculate_grade(scores):
    # Your code here
    # Use sum() and len() to calculate the average
    pass

# Test with
print(calculate_grade([85, 90, 78, 88]))  # Should return "B"
print(calculate_grade([95, 92, 90, 98]))  # Should return "A"
```

### Expected Output
```
B
A
```

</details>

<details>
<summary>Exercise 5: Shopping Cart Total (⭐⭐⭐)</summary>

### Task
Create a function that calculates the total cost of items in a shopping cart, including a discount if applicable.

```python
def calculate_cart_total(items, discount_percentage=0):
    # Your code here
    # Use sum() to calculate the total
    pass

# Test with
cart = [
    {"name": "T-shirt", "price": 15.99, "quantity": 2},
    {"name": "Jeans", "price": 29.99, "quantity": 1},
    {"name": "Shoes", "price": 59.99, "quantity": 1}
]
print(f"Total without discount: ${calculate_cart_total(cart):.2f}")
print(f"Total with 15% discount: ${calculate_cart_total(cart, 15):.2f}")
```

### Expected Output
```
Total without discount: $121.96
Total with 15% discount: $103.67
```

</details>

<details>
<summary>Exercise 6: Advanced Statistics (⭐⭐⭐⭐)</summary>

### Task
Create functions to calculate the sum, mean, median, and range of a list of numbers without using the statistics module.

```python
def calculate_statistics(numbers):
    # Your code here
    # Calculate sum, mean, median, and range
    pass

# Test with
data = [23, 19, 45, 32, 19, 27, 65, 42]
stats = calculate_statistics(data)
print(f"Sum: {stats['sum']}")
print(f"Mean: {stats['mean']}")
print(f"Median: {stats['median']}")
print(f"Range: {stats['range']}")
```

### Expected Output
```
Sum: 272
Mean: 34.0
Median: 29.5
Range: 46
```

</details>

## Code Quality 🏆

<details>
<summary>Exercise 7: Code Refactoring (⭐⭐⭐)</summary>

### Task
Refactor the following code to improve readability, maintainability, and performance without changing its functionality.

```python
def p(n,t):
    r=n
    for i in range(t-1):
        r=r*n
    return r

def c(a,b):
    if b==0:return 1
    if b==a:return 1
    return c(a-1,b-1)+c(a-1,b)

def s(l):
    r=0
    for i in l:r+=i
    return r

# Refactor the above code below
# Your refactored code here
```

### Expected Output
```
# Example of usage for the original functions:
print(p(2, 3))  # 8
print(c(5, 2))  # 10
print(s([1, 2, 3, 4]))  # 10

# Your refactored code should produce the same outputs
```

</details>

<details>
<summary>Exercise 8: Code Review (⭐⭐⭐)</summary>

### Task
Review the following code and identify at least 5 issues related to the 5 pillars of code quality. Then, fix the code to address these issues.

```python
def findMax(l):
    m = l[0]
    for x in l:
        if x > m:
            m = x
    return m

def processdata(d):
    for i in range(len(d)):
        d[i] = d[i] * 2
    r = []
    for x in d:
        if x > 100:
            r.append(x)
    return r

# Your code review comments and fixed code here
```

### Expected Output
```
# Comments identifying issues related to:
# 1. Readability
# 2. Maintainability
# 3. Extensibility
# 4. Testability
# 5. Performance

# And your fixed code that addresses these issues
```

</details>

<details>
<summary>Exercise 9: Function Documentation (⭐⭐)</summary>

### Task
Add proper documentation to the following functions based on best practices for code quality.

```python
def calculate_tax(income, rate=0.2):
    return income * rate

def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True

# Your documented versions of these functions here
```

### Expected Output
```
# Well-documented functions with clear descriptions,
# parameter explanations, return value descriptions,
# and example usage
```

</details>

## Copy by Reference vs. Copy by Value 🔄

<details>
<summary>Exercise 10: List Modification (⭐⭐⭐)</summary>

### Task
Create a function that demonstrates the difference between copy by reference and copy by value when working with lists.

```python
def modify_lists():
    # Create a list and make both reference and value copies
    # Modify all three lists differently
    # Return all three lists to show the differences
    pass

# Test your function
original, reference_copy, value_copy = modify_lists()
print(f"Original list: {original}")
print(f"Reference copy: {reference_copy}")
print(f"Value copy: {value_copy}")
```

### Expected Output
```
Original list: [1, 2, 3, 4, 100]
Reference copy: [1, 2, 3, 4, 100]
Value copy: [1, 2, 3, 4, 200]
```

</details>

<details>
<summary>Exercise 11: Nested List Copy (⭐⭐⭐⭐)</summary>

### Task
Demonstrate the limitations of shallow copying with nested lists and show how to perform a deep copy.

```python
import copy

def nested_list_copy():
    # Create a nested list and make shallow and deep copies
    # Modify elements at different levels
    # Return all three lists to show the differences
    pass

# Test your function
original, shallow_copy, deep_copy = nested_list_copy()
print(f"Original: {original}")
print(f"Shallow copy: {shallow_copy}")
print(f"Deep copy: {deep_copy}")
```

### Expected Output
```
Original: [[1, 2, 99], [3, 4, 5]]
Shallow copy: [[1, 2, 99], [3, 4, 5]]
Deep copy: [[1, 2, 3], [3, 4, 5]]
```

</details>

<details>
<summary>Exercise 12: Function Parameters (⭐⭐⭐)</summary>

### Task
Create a function that demonstrates how different data types (immutable vs. mutable) behave differently when passed as parameters to a function.

```python
def modify_parameters(number, string, list_param, dict_param):
    # Attempt to modify all parameters
    # Return the modified values from inside the function
    pass

# Test your function
num = 10
text = "hello"
my_list = [1, 2, 3]
my_dict = {"a": 1, "b": 2}

inside_values = modify_parameters(num, text, my_list, my_dict)
print(f"Inside function: {inside_values}")
print(f"Outside function - num: {num}")
print(f"Outside function - text: {text}")
print(f"Outside function - my_list: {my_list}")
print(f"Outside function - my_dict: {my_dict}")
```

### Expected Output
```
Inside function: (20, 'hello_modified', [1, 2, 3, 4], {'a': 1, 'b': 2, 'c': 3})
Outside function - num: 10
Outside function - text: hello
Outside function - my_list: [1, 2, 3, 4]
Outside function - my_dict: {'a': 1, 'b': 2, 'c': 3}
```

</details>

## Advanced Dictionary Operations 📚

<details>
<summary>Exercise 13: Book Database (⭐⭐⭐)</summary>

### Task
Create functions to extract specific information from a book database.

```python
books = [
    {"title": "Infinite Jest", "rating": 4.5, "genre": "Fiction"},
    {"title": "The Catcher in the Rye", "rating": 3.9, "genre": "Fiction"},
    {"title": "Sapiens", "rating": 4.9, "genre": "History"},
    {"title": "A Brief History of Time", "rating": 4.8, "genre": "Science"},
    {"title": "Clean Code", "rating": 4.7, "genre": "Technology"},
]

def get_titles(book_list):
    # Return a list of all book titles
    pass

def get_fiction_titles(book_list):
    # Return a list of titles of fiction books only
    pass

def get_highest_rated_books(book_list, min_rating=4.7):
    # Return a formatted string listing the highest rated books
    pass

# Test your functions
print(get_titles(books))
print(get_fiction_titles(books))
print(get_highest_rated_books(books))
```

### Expected Output
```
["Infinite Jest", "The Catcher in the Rye", "Sapiens", "A Brief History of Time", "Clean Code"]
["Infinite Jest", "The Catcher in the Rye"]
Highest rated books are: Sapiens, A Brief History of Time and Clean Code
```

</details>

<details>
<summary>Exercise 14: Dictionary Transformation (⭐⭐⭐⭐)</summary>

### Task
Write a function that transforms a list of student records into a dictionary keyed by student ID, with values containing all their course scores.

```python
records = [
    {"student_id": "S001", "course": "Python", "score": 85},
    {"student_id": "S002", "course": "Java", "score": 92},
    {"student_id": "S001", "course": "SQL", "score": 78},
    {"student_id": "S003", "course": "Python", "score": 88},
    {"student_id": "S002", "course": "Python", "score": 90},
    {"student_id": "S001", "course": "Java", "score": 65},
]

def transform_records(records_list):
    # Transform the records into a dictionary by student_id
    # with nested dictionaries of courses and scores
    pass

# Test your function
student_records = transform_records(records)
for student_id, courses in student_records.items():
    print(f"Student {student_id}: {courses}")
```

### Expected Output
```
Student S001: {'Python': 85, 'SQL': 78, 'Java': 65}
Student S002: {'Java': 92, 'Python': 90}
Student S003: {'Python': 88}
```

</details>

<details>
<summary>Exercise 15: Dictionary Comprehension (⭐⭐⭐⭐⭐)</summary>

### Task
Use dictionary comprehension to create a dictionary of word frequencies from a text, then find the most common word and its count.

```python
def word_frequency(text):
    # Use dictionary comprehension to create a word frequency dictionary
    # Return the dictionary, most common word, and its count
    pass

# Test your function
sample_text = """
Python is amazing. Python is versatile and Python is used in many industries.
Data scientists love Python because Python has great libraries for data analysis.
Web developers also use Python for backend development.
"""

freq_dict, most_common_word, count = word_frequency(sample_text)
print(f"Word frequencies: {freq_dict}")
print(f"Most common word: '{most_common_word}' (appears {count} times)")
```

### Expected Output
```
Word frequencies: {'python': 5, 'is': 4, 'amazing': 1, 'versatile': 1, 'and': 1, 'used': 1, 'in': 1, 'many': 1, 'industries': 1, 'data': 2, 'scientists': 1, 'love': 1, 'because': 1, 'has': 1, 'great': 1, 'libraries': 1, 'for': 2, 'analysis': 1, 'web': 1, 'developers': 1, 'also': 1, 'use': 1, 'backend': 1, 'development': 1}
Most common word: 'python' (appears 5 times)
```

</details>

## Bonus Challenge: Combining Concepts 🏆🔥

<details>
<summary>Exercise 16: Library Management System (⭐⭐⭐⭐⭐)</summary>

### Task
Create a simple library management system that combines multi-line strings, copy concepts, dictionary operations, built-in functions, and follows code quality principles.

The system should:
1. Allow adding books with title, author, publication year, and genre
2. Enable searching for books by title or author
3. Keep track of whether books are checked out
4. Generate formatted reports about the library collection

```python
class Library:
    def __init__(self, name):
        # Initialize the library
        pass
        
    def add_book(self, title, author, year, genre):
        # Add a book to the library
        pass
    
    def search_books(self, query):
        # Search for books by title or author
        pass
    
    def checkout_book(self, book_id):
        # Mark a book as checked out
        pass
    
    def return_book(self, book_id):
        # Mark a book as returned
        pass
    
    def generate_report(self):
        # Generate a formatted report about the library
        pass

# Test your library system with sample data
```

### Expected Output
```
# A formatted report showing library statistics
# Results from searches
# Confirmation of checkout/return operations
```

</details>

---

Good luck with these exercises! Remember to apply the concepts you've learned and focus on writing clean, efficient, and maintainable code. 🚀
