def greet(name):
    return f"Hi, {name}"


# Lambda expression/ Lambda Function: Function one liner

greet1 = lambda name: f"Hi, {name}"

print(greet("Jevan"))
print(greet1("Jevan"))


# Lambda expression
# 1. Anonymous - nameless function
# 2. One liner
# 3. Implicit return (automatically)


def add(n1, n2):
    return n1 + n2


add1 = lambda n1, n2: n1 + n2

print(add1(9, 8))


# map & filter


player_stats = [10, 30, 60]
boosted_stats = map(lambda x: x * 2, player_stats)
print(boosted_stats, list(boosted_stats))

# map -> fn -> Takes another fn as arg
# map -> Higher order functions
boosted_stats = map(lambda x: x * 2, [10, 30, 60])

dbl = lambda x: x * 2
boosted_stats = map(dbl, [10, 30, 60])

print(boosted_stats, list(boosted_stats))


def dbl1(x):
    return x * 2


boosted_stats = map(dbl1, [10, 30, 60])
print(boosted_stats, list(boosted_stats))


boosted_stats = map(lambda x: x * 2, player_stats)
print(boosted_stats, list(boosted_stats))

# 1. def - Reuse else where
# 2. lambda - one time use, concise


# filter -> HOF function
# HOF -> map, filter
# result = filter(lambda x: x > 10, [10, 30, 60])
# print(result, list(result))

gt1 = lambda x: x > 10  # Predicate: fn Returns boolean
result = filter(gt1, [10, 30, 60])
print(result, list(result))

# gt1(10) -> F
# gt1(30) -> T
# gt1(60) -> T
# [30, 60]

player_stats = [10, 30, 60]
boosted_stats = map(lambda x: x * 2, player_stats)
print(boosted_stats, list(boosted_stats))
print(player_stats)

# map
# 1. len(Input_list) == len(Output_list)
# 2. Transform data type
# 3. Does not affect the Input list

player_stats = [10, 30, 60]
result = filter(gt1, player_stats)
print(result, list(result))
print(player_stats)

# filter
# 1. len(Input_list) >= len(Output_list)
# 2. Input data_type == Output data_type
# 3. Does not affect the Input list
