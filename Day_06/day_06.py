inventory = [
    {"name": "Apple 🍎", "quantity": 30, "price": 0.5},
    {"name": "Banana 🍌", "quantity": 20, "price": 0.2},
]

item_name = input("What is the product name? ")
item_qty = int(input("What is the quantity? "))
item_price = float(input("What is the price? "))

product = {"name: ": item_name, "quantity: ": item_qty, "price: ": item_price}

inventory.append(product)


continue_input = input("Do you want to continue? ").lower()

while continue_input == "yes":
    item_name = input("What is the product name? ")
    item_qty = int(input("What is the quantity? "))
    item_price = float(input("What is the price? "))

    product = {"name: ": item_name, "quantity: ": item_qty, "price: ": item_price}

    inventory.append(product)
    continue_input = input("Do you want to continue? ").lower()

print(inventory)
