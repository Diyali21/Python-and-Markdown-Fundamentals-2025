# 🎮 Python Day 3: Fun & Practical Exercises 🚀

## 1. Emoji Battery Indicator (Difficulty: 1)
<details>
<summary>Topics</summary>

- Floor division
- String repetition
- F-strings
</details>

Create a fun battery indicator using emojis based on battery percentage.

```python
battery = int(input("Enter battery percentage (0-100): "))
# Create an emoji battery indicator that shows the battery level
```

**Expected Output:**
```
Enter battery percentage (0-100): 70
Battery: [🔋🔋🔋🔋🔋🔋🔋⬜⬜⬜] 70%
Power status: Good charge! 👍
```

**Hint:** Use floor division to determine how many battery emoji symbols to display.

---

## 2. Superhero Power Level (Difficulty: 2)
<details>
<summary>Topics</summary>

- Exponentiation operator
- Conditional statements
- F-strings
</details>

Calculate a superhero's power level based on strength and experience.

```python
name = input("Enter superhero name: ")
strength = int(input("Enter strength (1-10): "))
experience = int(input("Enter years of experience: "))
# Calculate power level using exponentiation and create a hero card
```

**Expected Output:**
```
Enter superhero name: Thunder Woman
Enter strength (1-10): 8
Enter years of experience: 5

⚡ HERO CARD ⚡
Name: Thunder Woman
Power Level: 32768
Rank: Legendary Hero 🏆
```

**Hint:** Calculate power level as strength raised to a power based on experience.

---

## 3. Movie Ticket Pricing (Difficulty: 2)
<details>
<summary>Topics</summary>

- Modulo operator
- Conditional statements
- String formatting
</details>

Calculate movie ticket prices based on age and day of the week.

```python
age = int(input("Enter age: "))
day = int(input("Enter day of week (1-7, where 1 is Monday): "))
# Calculate ticket price based on age and day
# Use modulo to check if it's a weekend (day 6-7)
```

**Expected Output:**
```
Case 1:
Enter age: 25
Enter day of week (1-7, where 1 is Monday): 3
Standard Ticket: $12.00 🎬
Enjoy your movie on Wednesday!

Case 2:
Enter age: 14
Enter day of week (1-7, where 1 is Monday): 6
Child Ticket: $8.00 🎬
Weekend Surcharge: $2.00 📈
Total: $10.00
Enjoy your movie on Saturday!
```

---

## 4. Secret Message Decoder (Difficulty: 2)
<details>
<summary>Topics</summary>

- String slicing
- String methods
- Reverse operations
</details>

Decode a secret message using various string manipulation techniques.

```python
coded_message = input("Enter the coded message: ")
# Decode by: 
# 1. Reversing the string
# 2. Taking every second character
# 3. Converting to uppercase
```

**Expected Output:**
```
Enter the coded message: eNcPtIhYsS iA eFcReEtT mOsSaGeE
Secret message: MESSAGE IS SECRET
```

**Hint:** Try combining string slicing with step values and other string methods.

---

## 5. Social Media Username Generator (Difficulty: 2)
<details>
<summary>Topics</summary>

- String methods (replace, lower)
- String concatenation
- Conditional statements
</details>

Create a username generator for social media based on user input.

```python
full_name = input("Enter your full name: ")
birth_year = input("Enter your birth year: ")
favorite_thing = input("Enter something you love: ")
# Generate a unique username with no spaces and special character replacement
```

**Expected Output:**
```
Enter your full name: John Smith
Enter your birth year: 1995
Enter something you love: Basketball

🔥 Username options:
1. john_smith95
2. j.smith_bball
3. bball_lover_95
4. john1995🏀
```

---

## 6. Emoji Mood Message (Difficulty: 3)
<details>
<summary>Topics</summary>

- String methods (find, replace)
- Conditional statements
- String formatting
</details>

Create a program that analyzes text messages and adds appropriate mood emojis.

```python
message = input("Enter your message: ")
# Analyze the message for mood keywords and add emojis
# Words like "happy", "love", "excited" should add positive emojis
# Words like "sad", "angry", "tired" should add negative emojis
```

**Expected Output:**
```
Case 1:
Enter your message: I am so happy today because I love programming
Enhanced: I am so happy 😊 today because I love ❤️ programming

Case 2:
Enter your message: I'm feeling tired and a bit sad
Enhanced: I'm feeling tired 😴 and a bit sad 😢
```

---

