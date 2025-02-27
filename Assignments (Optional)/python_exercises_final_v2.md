# 🐍 Python Day 2 Exercises 🚀

## 1. Name Tag Generator (Difficulty: 1) ✔️

<details>
<summary>Topics</summary>

- String manipulation
- F-strings
- User input
</details>

Create a program that asks for a name and prints a decorated name tag.

```python
name = input("Enter your name: ")
# Convert to uppercase and print decorated name
```

**Expected Output:**

```
Enter your name: Maria
✨ Hello, MARIA! ✨
```

**Hint:** Use string methods and f-strings.

---

## 2. Age Calculator (Difficulty: 1)

<details>
<summary>Topics</summary>

- Basic arithmetic
- Type conversion
- F-strings
</details>

Calculate someone's age based on their birth year.

```python
birth_year = int(input("Enter birth year: "))
current_year = 2025
# Calculate and display age
```

**Expected Output:**

```
Enter birth year: 2000
You are 25 years old in 2025.
```

---

## 3. Emoji Replacer (Difficulty: 2)

<details>
<summary>Topics</summary>

- Dictionaries
- String methods
- String replacement
</details>

Replace certain words in a sentence with emojis.

```python
emoji_dict = {"love": "❤️", "pizza": "🍕", "happy": "😊"}
sentence = input("Enter a sentence: ")
# Replace matching words with emojis
```

**Expected Output:**

```
Case 1:
Enter a sentence: I love coding and pizza
I ❤️ coding and 🍕

Case 2:
Enter a sentence: The weather is nice today
The weather is nice today
```

---

## 4. Tip Calculator (Difficulty: 2)

<details>
<summary>Topics</summary>

- Conditional statements
- Floating-point arithmetic
- String formatting
</details>

Calculate a restaurant tip based on the bill amount and service quality.

```python
bill = float(input("Bill amount: $"))
service = input("Service (poor/fair/good/excellent): ").lower()
# Calculate tip and total based on service quality
```

**Expected Output:**

```
Case 1:
Bill amount: $45.50
Service (poor/fair/good/excellent): good
Tip: $8.19
Total: $53.69

Case 2:
Bill amount: $100.00
Service (poor/fair/good/excellent): poor
Tip: $10.00
Total: $110.00
```

---

## 5. Temperature Converter (Difficulty: 2)

<details>
<summary>Topics</summary>

- Mathematical formulas
- Conditional logic
- Formatted output
</details>

Convert between Celsius and Fahrenheit.

```python
temp = float(input("Enter temperature: "))
unit = input("Convert from (C/F): ").upper()
# Convert temperature based on unit
```

**Expected Output:**

```
Case 1:
Enter temperature: 30
Convert from (C/F): C
30.0°C = 86.0°F

Case 2:
Enter temperature: 32
Convert from (C/F): F
32.0°F = 0.0°C
```

---

## 6. BMI Calculator (Difficulty: 2)

<details>
<summary>Topics</summary>

- Mathematical formulas
- Conditional categorization
- Floating-point arithmetic
</details>

Calculate Body Mass Index from height and weight.

```python
weight = float(input("Enter weight (kg): "))
height = float(input("Enter height (m): "))
# Calculate BMI and determine category
```

**Expected Output:**

```
Case 1:
Enter weight (kg): 70
Enter height (m): 1.75
Your BMI: 22.86 (Normal weight)

Case 2:
Enter weight (kg): 90
Enter height (m): 1.70
Your BMI: 31.14 (Obese)
```

**Hint:** Categorize BMI as Underweight (<18.5), Normal (18.5-24.9), Overweight (25-29.9), or Obese (≥30).

---

## 7. Coin Toss Simulator (Difficulty: 2)

<details>
<summary>Topics</summary>

- Random number generation
- Conditional statements
- Emoji output
</details>

Simulate a coin toss with emoji results.

```python
import random
# Generate random result and display heads or tails
```

**Expected Output:**

```
Flipping a coin...
Result: 🪙 Heads!
```

---

## 8. Password Generator (Difficulty: 3)

<details>
<summary>Topics</summary>

- Random character selection
- String concatenation
- Character sets
</details>

Generate a random password with specified length.

```python
import random
import string

length = int(input("Password length: "))
# Generate password using lowercase, uppercase, digits, and symbols
```

**Expected Output:**

```
Case 1:
Password length: 8
Generated password: Kd7$pQ2z

Case 2:
Password length: 4
Generated password: R5!a
```

---

## 9. Text Analyzer (Difficulty: 3)

<details>
<summary>Topics</summary>

- String methods
- Character counting
- Word splitting
- List operations
</details>

Analyze a text input for character count, word count, and average word length.

```python
text = input("Enter text: ")
# Count characters (excluding spaces)
# Count words
# Calculate average word length
```

**Expected Output:**

