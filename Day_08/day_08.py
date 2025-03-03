# # Task 1
# # Create function


# # greet("Ragav") -> Hi Ragav! 👋
# # greet("Jamie") -> Hi Jamie! 👋


# def greet(name):
#     return f"Hi {name}! 👋"


# print(greet("Ragav"))
# print(greet("Jamie"))


# # Task 2
# # Create a function named driving_test which takes name, age are parameter and returns eligibility

# # Case 1:
# # Anita is eligible for driving.

# # Case 2:
# # Try again after few years 👶🍼


# def driving_test(name, age):
#     if age >= 18:
#         return f"{name} is eligible for driving"
#     else:
#         return "Try again after few years 👶"


# print(driving_test("Anita", 17))


# def pattern(character, number):
#     for i in range(1, number + 1):
#         print(character * i)


# pattern("🥕", 5)


# def pattern(emoji, no):
#     return "\n".join([emoji * i for i in range(1, no + 1)])


# print(pattern("🥔", 3))


# # Task 4


# def greet(name):
#     return(f"Hi {name}! 👋")


# names = ["Anita", "Jamie", "Diyali", "Siyanda"]

# for name in names:
#     print(greet[name]))
# greet(names)
# # Output
# # Hi Anita! 👋
# # Hi Jamie! 👋
# # Hi Diyali! 👋
# # Hi Siyanda! 👋

# Output
# Welcome to our Library app
# Main menu:
# 1. Add book to the library
# 2. Print all the books
# 3. Exit

# Please choose an option: 1
# Please tell me the title?
# Please tell me the author?
# Please tell me the year?
# Please tell me the available?

# Successfully added 😄✅

# Main menu:
# 1. Add book to the library
# 2. Print all the books
# 3. Exit

# Please choose an option: 2

# [
#     {
#         "title": "Python Programming",
#         "author": "Eric Matthes",
#         "year": 2019,
#         "available": True,
#     },
#     {
#         "title": "Automate the Boring Stuff with Python",
#         "author": "Al Sweigart",
#         "year": 2020,
#         "available": True,
#     },
#     {
#         "title": "Learning Python I",
#         "author": "Mark Lutz",
#         "year": 2013,
#         "available": False,
#     },
#     {
#         "title": "Fluent Python",
#         "author": "Luciano Ramalho",
#         "year": 2015,
#         "available": True,
#     },
#     {
#         "title": "Adavance Python",
#         "author": "Mark Lutz",
#         "year": 2015,
#         "available": False,
#     },
# ]

# Main menu:
# 1. Add book to the library
# 2. Print all the books
# 3. Exit

# Bye 😄👋

from ast import main

library_list = [
    {
        "title": "Python Programming",
        "author": "Eric Matthes",
        "year": 2019,
        "available": True,
    },
    {
        "title": "Automate the Boring Stuff with Python",
        "author": "Al Sweigart",
        "year": 2020,
        "available": True,
    },
    {
        "title": "Learning Python I",
        "author": "Mark Lutz",
        "year": 2013,
        "available": False,
    },
    {
        "title": "Fluent Python",
        "author": "Luciano Ramalho",
        "year": 2015,
        "available": True,
    },
    {
        "title": "Adavance Python",
        "author": "Mark Lutz",
        "year": 2015,
        "available": False,
    },
]


def option1():
    books = {}

    title = input("Please tell me the title? ")
    author = input("Please tell me the author? ")
    year = int(input(("Please tell me the year? ")))
    avail = bool(input(("Please tell me the available? ")))

    books["title"] = title
    books["author"] = author
    books["year"] = year
    books["available"] = avail
    library_list.append(books)
    return "Successfully added 😄✅"


def option2():
    return library_list


def option3():
    return "Bye 😄👋"


def main_menu():
    print(f"Main Menu \n1. Add book to the library \n2. Print all the books \n3. Exit")
    option_no = int(input("Please choose an option: "))
    return option_no


print(f"Welcome to our Library app")

books = {}

option = 0
while option != 3:
    option = main_menu()

    if option == 2:
        print(option2())
    elif option == 3:
        print(option3())
    else:
        print(option1())
