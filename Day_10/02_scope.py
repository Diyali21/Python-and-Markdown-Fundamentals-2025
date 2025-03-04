# Scope of variable
# Lifetime of variable
# Area in which the variable alive (Which line no. to which line no.)

# print(z1)  # NameError: name 'z1' is not defined ❌

# t1 = 100

# t2 (11 - 12)
def simple():
    t2 = 10
    print(t2)


# # t2 -> simple function scope
# # Cannot access t2 outside

# simple()
# print(t1)
# print(t2)   # NameError: name 't2' is not defined ❌

# price = 100


# # Case 1:
# def get_price():
#     print("The price of the book is: ", price)


# get_price()

# get_price
# 1. First checks for local `price` variable
# 2. Then goes to outer scope (Lexical scope)

# Case 2:


code_word = "Hulk"


def space_ship():
    question = "Please provide code word"

    def code_word_check():
        password = "Hulk"
        print(question)

        if password == code_word:
            print(f"Welcome, {password} the strongest avenger 💪")
        else:
            print("❌ Access denied to 🚀")

    code_word_check()


space_ship()
