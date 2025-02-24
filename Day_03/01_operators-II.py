# Task 3
# Output (Assume PI - 3.14)
# Provide the radius of the circle: 4.2
# Area of cicle is 55.3896

# PI = 3.14
# radius = float(input("Provide the radius of the circle: "))
# area = PI * radius**2  # readability helps devs
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
space = (10 - num1) * " "
print(f"[{output}{space}] {num}%")
