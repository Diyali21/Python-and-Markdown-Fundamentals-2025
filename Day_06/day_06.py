# inventory = [
#     {"name": "Apple 🍎", "quantity": 30, "price": 0.5},
#     {"name": "Banana 🍌", "quantity": 20, "price": 0.2},
# ]

# for i in range(len(inventory)):
#     print(inventory[i].get("name"))

captain_america = {
    "name": "Steve Rogers 🦸‍♂️",
    "age": 100,
    "height": 185,
    "address": {"city": "Brooklyn", "country": "US"},
}


spiderman = {
    "name": "Peter Parker",
    "age": 18,
    "team_name": "Avengers",
    "team": ["Iron Man", "Thor", "Hulk", "Captain America"],
}

hulk = {
    "name": "Bruce Banner",
    "age": 35,
}

heroes = [captain_america, spiderman, hulk]

for hero in heroes:
    city = hero.get("address", {}).get("city")
    if city != None:
        print(f"{hero['name']} lives in {city}")
    else:
        print(f"{hero['name']} location is Top Secret 🔒")
