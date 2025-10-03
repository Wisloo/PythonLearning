# dictionary = a collection of {key:value} pairs
#              ordered and changeable. No duplicates

capitals = {"USA": "Washington D.C.",
            "India": "New Delhi",
            "China": "Beijing",
            "Russia": "Moscow"}

# print(capitals.get("India")) # shows the value of the key
capitals.update({"Germany": "Berlin"}) # updates the key value pair
# capitals.pop("China") # removes a key value pair from the collection
capitals.popitem() # removes the latest key value pair that was inserted

keys = capitals.keys() # displays the available keys in the collections

# for key in capitals.keys(): # iterate over each key
   # print(key)

# values = capitals.values() # displays the available values in the collections

# for value in capitals.values(): # iterate over each values
    # print(value)

items = capitals.items() # a combination of key and value

for key, value in capitals.items():
    print(f"{key}: {value}")