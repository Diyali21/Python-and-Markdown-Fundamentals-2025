# Day 2
# Question 1
## 1. Name Tag Generator (Difficulty: 1) ✔️
# <details>
# <summary>Topics</summary>

# - String manipulation
# - F-strings
# - User input
# </details>

# Create a program that asks for a name and prints a decorated name tag.

# ```python
# name = input("Enter your name: ")
# # Convert to uppercase and print decorated name
# ```

# **Expected Output:**
# ```
# Enter your name: Maria
# ✨ Hello, MARIA! ✨
# ```

# **Hint:** Use string methods and f-strings.

name = input("Enter your name: ")
print(f"✨ Hello, {name.upper()}! ✨")

# -------------------------------------------------------------------------------------------------------------

# Question 2
## 2. Age Calculator (Difficulty: 1)
# <details>
# <summary>Topics</summary>

# - Basic arithmetic
# - Type conversion
# - F-strings
# </details>

# Calculate someone's age based on their birth year.

# ```python
# birth_year = int(input("Enter birth year: "))
# current_year = 2025
# # Calculate and display age
# ```

# **Expected Output:**
# ```
# Enter birth year: 2000
# You are 25 years old in 2025.
# ```

# ---

birth_year = int(input("Enter birth year: "))
current_year = 2025

print(f"You are {current_year - birth_year} years old in {current_year}")
# ------------------------------------------------------------------------------------------

# 3. Emoji Replacer (Difficulty: 2)
# <details>
# <summary>Topics</summary>

# - Dictionaries
# - String methods
# - String replacement
# </details>

# Replace certain words in a sentence with emojis.

# ```python
# emoji_dict = {"love": "❤️", "pizza": "🍕", "happy": "😊"}
# sentence = input("Enter a sentence: ")
# # Replace matching words with emojis
# ```

# **Expected Output:**
# ```
# Case 1:
# Enter a sentence: I love coding and pizza
# I ❤️ coding and 🍕

# Case 2:
# Enter a sentence: The weather is nice today
# The weather is nice today
# ```

# ---
emoji_dict = {"love": "❤️", "pizza": "🍕", "happy": "😊"}
sentence = input("Enter a sentence: ")

emoji_list = sentence.split(" ")

keys_str = ""

for keys in emoji_dict.keys():
    keys_str = keys_str + keys + " "

for i in range(len(sentence)):
    if sentence[i] in keys_str[i]:
        print("hi")
