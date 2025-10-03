# if = Do some code only IF some condition is True
#      Else do something else

age = int(input("Enter your age: "))

if age >= 100:
    print("You are too old to sign up.")
elif age >= 18:
    print("You are eligible for a credit card.")
elif age < 0:
    print("You are not born yet.")
else:
    print("You are a chingus bingus.")

# do pay attention to the order of if else statement