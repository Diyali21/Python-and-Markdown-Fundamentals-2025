# Task 2
inventory = [
    {"name": "Apple 🍎", "quantity": 30, "price": 0.5},
    {"name": "Banana 🍌", "quantity": 20, "price": 0.2},
]

name = input("Enter product name to update: ")
qty = int(input("Enter additional quantity: "))
price = float(input("Enter new price: "))

for product in inventory:
    product_name = product.get("name")
    if name == product_name:
        print(f"Updated {name} successfully! 🎉")
        product["quantity"] += qty
        product["price"] = price
print(f"Updated Inventory: {inventory}")


# Task 3
inventory = [
    {"name": "Apple 🍎", "quantity": 70, "price": 0.4},
    {"name": "Banana 🍌", "quantity": 20, "price": 0.2},
]


name = input("Enter product name: ")
qty = int(input("Enter quantity: "))
price = float(input("Enter price: "))

for product in inventory:
    product_name = product.get("name")
    if name == product_name:
        product["quantity"] += qty
        product["price"] = price
        print(f"Updated {name} successfully! 🎉")
        break
else:
    product = {"name: ": name, "quantity: ": qty, "price: ": price}
    inventory.append(product)
    print(f"Added new product {name}! 🎉")

print(f"Updated Inventory: {inventory}")
