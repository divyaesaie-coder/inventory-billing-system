#Program to create a simple inventory and billing system with stock management and purchase calculation.
items = []
prices = []
stocks = []

# -------- INVENTORY INPUT --------
while True:
    item = input("Enter item name: ")
    price = float(input("Enter price: "))
    stock = int(input("Enter stock: "))

    items.append(item)
    prices.append(price)
    stocks.append(stock)

    if input("Add more items? (yes/no): ") != "yes":
        break

# -------- BILLING --------
total_bill = 0

while True:
    customer_item = input("Enter item to buy: ")

    if customer_item in items:
        idx = items.index(customer_item)
        qty = int(input("Enter quantity: "))

        if qty <= stocks[idx]:
            cost = prices[idx] * qty
            total_bill += cost
            stocks[idx] -= qty
            print("Added to bill:", cost)
        else:
            print("Insufficient stock")
    else:
        print("Item not found")

    if input("Continue shopping? (yes/no): ") != "yes":
        break

print("\nTotal Bill:", total_bill)

# -------- REMAINING INVENTORY VALUE --------
inventory_value = 0
for i in range(len(items)):
    inventory_value += prices[i] * stocks[i]

print("Remaining Inventory Value:", inventory_value)
