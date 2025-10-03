# indexing = accessing elements of a sequence using [] (indexing operator)
#            [start : end : step]

credit_number = "1234-5678-9012-3456"

# print to a specific number
print(credit_number[0:4])
print(credit_number[5:9])

# To ending
print(credit_number[5:])

# negative index (will start at the end)
print(credit_number[-2])

# step
print(credit_number[::2]) # prints every second character of the string

last_digits = credit_number[-4:]
print(f"XXXX-XXXX-XXXX-{last_digits}")

# reverse a string
reversed_string = credit_number[::-1]
print(f"{reversed_string}")