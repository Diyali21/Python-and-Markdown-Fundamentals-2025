from datetime import datetime

items = [
    {"name": "Widget A", "quantity": 10, "price": 2.5},
    {"name": "Widget B", "quantity": 5, "price": 15.75},
    {"name": "Gadget", "quantity": 2, "price": 99.99},
]

# Output
# Invoice Date: 03 March 2025

# Product               Qty     Unit Price          Total
# -------------------------------------------------------
# Widget A               10           2.50          25.00
# Widget B                5          15.75          78.75
# Gadget                  2          99.99         199.98
# -------------------------------------------------------
# Grand Total                                      303.73


def print_invoice(invoice_date, items):
    print(f"Invoice Date: {invoice_date:%d %B %Y} \n\n")

    print(f"{'Product':<21} {'Qty':<7} {'Unit Price':<19} {'Total'}")

    print(f"{'-':-<55}")

    grand_total = 0
    for item in items:
        name = item["name"]
        qty = item["quantity"]
        up = item["price"]
        total = qty * up
        grand_total = grand_total + total
        print(f"{name:<22} {qty:<11} {up:<14} {total:.2f}")

    print(f"{'-':-<55}")
    print(f"{'Grand Total':<50}{grand_total}")


invoice_date_str = input("Enter date in 'YYYY-MM-DD' format: ")
invoice_date = datetime.strptime(invoice_date_str, "%Y-%m-%d")
print_invoice(invoice_date, items)
