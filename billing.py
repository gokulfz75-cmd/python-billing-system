# Simple Billing System - Python
# Created by [Un Per]

items = []

while True:
    name = input("Item name (or 'done'): ")
    if name == "done":
        break
    price = int(input("Price: "))
    qty = int(input("Qty: "))
    items.append([name, price, qty])

print("\n--- BILL ---")
total = 0
for n, p, q in items:
    amt = p*q
    print(f"{n} x {q} = {amt}")
    total += amt

print(f"Total Amount: {total}")
print("Thank you!")
