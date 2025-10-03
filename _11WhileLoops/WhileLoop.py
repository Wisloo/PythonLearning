# while loop = execute some code WHILE some condition remains true

name = input("Enter your name: ")
while name == "":
    print("You did not enter your name")
    name = input("Enter your name: ")
print(f"Hello {name}")

age = int(input("Enter your age: "))
while age <= 0:
    print("Age can't be less than or equal to 0")
    age = int(input("Enter your age: "))
print(f"Your age is {age}")

food = input("Enter a food you like (Type Q to Quit): ").upper()
while not food == "Q":
    print(f"You like {food}")
    food = input("Enter a food you like (Type Q to Quit): ").upper()

number = int(input("Enter a number between 1 - 10: "))
while number < 1 or number > 10:
    print(f"{number} is not valid")
    number = int(input("Enter a number between 1 - 10: "))
print("bye")