## 7. Adventure Game Choice (Difficulty: 3)
<details>
<summary>Topics</summary>

- Conditional statements (if-elif-else)
- User input
- String methods
</details>

Create a mini text adventure game with branching choices.

```python
print("🏰 Welcome to the Enchanted Forest 🌲")
print("You encounter a fork in the path.")
choice = input("Do you go left, right, or straight ahead? ").lower()
# Create different outcomes based on user's choice
```

**Expected Output:**
```
Case 1:
🏰 Welcome to the Enchanted Forest 🌲
You encounter a fork in the path.
Do you go left, right, or straight ahead? left
You follow the left path and discover a hidden treasure chest! 💰
It contains 50 gold coins and a magic amulet! ✨

Case 2:
🏰 Welcome to the Enchanted Forest 🌲
You encounter a fork in the path.
Do you go left, right, or straight ahead? right
You take the right path and come across a friendly dragon! 🐉
It offers to fly you to the nearest village.
```

---

## 8. Weather Outfit Advisor (Difficulty: 3)
<details>
<summary>Topics</summary>

- Conditional statements with multiple conditions
- Comparison operators
- Logical operators
</details>

Recommend what to wear based on weather conditions.

```python
temperature = float(input("Enter temperature in Celsius: "))
is_raining = input("Is it raining? (yes/no): ").lower() == "yes"
is_windy = input("Is it windy? (yes/no): ").lower() == "yes"
# Make outfit recommendations based on conditions
```

**Expected Output:**
```
Case 1:
Enter temperature in Celsius: 28
Is it raining? (yes/no): no
Is it windy? (yes/no): no
Weather: Hot and clear ☀️
Recommendation: Wear light clothes, sunglasses, and don't forget sunscreen! 😎

Case 2:
Enter temperature in Celsius: 5
Is it raining? (yes/no): yes
Is it windy? (yes/no): yes
Weather: Cold, rainy, and windy 🌧️
Recommendation: Wear a heavy coat, waterproof boots, and bring an umbrella! Stay warm! 🧥
```

---

## 9. Emoji Code Breaker (Difficulty: 3)
<details>
<summary>Topics</summary>

- String methods (count, replace)
- Conditional logic
- String manipulation
</details>

Decode a message where emojis have been used to hide the real message.

```python
emoji_message = input("Enter the emoji-encoded message: ")
# Extract the hidden message from emoji patterns
# Example rules:
# - Every character after 🔑 is part of the message
# - 🔒 means ignore the next character
# - 💫 means repeat the previous character
```

**Expected Output:**
```
Enter the emoji-encoded message: hi🔑c🔒zo💫de
Decoded message: CODE
```

---

## 10. Rock Paper Scissors Game (Difficulty: 3)
<details>
<summary>Topics</summary>

- Conditional statements
- Logical comparisons
- Random selection
</details>

Create a simple Rock, Paper, Scissors game with emoji feedback.

```python
import random

choices = ["rock", "paper", "scissors"]
computer_choice = random.choice(choices)
player_choice = input("Choose rock, paper, or scissors: ").lower()
# Determine winner using conditionals and display with emojis
```

**Expected Output:**
```
Case 1:
Choose rock, paper, or scissors: rock
Computer chose: paper 📄
You chose: rock 🪨
Paper covers rock! You lose! 😢

Case 2:
Choose rock, paper, or scissors: scissors
Computer chose: paper 📄
You chose: scissors ✂️
Scissors cut paper! You win! 🎉
```

---

## 11. Password Validator (Difficulty: 4)
<details>
<summary>Topics</summary>

- Logical operators
- String methods
- Complex conditionals
</details>

Create a password validator with specific requirements and emojis for feedback.

```python
password = input("Create a password: ")
# Check if password meets these requirements:
# - At least 8 characters long
# - Contains at least one uppercase letter
# - Contains at least one number
# - Contains at least one special character (!@#$%^&*)
```

**Expected Output:**
```
Create a password: pass123
❌ Password must be at least 8 characters long
❌ Password must contain at least one uppercase letter
❌ Password must contain at least one special character
Password strength: Weak 🔓

Create a password: Password123!
✅ Length requirement met
✅ Uppercase requirement met
✅ Number requirement met
✅ Special character requirement met
Password strength: Strong 🔒
```

---

## 12. Movie Rating Analyzer (Difficulty: 4)
<details>
<summary>Topics</summary>

- String manipulation
- Conditional logic
- Formatting output
</details>

