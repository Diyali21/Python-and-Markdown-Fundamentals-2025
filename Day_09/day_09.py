# def own_max(*nums):
#     max_no = nums[0]
#     for i in nums:
#         if i > max_no:
#             max_no = i
#     return max_no


# print(own_max(9, 6))
# print(own_max(3, 4, 5, 6))
# print(own_max(3, 4, 5, 6, 7, 2, 3, 10, 1))


def mood_report(mood="🙂", time_of_day="🌅"):
    return f"Feeling {mood} this {time_of_day}"


# Example outputs:
print(mood_report())  # "Feeling 🙂 this morning 🌅."
print(
    mood_report(mood="😎", time_of_day="afternoon ☀️")
)  # "Feeling 😎 this afternoon ☀️."

# Task 1.2

books = [
    {"title": "1984", "author": "George Orwell", "year": 1949},
    {"author": "J.K. Rowling"},  # Missing title and year
    {"title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "year": 1925},
    {"title": "To Kill a Mockingbird", "year": 1960},  # Missing author
    {"author": "Ernest Hemingway", "year": 1952},  # Missing title
]


# Output
# '1984' by George Orwell (1949)
# 'Untitled' by J.K. Rowling (N/A)
# 'The Great Gatsby' by F. Scott Fitzgerald (1925)
# 'To Kill a Mockingbird' by Unknown (1960)
# 'Untitled' by Ernest Hemingway (1952)


def format_book_info1(book):
    title = book.get("title", "Untitled")
    author = book.get("author", "Unknown")
    year = book.get("year", "N/A")
    return f"'{title}' by {author} ({year})"


def format_book_info2(
    title="Untitled", author="Unknown", year="N/A"
):  # title -> If None then default value
    return f"'{title}' by {author} ({year})"


def main():
    for book in books:
        print(
            format_book_info2(
                book.get("title"), book.get("author"), book.get("year")
            )  # doesn't work
        )


main()
