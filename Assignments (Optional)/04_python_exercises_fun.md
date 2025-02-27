# 🚀 Python Day 04 Exercises: Loops, Lists, and Conditionals

These exercises are designed to help you practice using loops, lists, and conditionals in Python. Each exercise includes a difficulty rating, instructions, minimal setup code, and expected output.

<details>
<summary>📋 Exercise 1: Countdown to Launch! (Difficulty: ⭐)</summary>

**Task**: Create a countdown loop that prints the countdown from 10 to 1, and then prints "Blastoff! 🚀"

**Setup Code**:
```python
# Write a countdown loop from 10 to 1, then print "Blastoff! 🚀"
```

**Expected Output**:
```
10
9
8
7
6
5
4
3
2
1
Blastoff! 🚀
```

**Hint**: Use a `for` loop with the `range()` function. Remember that `range()` can count down with a negative step.
</details>

<details>
<summary>📋 Exercise 2: Temperature Converter (Difficulty: ⭐⭐)</summary>

**Task**: Write a program that converts temperatures from Celsius to Fahrenheit for a range of values.

**Setup Code**:
```python
# Convert these Celsius temperatures to Fahrenheit
celsius_temps = [0, 10, 20, 30, 40]

# Formula: F = (C × 9/5) + 32
```

**Expected Output**:
```
0°C = 32.0°F
10°C = 50.0°F
20°C = 68.0°F
30°C = 86.0°F
40°C = 104.0°F
```

**Hint**: Loop through the list of Celsius temperatures and apply the conversion formula.
</details>

<details>
<summary>📋 Exercise 3: Shopping Cart Total (Difficulty: ⭐⭐)</summary>

**Task**: Calculate the total cost of items in a shopping cart, applying a discount if the total exceeds R10,000.

**Setup Code**:
```python
# Calculate the total cost with a 15% discount if total exceeds R10,000
cart_items = [1200, 4500, 3200, 2800, 950]
discount_rate = 0.15  # 15% discount
```

**Expected Output**:
```
Items in cart: 5
Original total: R12650
Discount applied: R1897.5
Final total: R10752.5
```

**Hint**: Use a loop to calculate the sum, then apply the conditional discount.
</details>

<details>
<summary>📋 Exercise 4: Pattern Printer (Difficulty: ⭐⭐)</summary>

**Task**: Create a program that prints a triangle pattern of stars with a user-specified height.

**Setup Code**:
```python
# Print a triangle of stars with the given height
height = 5  # You can change this value
```

**Expected Output** (for height = 5):
```
*
**
***
****
*****
```

**Hint**: Use nested loops or a single loop with string multiplication.
</details>

<details>
<summary>📋 Exercise 5: Word Length Analyzer (Difficulty: ⭐⭐)</summary>

**Task**: Analyze a list of words and categorize them by length (short, medium, long).

**Setup Code**:
```python
# Categorize words as: 
# short (1-3 chars), medium (4-6 chars), or long (7+ chars)
words = ["cat", "elephant", "mouse", "dog", "rhinoceros", "ant", "giraffe"]
```

**Expected Output**:
```
Short words: ['cat', 'dog', 'ant']
Medium words: ['mouse']
Long words: ['elephant', 'rhinoceros', 'giraffe']
```

**Hint**: Use a loop with conditional statements to categorize each word.
</details>

<details>
<summary>📋 Exercise 6: Weather Report (Difficulty: ⭐⭐⭐)</summary>

**Task**: Create a program that analyzes a week's temperature data and provides a summary report.

**Setup Code**:
```python
# Analyze the week's temperature data and provide a report
temperatures = [28, 31, 25, 29, 32, 27, 26]  # Temperatures in Celsius
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
```

**Expected Output**:
```
Weekly Temperature Report:
Monday: 28°C 🌤️
Tuesday: 31°C 🔥
Wednesday: 25°C ❄️
Thursday: 29°C 🌤️
Friday: 32°C 🔥
Saturday: 27°C 🌤️
Sunday: 26°C 🌤️

Hottest day: Friday (32°C)
Coldest day: Wednesday (25°C)
Average temperature: 28.3°C
```

**Hint**: Use loops, conditionals, and list operations to analyze the data.
</details>

<details>
<summary>📋 Exercise 7: Number Classifier (Difficulty: ⭐⭐)</summary>

**Task**: Write a program that takes a list of numbers and separates them into even, odd, and prime numbers.

**Setup Code**:
```python
# Separate the numbers into even, odd, and prime numbers
numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

# Helper function for checking prime numbers
def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True
```

