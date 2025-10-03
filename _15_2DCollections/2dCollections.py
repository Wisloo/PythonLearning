# 2d collections are useful for when you need a grid or excel like representation of data

fruits = ["apple", "orange", "banana", "coconut"]
vegetables = ["celery", "carrots", "potatoes"]
meats = ["chicken", "fish", "turkey"]

groceries = [fruits, vegetables, meats]
print(groceries[2][1]) # you print each item in a 2d list like it is a coordinate

for x in range(len(groceries)):
    print(groceries[x])
print()

# or you can do this

for collection in groceries:
    for food in collection:
        print(food, end = " ")
    print()

