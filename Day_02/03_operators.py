# Task 1
# Output
# Please provide your Fahrenheit: 98.6
# The 98.6°F is 37°C

# fahrenheit = float(input("Please provide your Fahrenheit: "))
# degrees = (fahrenheit - 32) * 5 / 9
# print(f"The {fahrenheit}°F is {degrees}°C")


# Task 2
# Output
# Please provide your birth year: 2000
# Your age is 25

# birth_year = input("Please provide your birth year: ")
# age = 2025 - int(birth_year)
# print(f"Your age is {age}")

# Task 3
# Output (Assume PI - 3.14)
# Provide the radius of the circle: 4.2
# Area of cicle is 55.3896

# radius = input("Provide the radius of the circle: ")
# area = 3.14 * (float(radius) ** 2)
# print(f"Area of circles is {area}")


# Task 4
# Task: Build a loader
# Input: 70
# Output: [======= ] 70%

# Input: 23
# Output: [==      ] 23%
num = int(input("Input: "))
num1 = num // 10
output = num1 * "="
print(f"[{output}] {num}%")