**Expected Output**:
```
Even numbers: [2, 4, 6, 8, 10, 12, 14]
Odd numbers: [3, 5, 7, 9, 11, 13, 15]
Prime numbers: [2, 3, 5, 7, 11, 13]
```

**Hint**: Use the provided helper function and conditionals to classify each number.
</details>

<details>
<summary>📋 Exercise 8: Text Message Filter (Difficulty: ⭐⭐⭐)</summary>

**Task**: Create a program that filters inappropriate words from a message and replaces them with asterisks.

**Setup Code**:
```python
# Filter out inappropriate words and replace them with asterisks
message = "This darn code is not working. What the heck is wrong with it? It's so stupid!"
inappropriate_words = ["darn", "heck", "stupid"]
```

**Expected Output**:
```
Original message: This darn code is not working. What the heck is wrong with it? It's so stupid!
Filtered message: This **** code is not working. What the **** is wrong with it? It's so ******!
```

**Hint**: Split the message into words, check each against the inappropriate list, and replace if needed.
</details>

<details>
<summary>📋 Exercise 9: Movie Database Search (Difficulty: ⭐⭐⭐)</summary>

**Task**: Create a simple movie database search function that filters movies by genre and minimum rating.

**Setup Code**:
```python
# Search for movies by genre and minimum rating
movies = [
    {"title": "The Shawshank Redemption", "genre": "Drama", "rating": 9.3},
    {"title": "The Godfather", "genre": "Crime", "rating": 9.2},
    {"title": "The Dark Knight", "genre": "Action", "rating": 9.0},
    {"title": "Pulp Fiction", "genre": "Crime", "rating": 8.9},
    {"title": "Fight Club", "genre": "Drama", "rating": 8.8},
    {"title": "Inception", "genre": "Sci-Fi", "rating": 8.8},
    {"title": "The Matrix", "genre": "Sci-Fi", "rating": 8.7},
    {"title": "Goodfellas", "genre": "Crime", "rating": 8.7},
    {"title": "The Avengers", "genre": "Action", "rating": 8.0},
    {"title": "Interstellar", "genre": "Sci-Fi", "rating": 8.6}
]

# Search parameters
search_genre = "Action"
minimum_rating = 8.5
```

**Expected Output**:
```
Movies matching genre "Action" with rating 8.5 or higher:
- The Dark Knight (9.0/10)

Total matches: 1
```

**Hint**: Use a loop with conditionals to filter the movies based on the search criteria.
</details>

<details>
<summary>📋 Exercise 10: Emoji Translator (Difficulty: ⭐⭐⭐)</summary>

**Task**: Create a simple emoji translator that replaces certain words in a message with emojis.

**Setup Code**:
```python
# Replace specific words with emojis
message = "I love pizza and hamburgers but I'm trying to eat more salad and apple"
emoji_dict = {
    "pizza": "🍕",
    "hamburger": "🍔", 
    "hamburgers": "🍔",
    "salad": "🥗",
    "apple": "🍎",
    "love": "❤️"
}
```

**Expected Output**:
```
Original message: I love pizza and hamburgers but I'm trying to eat more salad and apple
Translated message: I ❤️ 🍕 and 🍔 but I'm trying to eat more 🥗 and 🍎
```

**Hint**: Split the message into words and check if each word is in the emoji dictionary.
</details>

<details>
<summary>📋 Exercise 11: List Flattener (Difficulty: ⭐⭐⭐)</summary>

**Task**: Create a function that flattens a list of lists into a single list.

**Setup Code**:
```python
# Flatten a list of lists into a single list
nested_list = [[1, 2, 3], [4, 5], [6, 7, 8, 9], [10]]
```

**Expected Output**:
```
Nested list: [[1, 2, 3], [4, 5], [6, 7, 8, 9], [10]]
Flattened list: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
```

**Hint**: Use nested loops to iterate through each inner list.
</details>

<details>
<summary>📋 Exercise 12: Contact List Organizer (Difficulty: ⭐⭐⭐⭐)</summary>

**Task**: Create a program that organizes a contact list alphabetically by last name, then by first name.

**Setup Code**:
```python
# Organize contacts alphabetically by last name, then first name
contacts = [
    {"first_name": "John", "last_name": "Smith", "phone": "555-1234"},
    {"first_name": "Mary", "last_name": "Johnson", "phone": "555-2345"},
    {"first_name": "James", "last_name": "Smith", "phone": "555-3456"},
    {"first_name": "Patricia", "last_name": "Williams", "phone": "555-4567"},
    {"first_name": "Robert", "last_name": "Jones", "phone": "555-5678"},
    {"first_name": "Linda", "last_name": "Brown", "phone": "555-6789"},
    {"first_name": "Michael", "last_name": "Johnson", "phone": "555-7890"}
]
```

