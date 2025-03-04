# Scope of variable
# Lifetime of variable
# Area in which the variable alive (which line no. to which line no.)


# t1 = 100

# # t2 -> simple function scope
# # Can't access t2 outside

# def simple():
#     t2 = 10


# simple()
# print(t1)
# print(t2) # NameError: name 't2' is not defined ❌


price = 100


def get_price():
    print("The price of the book is: ", price)


get_price()

# get_price
# 1. First checks for local `price` variable
# 2. Then goes to outer scope (Lexical scope)

# Case 2:
