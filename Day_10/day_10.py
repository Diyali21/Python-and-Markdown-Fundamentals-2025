# def f1():
#     def f2():
#         print("Hello")

#     return f2


# print(f1()())


add1 = lambda n1, n2: n1 + n2
print(add1(1, 2))

player_stats = [10, 30, 60]

boosted_stats = map(lambda x: x * 2, player_stats)

print(boosted_stats, list(boosted_stats))
