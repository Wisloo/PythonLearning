# keyword arguments = an argument preceded by an identifier
#                     helps with readability
#                     order of arguments doesn't matter
#                     1. positional 2. default 3. KEYWORD 4. arbitrary

def hello(greeting, title, first_name, last_name):
    print(f"{greeting} {title} {first_name} {last_name}")

hello(greeting = "Hello", last_name = "Lapayag", first_name = "Louis",  title = "Teacher")

# order won't matter if you use keyword arguments by preceding them with their keywords

for x in range(1, 11):
    print(x, end = " ")
print()
print("1", "2", "3", "4", "5", sep = "-")