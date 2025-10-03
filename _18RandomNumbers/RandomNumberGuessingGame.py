import random


secret_number = random.randint(0,100)
attempts = 0
guess = 0
print("**********************************")
print("WELCOME TO NUMBER GUESSING GAME!")
print("**********************************")

while not guess == secret_number:
    guess = int(input("Enter guess number: "))
    attempts+=1

    if guess < secret_number:
        print("Guess is too low.")
    elif guess > secret_number:
        print("Guess is too high.")
    else:
        print(f"Correct! You guess it in {attempts} attempts.")
        break
