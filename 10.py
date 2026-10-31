products = (
    ("Pen", 10, 50),
    ("Book", 40, 20),
    ("Pencil", 5, 100),
    ("Bag", 500, 10)
)

total_value = 0

for product in products:
    name, price, quantity = product

    value = price * quantity
    total_value = total_value + value

    print("\nProduct:", name)
    print("Price:", price)
    print("Quantity:", quantity)
    print("Total value:", value)

    if quantity < 15:
        print("Reorder required")

print("\nTotal Inventory Value:", total_value)