# Task 1.1
# Please tell me your year of birth 2000
# Your age is 25

# from datetime import datetime

# def calculate_age():
#     age_year = int(input("Please enter your year of birth: "))
#     return f"Your age is {datetime.now().year - age_year}"

# Task 1.2
# Handling Error

# from datetime import datetime


# def calculate_age():

#     try:
#         age_year = int(input("Please enter your year of birth: "))
#         return f"Your age is {datetime.now().year - age_year}"

#     except ValueError as err:
#         return f"Please enter a whole number {err}"


# print(calculate_age())


from datetime import datetime


def calculate_age():
    try:
        age_year = int(input("Please enter your year of birth: "))

        current_year = datetime.now().year

        if age_year <= 0:
            raise ValueError("Year cannot be negative")

        if age_year > current_year:
            raise ValueError("You're not flash to be from the future 🚀")

        return f"Your age is {current_year - age_year}"

    except ValueError as err:
        return f"Invalid {err}"


print(calculate_age())
