# scrambled_message = "world the save to time no is there"

# # Output
# # there is no time to save the world

# scrambled_list = scrambled_message.split(" ")

# unscrambled_list = scrambled_list[::-1]

# unscrambled_str = " ".join(unscrambled_list)

# print(unscrambled_str)


import math

points = [(3, 4), (6, 12), (10, 13)]

# Expected Output
# distances = [5.0, 13.42, 16.4]

distances = []

for point in points:
    a, b = point
    d = math.sqrt(a**2 + b**2)
    distances.append(round(d, 2))
print(distances)