Analyze a movie description and rating to provide personalized recommendations.

```python
movie_name = input("Enter movie title: ")
genre = input("Enter genre: ")
rating = float(input("Enter rating (0-10): "))
length = int(input("Enter movie length in minutes: "))
# Analyze movie details and provide tailored recommendations
```

**Expected Output:**
```
Enter movie title: The Matrix
Enter genre: sci-fi
Enter rating (0-10): 8.7
Enter movie length in minutes: 136

🎬 Movie Analysis: The Matrix
Rating: ⭐⭐⭐⭐⭐ 8.7/10 (Excellent!)
Length: 136 mins (Standard feature length)
Recommendation: Must-watch for sci-fi fans! 🤖
Perfect for: Weekend movie night with friends 🍿
```

---

## 13. Fitness Goal Calculator (Difficulty: 4)
<details>
<summary>Topics</summary>

- Complex conditionals
- Math operations
- String formatting
</details>

Calculate fitness goals and provide motivational feedback.

```python
weight = float(input("Enter your current weight (kg): "))
goal_weight = float(input("Enter your goal weight (kg): "))
weekly_exercise = int(input("How many times do you exercise per week? "))
# Calculate timeframe to reach goal and provide motivational message
```

**Expected Output:**
```
Case 1:
Enter your current weight (kg): 85
Enter your goal weight (kg): 75
How many times do you exercise per week? 3

🏋️ Fitness Goal Analysis 🏋️
Weight change needed: 10.0 kg (lose)
Estimated weekly loss: 0.5 kg
Estimated time to goal: 20 weeks
Motivation level: Good! 👍
Tip: Adding one more workout per week could reduce time to 16 weeks! 💪

Case 2:
Enter your current weight (kg): 60
Enter your goal weight (kg): 65
How many times do you exercise per week? 4

🏋️ Fitness Goal Analysis 🏋️
Weight change needed: 5.0 kg (gain)
Estimated weekly gain: 0.3 kg
Estimated time to goal: 17 weeks
Motivation level: Excellent! 🌟
Tip: Ensure adequate protein intake for muscle gain! 🥩
```

---

## 14. Emoji Story Generator (Difficulty: 4)
<details>
<summary>Topics</summary>

- String concatenation
- Conditional logic
- String methods
</details>

Create a program that generates a short story with emojis based on user input.

```python
character = input("Choose a character (wizard/knight/explorer): ").lower()
setting = input("Choose a setting (forest/castle/mountain): ").lower()
item = input("Choose a magical item: ").lower()
# Generate a story with emojis based on the inputs
```

**Expected Output:**
```
Choose a character (wizard/knight/explorer): wizard
Choose a setting (forest/castle/mountain): forest
Choose a magical item: wand

🧙 THE MAGICAL ADVENTURE 🧙

Once upon a time, a powerful wizard 🧙‍♂️ ventured into the enchanted forest 🌲🌲🌲.
The forest was filled with mysterious creatures 🦊🦉 and glowing plants ✨🌿.
The wizard discovered a magical wand ✨ hidden beneath an ancient tree 🌳.
When the wizard waved the wand, the entire forest lit up with magical light ✨🌟✨!

THE END 📚
```

---

## 15. Smart Shopping Assistant (Difficulty: 5)
<details>
<summary>Topics</summary>

- Complex conditional logic
- String manipulation
- Math operations
</details>

Create a shopping assistant that helps with budget calculations and recommendations.

```python
budget = float(input("Enter your shopping budget: $"))
item1 = input("Enter first item name: ")
price1 = float(input(f"Enter price for {item1}: $"))
item2 = input("Enter second item name: ")
price2 = float(input(f"Enter price for {item2}: $"))
item3 = input("Enter third item name: ")
price3 = float(input(f"Enter price for {item3}: $"))
# Calculate total, check against budget, and make recommendations
```

**Expected Output:**
```
Enter your shopping budget: $100
Enter first item name: Headphones
Enter price for Headphones: $89.99
Enter second item name: Book
Enter price for Book: $15.50
Enter third item name: Coffee
Enter price for Coffee: $4.25

🛒 Shopping Analysis 🛒

Items:
1. Headphones - $89.99
2. Book - $15.50
3. Coffee - $4.25

Subtotal: $109.74
Budget: $100.00
Status: Over budget by $9.74 ⚠️

Recommendations:
- Consider removing Coffee to save $4.25
- You might want to look for cheaper Headphones
- Items 2 and 3 together fit within your budget
```
