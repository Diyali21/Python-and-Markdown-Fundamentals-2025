# print("Vote for Jevan")
# print("Vote for Jevan")
# print("Vote for Jevan")

# Refactor in while loop

# i = 1
# while i <= 3:
#     print("Vote for Jevan 🎊")
#     i = i + 1

# print("Voting ended 🎊")

# Refactor in for loop
# for and range (pair)

# for i in range(3):
#     print(i)

# for i in range(1,11):
#     print(i)


# Task
# Print only odd numbers for 1 to 50

# # Task 1.1 (Hard)
# for i in range(1, 51):
#     if i % 2 != 0:
#         print(i)

# # Task 1.2 (Easy)
# for i in range(1, 51, 2):
#     print(i)

# Task 1.3 Refactor in for loop
# for and range 'Vote for Jevan 🎊'

# for i in range(3):
#     print("Vote for Jevan 🎊")

# print("Voting ended 🎊")


# Task 1.1
# While loop
# 🔥
# 🔥🔥
# 🔥🔥🔥
# 🔥🔥🔥🔥
# 🔥🔥🔥🔥🔥


# Task 1.2
# Refactoring with for Loop
# 🔥
# 🔥🔥
# 🔥🔥🔥
# 🔥🔥🔥🔥
# 🔥🔥🔥🔥🔥


# Task 1.3 (with while loop)
# Output
# Please tell the no of rows?: 3
# Please tell the pattern?: 🍧
# 🍧
# 🍧🍧
# 🍧🍧🍧


# Task 1.4 (Refactor with for loop)
# Clue: range has 3 arguments
# Output
# Please tell the no of rows?: 3
# Please tell the pattern?: 🍧
# 🍧
# 🍧🍧
# 🍧🍧🍧

# Task 1.1
i = 1
while i <= 5:
    print("🔥" * i)
    i = i + 1


# Task 1.2
for i in range(1, 6):
    print("🔥" * i)

# Task 1.3
iRows = int(input("Please tell the no. of rows?: "))
sEmoji = input("Please tell the pattern?: ")

i = 1
while i <= iRows:
    print(sEmoji * i)
    i = i + 1

# Task 1.4
iRows = int(input("Please tell the no. of rows?: "))
sEmoji = input("Please tell the pattern?: ")

for i in range(1, iRows + 1):
    print(sEmoji * i)

# This is nice line added 🍧
shopping_items = [1000, 5000, 4000, 2000, 3000]
sum_items = 0

for item in shopping_items:
    sum_items = sum_items + item

tax = sum_items * 0.1
total = sum_items + tax
print(
    f"""
Your total is R{sum_items})
Tax is 10%   R{tax}
Your grand total is R{total}
"""
)
