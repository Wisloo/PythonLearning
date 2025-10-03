item = input("What item would you like to buy? ")
price = float(input("What is the price of the item? "))
quantity = int(input("How many would you like? "))
total = price * quantity

print(f"You are going to buy {item} and the price is {price} with a quantity of {quantity}.")
print(f"The total is ${total}")
