# # Conditionals (Control Flow)
# # Take a choice -> Choice


# # if...else
# # if no_of_person <= 2 -> bike else car

# no_of_person = 10

# # Condition return boolean | if expects a boolean
# if no_of_person <= 2:
#     print("We will take the bike for the party")
# else:
#     print("We will take the car for the party")

# name1 = input("Enter name for person 1: ")
# name2 = input("Enter name person 2: ")
# height1 = float((input("Enter height person 1: ")))
# height2 = float((input("Enter height person 2: ")))


# if height1 > height2:
#     print(f"{name1} is taller than {name2} by: {(height1 - height2)} cm")
# else:
#     print(f"{name2} is taller than {name1} by: {(height2 - height1)} cm")


# # Task 1.2
# # Case 3:
# # Ethan, Luvuyo
# # 185cm, 185cm
# # Ethan and Luvuyo are of the same height
# # Clue: elif
# name1 = input("Enter name for person 1: ")
# name2 = input("Enter name person 2: ")
# height1 = float((input("Enter height person 1: ")))
# height2 = float((input("Enter height person 2: ")))


# if height1 > height2:
#     print(f"{name1} is taller than {name2} by: {(height1 - height2)} cm")
# elif height1 == height2:
#     print(f"{name1} and {name2} are of the same height")
# else:
#     print(f"{name2} is taller than {name1} by: {(height2 - height1)} cm")


# # Task 1.3
# # Improve code quality
# # Clue: abs()

# name1 = input("Enter name for person 1: ")
# name2 = input("Enter name for person 2: ")
# height1 = float((input("Enter height for person 1: ")))
# height2 = float((input("Enter height for person 2: ")))
# difference = abs(height1 - height2)


# if height1 > height2:
#     print(f"{name1} is taller than {name2} by: {difference} cm")
# elif height1 == height2:
#     print(f"{name1} and {name2} are of the same height")
# else:
#     print(f"{name2} is taller than {name1} by: {difference} cm")


stock1 = "vanilla"
stock2 = "chocolate"
stock3 = "tin roof"
stock4 = "cookie dough"

# Output
# Case 1
# Please enter your fav 🍧?: VAnilla
# Yes, we have vanilla in stock

# Case 2
# Please enter your fav 🍧?: salted Caramel
# Sorry, we ran out of Salted Caramel

# Task 1.1
# Clue: if..elif..else

ice_cream = input("Please enter your fav 🍧?: ").lower()

if ice_cream == stock1:
    print(f"Yes, we have {stock1} in stock")
elif ice_cream == stock2:
    print(f"Yes, we have {stock2} in stock")
elif ice_cream == stock3:
    print(f"Yes, we have {stock3} in stock")
elif ice_cream == stock4:
    print(f"Yes, we have {stock4} in stock")
else:
    print(f"Sorry, we ran out of {ice_cream.title()}")


# Task 1.2
#  Clue: or
ice_cream = input("Please enter your fav 🍧?: ").lower().strip()

if (
    (ice_cream == stock1)
    or (ice_cream == stock2)
    or (ice_cream == stock3)
    or (ice_cream == stock4)
):
    print(f"Yes, we have {ice_cream} in stock")
else:
    print(f"Sorry, we ran out of {ice_cream.title()}")

# Task 1.3
ice_cream = input("Please enter your fav 🍧?: ").lower().strip()

if ice_cream in [stock1, stock2, stock3, stock4]:
    print(f"Yes, we have {ice_cream} in stock")
else:
    print(f"Sorry, we ran out of {ice_cream.title()}")
