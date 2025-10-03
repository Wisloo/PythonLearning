import random
low = 1
high = 100

options = ("Rock", "Paper", "Scissor")
# number = random.randint(low, high) # a is starting range while b is ending range
# number = random.random() # returns a float precision point variable between 0 and 1
# option = random.choice(options) # returns a random element from a collection
cards = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
random.shuffle(cards)

print(cards)