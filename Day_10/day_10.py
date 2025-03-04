# # def f1():
# #     def f2():
# #         print("Hello")

# #     return f2


# # print(f1()())


# # add1 = lambda n1, n2: n1 + n2
# # print(add1(1, 2))

# # player_stats = [10, 30, 60]

# # boosted_stats = map(lambda x: x * 2, player_stats)

# # print(boosted_stats, list(boosted_stats))


# avengers = [
#     "Hulk",
#     "Iron man",
#     "Black widow",
#     "Captain america",
#     "Spider man",
#     "Thor",
# ]

# # Task (map or filter)
# # Number letter in the name
# # [4, 8, 11, 15, 10, 4]


# letter_name = map(lambda num: len(num), avengers)
# print(letter_name, list(letter_name))

# # Task 1.2

# # Find longer names more the 10 letters name and stored in a new list

# # Output
# # ["Black widow", "Captain america"]


# longer_name = filter(lambda num: len(num) > 10, avengers)
# print(longer_name, list(longer_name))


# scores = [
#     {
#         "marks": 32,
#         "name": "Yvette Merritt",
#     },
#     {
#         "marks": 57,
#         "name": "Lillian Ellis",
#     },
#     {
#         "marks": 22,
#         "name": "Mccall Carter",
#     },
#     {
#         "marks": 21,
#         "name": "Pate Collier",
#     },
#     {
#         "marks": 91,
#         "name": "Debra Beard",
#     },
#     {
#         "marks": 75,
#         "name": "Nettie Hancock",
#     },
#     {
#         "marks": 20,
#         "name": "Hatfield Hodge",
#     },
# ]


# # Task 1.3

# # Find the passed student's names (pass criteria >= 40)

# # Output
# # ["Lillian Ellis", "Debra Beard",  "Nettie Hancock" ]


# stud_marks = list(filter(lambda student: student["marks"] >= 40, scores))
# names = list(map(lambda student: student["name"], stud_marks))

# print(names)


# # Task 1.4
# topper = list(sorted(scores, key=lambda student: student["marks"]))
# print(topper[-1]["name"])


# num = 5


# def multiply_num():
#     global num
#     num = num * 2


# print("Old num = ", num)

# multiply_num()

# print("New num = ", num)


def msg1():
    singer = "Dua Lipa"

    def msg2():
        singer = "dua lipa is the best singer"

        def msg3():
            nonlocal singer
            singer = "Dua Lipa is the greatest singer of all time"
            print(singer)

        msg3()
        print(singer)

    msg2()
    print(singer)


msg1()
