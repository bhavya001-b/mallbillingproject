print("=" * 60)
print("                 WELCOME TO OUR MALL")
print("=" * 60)

# Menu
menu = {
    1: ("Pizza", 200),
    2: ("Burger", 350),
    3: ("French Fries", 150),
    4: ("T-Shirt", 400),
    5: ("Shirt", 1500),
    6: ("Pant", 2000),
    7: ("Milk", 70),
    8: ("Tomato", 50),
    9: ("Avocado", 90)
}

# Display menu
print("\nFOOD")
print("1. Pizza                  ₹200")
print("2. Burger                 ₹350")
print("3. French Fries           ₹150")

print("\nCLOTHES")
print("4. T-Shirt                ₹400")
print("5. Shirt                  ₹1500")
print("6. Pant                   ₹2000")

print("\nGROCERIES")
print("7. Milk                   ₹70")
print("8. Tomato                 ₹50")
print("9. Avocado                ₹90")

print("\n0. Checkout")

# Store customer's order
cart = []

# Taking orders
while True:

    choice = int(input("\nEnter item number: "))

    # Checkout
    if choice == 0:
        break

    # Check whether item exists
    if choice not in menu:
        print("Invalid item number!")
        continue

    item_name, price = menu[choice]

    quantity = int(input("Enter quantity: "))

    if quantity <= 0:
        print("Quantity must be greater than 0!")
        continue

    item_total = price * quantity

    cart.append((item_name, quantity, price, item_total))

    print(f"{item_name} x {quantity} = ₹{item_total}")
    print("Item added to cart!")


# Generate bill
print("\n")
print("=" * 60)
print("                    FINAL BILL")
print("=" * 60)

print(f"{'ITEM':<20}{'QTY':<10}{'PRICE':<12}{'TOTAL'}")
print("-" * 60)

total_price = 0

for item in cart:
    item_name, quantity, price, item_total = item

    print(f"{item_name:<20}{quantity:<10}₹{price:<11}₹{item_total}")

    total_price += item_total

print("-" * 60)
print(f"{'TOTAL BILL':<42}₹{total_price}")
print("=" * 60)

print("           THANK YOU FOR SHOPPING!")
print("=" * 60)