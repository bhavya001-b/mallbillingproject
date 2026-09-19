print("=======================================================================================")

print("WELCOME TO OUR MALL")

print("What would you like to order? Here is the menu")

print("FOOD")

print("SR.NO           ITEM                                                        PRICE")

print("1.              pizza                                                       200")
print("2.              burger                                                      350")
print("3.              french fries                                                150")

print("CLOTHES")

print("5.              Tshirt                                                      400")
print("6.              shirt                                                       1500")
print("7.              pant                                                        2000")

print("GROCERIES")

print("8.              milk                                                        70")
print("9.              tomato                                                      50")
print("10.             avocado                                                     90")

print("=======================================================================================")

number_of_item = int(input("How many items you want to order: "))

ordered_items = []
ordered_quant = []
ordered_price = []
price_per_unit = []

total_price = 0

for i in range(number_of_item):

    ordered_items.append(input("Enter item name       : "))

    quantity = int(input("Enter quantity        : "))
    ordered_quant.append(quantity)

    price = float(input("Enter price of 1 unit : "))
    ordered_price.append(price)

    item_total = price * quantity
    price_per_unit.append(item_total)

    total_price += item_total

print("=======================================================================================")

print("Item                 Qty             Price")

for j in range(number_of_item):

    print(ordered_items[j], "             ", ordered_quant[j], "             ", price_per_unit[j])

print("Total Price:", total_price)

print("=======================================================================================")