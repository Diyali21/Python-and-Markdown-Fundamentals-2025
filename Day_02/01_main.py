# variable_name = value
name = "Chleo"
age = 20
balance = 1000000.50
is_rich = True

print(name)
print(age)
print(balance)

# Dynamically typed -> Python smart

print(type(name))  # <class 'str'>
print(type(age))  # <class 'int'>
print(type(balance))  # <class 'float'>
print(type(is_rich))  # <class 'bool'>

# My name is Chleo
print("My name is " + name)

# My age is 20
# str + int -> ❌
print("My age is " + str(age))
# Type conversions
# str, int, float, bool

# fstring - imporves DX
# {} -> interpolation
# {} -> expressions are allowed
# Auto converts
# Readable
print(f"My age is {age}")
print(f"She has {2 * 1000} followers 🎊s")
