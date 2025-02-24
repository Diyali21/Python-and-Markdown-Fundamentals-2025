# Control Flow

## Conditionals

### if...elif

```py
ice_cream = input("Please enter your fav 🍧?: ").lower().split()

if ice_cream == stock1:
    print(f"Yes, we have {stock1} in stock")
elif ice_cream == stock2:
    print(f"Yes, we have {stock2} in stock")
elif ice_cream == stock3:
    print(f"Yes, we have {stock3} in stock")
elif ice_cream == stock4:
    print(f"Yes, we have {stock4} in stock")
else:
    print(f"Sorry, we ran out of {ice_cream.title()}")
```

### or

```py
ice_cream = input("Please enter your fav 🍧?: ").lower().strip()

if (
    (ice_cream == stock1)
    or (ice_cream == stock2)
    or (ice_cream == stock3)
    or (ice_cream == stock4)
):
    print(f"Yes, we have {ice_cream} in stock")
else:
    print(f"Sorry, we ran out of {ice_cream.title()}")
```

### in

```py
ice_cream = input("Please enter your fav 🍧?: ").lower().strip()

if ice_cream in [stock1, stock2, stock3, stock4]:
    print(f"Yes, we have {ice_cream} in stock")
else:
    print(f"Sorry, we ran out of {ice_cream.title()}")
```

## Loops

Pupose: Simply repeating statements

```py
print("Vote for Jevan")
print("Vote for Jevan")
print("Vote for Jevan")
```

### `while loops`

Executes the statement while the condition is True

```py
i = 1
while i <= 3:
    print("Vote for Jevan 🎊")
    i = i + 1

print("Voting ended 🎊")
```

### `for loops`

`for` and `range` (pair)

1. `range` always starts with 0
2. `range` excludes the ended

```py
for i in range(3):
    print(i) #0 1 2
```

3. `range(start, end, step)`
4. `range(3) ➡️ range(end)`
5. `for` and `range` takes care of `incrementing 'i'`
6. step ➡️ default is `1`

## Intro to Git

- Commit at least 3 times in an hour - Logical changes - commit
- Version control for your project
- Be confident with your change
- Linus Torvalds - side project made Git to maintain Linus - 2007
- Git - Does not need internet | On plane

1. git init
2. Stage all
3. Provide message - Why? > What?
4. When to commit
   1. Commit at least 3 times in an hour
   2. Logical commit - Complete commit (No bugs)
   3. Small commit - Don't commit > 10 files
5. Commit (Save point)
6. Sync to github (online)

### Git vs Github

- `Git` - Version control system - Does not need internet
- `Github` - like GoogleDrive (Storing files)
