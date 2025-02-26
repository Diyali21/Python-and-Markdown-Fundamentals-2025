# scrambled_message = "world the save to time no is there"

# # Output
# # there is no time to save the world

# scrambled_list = scrambled_message.split(" ")

# unscrambled_list = scrambled_list[::-1]

# unscrambled_str = " ".join(unscrambled_list)

# print(unscrambled_str)


books = [
    {"title": "Infinite Jest", "rating": 4.5, "genre": "Fiction"},
    {"title": "The Catcher in the Rye", "rating": 3.9, "genre": "Fiction"},
    {"title": "Sapiens", "rating": 3.9, "genre": "History"},
    {"title": "A Brief History of Time", "rating": 4.8, "genre": "Science"},
    {"title": "Clean Code", "rating": 4.7, "genre": "Technology"},
]

# titles = []
# for book in books:
#     if book["rating"] >= 4.7:
#         titles.append(book["title"])

# if len(titles) >= 2:
#     and_index = len(titles) - 1
#     titles.insert(and_index, "and")
# title_str = ", ".join(titles)
# print(title_str)
# output = title_str.replace(", and,", " and")
# print(f"Highest rated books are: {output}")
