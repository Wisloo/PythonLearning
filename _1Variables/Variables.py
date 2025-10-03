# Variable = A container for a value (string, integer, float, boolean)
#            A variable behaves as if it was the value it contains

#string
first_name = "Louis"
food = "Burger"
email = "louisgwapochingusbingus@gmail.com"
print(f"Hello {first_name}")
print(f"I am eating a {food}")
print(f"Your email is {email}")

#integer = whole number
age = 19
quantity = 3
num_of_students = 43
print(f"Hello {first_name} you are {age} years old")
print(f"You are going to buy {quantity} apples")
print(f"Your class has {num_of_students} students")

#float = floating point number
price = 15.99
gpa = 3.2
distance = 9.27
print(f"The price is ${price} per apple")
print(f"My gpa is {gpa}")
print(f"You ran {distance} km")

#boolean
is_student = False # first letter is capital
for_sale = True
is_online = True

if for_sale:
    print("This item is for sale")
else:
    print("This item is not for sale")