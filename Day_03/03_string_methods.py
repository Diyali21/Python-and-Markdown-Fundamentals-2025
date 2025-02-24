fav_movie = "John Wick"

# Only J

# Index
print(fav_movie[0])
print(fav_movie[5])

# Negative Index
print(fav_movie[-1])
print(fav_movie[-2])

# Only 'Wick'
print(fav_movie[-4] + fav_movie[-3] + fav_movie[-2] + fav_movie[-1])

# Slice Operator (:)
print(fav_movie[2:6])  # hn W
print(fav_movie[2:8])  # hn Wic
print(fav_movie[2:9])  # hn Wick

print(fav_movie[2:])  # hn Wick

# Copy string
print(fav_movie[0:])  # John Wick
print(fav_movie[:])  # John Wick

# Only 'Wick'
print(fav_movie[5:9])
print(fav_movie[5:])
print(fav_movie[-4:])

print(fav_movie[2:9:1])  # hn Wick
print(fav_movie[2:9:2])  # h ick

# Reverse string, step < 0
print(fav_movie[::-1])  # kciW nhoJ
print(fav_movie[-4::-1])  # W nhoJ

print(fav_movie[-4:-2:-1])  # W nhoJ
print(fav_movie[-4:-9:-1])  # W nho


# Immutable - cannot modify
fav_hero = "The Hulk"

# Output
# The hulk
print(fav_hero[:4] + "h" + fav_hero[5:])

# Case modifying methods
catchphrase = "I am Groot"

print(catchphrase.upper())  # I AM GROOT
print(catchphrase.lower())  # i am groot
print(catchphrase.capitalize())  # I am groot
print(catchphrase.title())  # I Am Groot
print(catchphrase.swapcase())  # i AM gROOT


# Strip - remove only leading & trailing characters
message = "  With great power comes great responsibility   "
clean_message = message.strip()
print(clean_message)

coded_message = "********SO*S******"
decoded = coded_message.strip("*")
print(decoded)  # SO*S

# message.lstrip()
# message.rstrip()

# How many times Dream is repeated?
quote = "Dream is not something that you see in sleep, Dream is something that does not let you sleep"
print(quote.count("Dream"))

# Dream -> 🛌💭
print(quote.replace("Dream", "🛌💭", 1))

print(quote.find("something"))  # 13
print(quote.find("**"))  #  -1
