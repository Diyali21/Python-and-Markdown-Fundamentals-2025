# In python
# Function treated first class citizen (value)


# Rules
# 1. Assign to variable
# 2. Pass as argument
# 3. Returned


# Rules
# 1. Function: Assign to variable
# 2. Function: Pass as argument
# 3. Function: Returned

# 1. Assign to variable
# x = 1


# def greet(name):
#     return f"Hi, {name}"


# print(type(greet))  # <class 'function'>
# # print(type(greet("Jevan")))

# # 1. Assign to variable
# y = greet  # function

# print(y("Jamie"))  # Hi, Jamie


# 2. Function: Pass as argument


def say_hello():
    return "Hello, "


# # 2. Function: Pass as argument - say_hello (function) is passed as argument
def greeting(hello_msg, name):
    print(hello_msg() + name)


greeting(say_hello, "Python!")

# Functional languages - F#, Haskell, Scala - Recursion

# print(say_hello())


# 3. Function: Returned


def f1():
    def f2():
        return "Hi 😄🤚"

    return f2


# Make it print -  "Hi 😄🤚"


x = f1()  # f2
print(x())  # f2()

print(f1()())  # f2()

print(f1()())


# Rules
# 1. Function: Assign to variable
# 2. Function: Pass as argument
# 3. Function: Returned
