name = input("Enter your full name: ")
phone_number = input("Enter your phone number: ")
string_length = len(name) # returns the length of a string
print(string_length)

string_find = name.find(" ")
string_reverse_find = name.rfind("L")
print(string_find)
print(string_reverse_find)

name = name.capitalize()
print(name)

name = name.upper()
print(name)

name = name.lower()
print(name)

result = name.isdigit() # returns a boolean value. true if the string only contains digits.
print(result)

result = name.isalpha()
print(result)

result = name.isalnum()
print(result)

phone_number = phone_number.replace("-", " ")
print(phone_number)

phone_number = phone_number.count(" ")
print(phone_number)

