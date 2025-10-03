# collection = single 'variable' used to store multiple values
# List  = []  ordered and changeable. Duplicates OK
# Set   = {}  unordered and mutable, no duplicates allowed
# Tuple = ()  ordered and unchangeable. Duplicates OK. Faster performance

fruits = ["apple", "orange", "banana", "coconut"]
toys = {"car", "ball", "racket", "rubix cube",}
bike_brands = ("Pinarello", "Cinelli", "MountainPeak", "Bianchi", "Specialized")
# print(fruits[:3:2]) # start:end:step

# for fruit in fruits:
    # print(fruit, end=" ")

# LISTS:
# print(dir(fruits)) # lists the methods that are available for the function
# print(help(fruits)) # description of all the methods that you can use in the function
# print(len(fruits)) # returns length of the collection
# print("apple" in fruits) # returns boolean value whether an item is in the collection or not
# fruits[0] = "pineapple" # reassign a value to a specified index
# fruits.append("grapes") # adds an item to the list
# fruits.remove("apple") # removes an item from the list
# fruits.insert(2, "kiwi") # inserts an item to the given index
# fruits.sort() # sorts the list collection
# fruits.reverse() # reverses the list
# fruits.clear() # clears the list
# print(fruits.index("grapes")) # prints the index of a given element
# print(fruits.count("banana")) # prints how many of the given element is in the list

# SETS
# toys.pop() # removes first element on the set
# print(dir(toys)) # lists the methods that are available for the function
# print(help(toys)) # description of all the methods that you can use in the function
# print(len(toys)) # returns length of the collection
# print("apple" in toys) # returns boolean value whether an item is in the collection or not
# toys.clear() # clears te set

# TUPLES
# print(bike_brands)
# print(dir(bike_brands))
# print(help(toys))
print(len(bike_brands))
print("Pinarello" in bike_brands)

bike_brands.index("Cinelli")
print(bike_brands.count("Pinarello"))