**Expected Output**:
```
Organized Contact List:
1. Brown, Linda (555-6789)
2. Johnson, Mary (555-2345)
3. Johnson, Michael (555-7890)
4. Jones, Robert (555-5678)
5. Smith, James (555-3456)
6. Smith, John (555-1234)
7. Williams, Patricia (555-4567)
```

**Hint**: Use the `sorted()` function with a custom key function that creates a tuple of (last_name, first_name).
</details>

<details>
<summary>📋 Exercise 13: Shopping Budget Helper (Difficulty: ⭐⭐⭐)</summary>

**Task**: Create a program that helps a shopper stay within budget by suggesting what items they can buy.

**Setup Code**:
```python
# Help a shopper stay within budget
items = [
    {"name": "Laptop", "price": 12000},
    {"name": "Headphones", "price": 1500},
    {"name": "Mouse", "price": 800},
    {"name": "Monitor", "price": 3500},
    {"name": "Keyboard", "price": 1200},
    {"name": "Smartphone", "price": 8000},
    {"name": "Tablet", "price": 5000},
    {"name": "Speakers", "price": 2000}
]

budget = 15000  # Shopper's budget in Rands
```

**Expected Output**:
```
Shopping Suggestions (Budget: R15000):

Possible combinations:
1. Laptop (R12000) + Mouse (R800) + Keyboard (R1200) = R14000
2. Laptop (R12000) + Headphones (R1500) = R13500
3. Monitor (R3500) + Keyboard (R1200) + Smartphone (R8000) = R12700
4. Monitor (R3500) + Headphones (R1500) + Tablet (R5000) + Mouse (R800) = R10800
5. Smartphone (R8000) + Tablet (R5000) = R13000

Best Value Option: Monitor (R3500) + Headphones (R1500) + Tablet (R5000) + Mouse (R800) = R10800
```

**Hint**: This is a more complex problem. Start by finding affordable items, then try different combinations.
</details>

<details>
<summary>📋 Exercise 14: Word Frequency Counter (Difficulty: ⭐⭐⭐)</summary>

**Task**: Create a program that counts the frequency of each word in a text, ignoring case and punctuation.

**Setup Code**:
```python
# Count the frequency of each word in the text
text = """
Python is an amazing programming language. Python is easy to learn,
yet powerful enough for professional developers. Many companies use
Python for web development, data analysis, artificial intelligence,
and more. Python's syntax is clean and readable.
"""
```

**Expected Output**:
```
Word Frequency Analysis:
python: 4
is: 3
an: 1
amazing: 1
programming: 1
language: 1
easy: 1
to: 1
learn: 1
yet: 1
powerful: 1
enough: 1
for: 2
professional: 1
developers: 1
many: 1
companies: 1
use: 1
web: 1
development: 1
data: 1
analysis: 1
artificial: 1
intelligence: 1
and: 2
more: 1
syntax: 1
clean: 1
readable: 1
```

**Hint**: Split the text into words, convert to lowercase, remove punctuation, and count occurrences.
</details>

<details>
<summary>📋 Exercise 15: Tic-Tac-Toe Winner Checker (Difficulty: ⭐⭐⭐⭐⭐)</summary>

**Task**: Create a function that checks if there's a winner in a Tic-Tac-Toe game board.

**Setup Code**:
```python
# Check if there's a winner in the Tic-Tac-Toe board
# 'X' for player X, 'O' for player O, and ' ' for empty spaces
board1 = [
    ['X', 'O', 'X'],
    ['O', 'X', 'O'],
    ['O', 'O', 'X']
]  # Diagonal win for X

board2 = [
    ['O', 'X', 'X'],
    ['X', 'O', 'X'],
    ['O', 'O', 'O']
]  # Row win for O

board3 = [
    ['X', 'O', 'X'],
    ['O', 'O', 'X'],
    ['O', 'X', 'X']
]  # Column win for X

board4 = [
    ['X', 'O', 'X'],
    ['O', 'X', 'O'],
    ['X', 'O', 'X']
]  # No winner
```

**Expected Output**:
```
Board 1: X wins!
Board 2: O wins!
Board 3: X wins!
Board 4: No winner
```

**Hint**: Check rows, columns, and diagonals for three of the same character.
</details>