```
Case 1:
Enter text: Python is fun to learn!
Characters: 22
Words: 5
Average word length: 4.4

Case 2:
Enter text: Programming
Characters: 11
Words: 1
Average word length: 11.0
```

---

## 10. Emoji Mood Detector (Difficulty: 3)

<details>
<summary>Topics</summary>

- String searching
- Dictionaries
- Conditional logic
</details>

Detect the mood of a message based on emojis present.

```python
message = input("Enter your message: ")
# Define emojis for different moods (happy, sad, angry)
# Detect emojis in the message and determine mood
```

**Expected Output:**

```
Case 1:
Enter your message: Today was great 😊
Mood detected: Happy 🎉

Case 2:
Enter your message: That's annoying 😡 but also funny 😃
Mood detected: Mixed feelings 🤔
```

---

## 11. Countdown Timer (Difficulty: 3)

<details>
<summary>Topics</summary>

- Loops
- Time functions
- F-strings
</details>

Create a simple countdown timer that counts down from a user-specified number.

```python
import time
count = int(input("Start countdown from: "))
# Count down from the specified number to zero
# Include 1-second delays between counts
```

**Expected Output:**

```
Start countdown from: 3
3... 🕐
2... 🕐
1... 🕐
0... 🎉 Blast off!
```

---

## 12. Grade Calculator (Difficulty: 4)

<details>
<summary>Topics</summary>

- Conditional statements
- Grade boundaries
- String formatting
</details>

Calculate a letter grade based on a numerical score.

```python
score = float(input("Enter test score (0-100): "))
# Determine letter grade based on score ranges
```

**Expected Output:**

```
Case 1:
Enter test score (0-100): 87
Score: 87 = B+

Case 2:
Enter test score (0-100): 65
Score: 65 = D

Case 3:
Enter test score (0-100): 95
Score: 95 = A
```

---

## 13. Currency Converter (Difficulty: 4)

<details>
<summary>Topics</summary>

- Dictionaries
- Conversion rates
- Error handling
</details>

Convert between different currencies using fixed exchange rates.

```python
# Simple exchange rates dictionary
exchange_rates = {"USD": 1.0, "EUR": 0.92, "GBP": 0.78, "JPY": 150.23}

amount = float(input("Amount: "))
from_currency = input("From currency (USD/EUR/GBP/JPY): ").upper()
to_currency = input("To currency (USD/EUR/GBP/JPY): ").upper()
# Convert between currencies
```

**Expected Output:**

```
Case 1:
Amount: 100
From currency (USD/EUR/GBP/JPY): USD
To currency (USD/EUR/GBP/JPY): EUR
100.00 USD = 92.00 EUR 💱

Case 2:
Amount: 50
From currency (USD/EUR/GBP/JPY): GBP
To currency (USD/EUR/GBP/JPY): JPY
50.00 GBP = 9629.49 JPY 💱
```

---

## 14. Word Guessing Game (Difficulty: 4)

<details>
<summary>Topics</summary>

- Random selection
- Loops
- String comparison
- Pattern matching
</details>

Create a simple word guessing game with emoji hints.

```python
import random
words = ["solar", "pilot", "dance", "brain", "water"]
secret_word = random.choice(words).lower()
max_attempts = 5
# Implement guessing logic with emoji feedback
```

**Expected Output:**

```
I'm thinking of a 5-letter word.
Guess 1: slate
Hint: 🟩⬜⬜⬜⬜
Guess 2: sugar
Hint: 🟩🟩⬜⬜⬜
Guess 3: solar
Hint: 🟩🟩⬜🟩🟩
Guess 4: sonar
Hint: 🟩🟩⬜🟩🟩
Guess 5: solar
Correct! The word was SOLAR ⭐
```

---

## 15. Personal Finance Tracker (Difficulty: 5)

<details>
<summary>Topics</summary>

- Dictionary data structure
- Numerical calculations
- Percentages
- Conditional output
</details>

Create a simple income and expense tracker with budget warnings.

```python
income = float(input("Enter your monthly income: $"))
# Get expenses for standard categories (rent, food, etc.)
# Calculate total expenses and remaining balance
# Determine budget status with appropriate emoji
```

**Expected Output:**

```
Case 1:
Enter your monthly income: $3000
Enter rent expense: $1000
Enter food expense: $400
Enter other expenses: $800

💰 Financial Summary 💰
Income: $3000.00
Expenses: $2200.00
Balance: $800.00
Status: 😊 (26.7% of income remaining - Good job!)

Case 2:
Enter your monthly income: $2000
Enter rent expense: $1200
Enter food expense: $500
Enter other expenses: $400

💰 Financial Summary 💰
Income: $2000.00
Expenses: $2100.00
Balance: -$100.00
Status: 🚨 (Overspent by 5.0% - Time to budget better!)
```
