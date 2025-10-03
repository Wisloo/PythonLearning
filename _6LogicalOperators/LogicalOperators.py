# logical operators = Evaluate multiple conditions (or, and, not)
#                     or = at least one condition must be True
#                     and = both conditions must be True
#                     not = inverts the condition (not False, not True)

temperature = 15
is_raining = True
is_sunny = False

if temperature > 35 or temperature < 0 or is_raining:
    print("The outdoor event is cancelled")
else:
    print("The outdoor event is still scheduled")

if temperature >= 28 and is_sunny:
    print("It is hot outside")
    print("It is SUNNY")
elif temperature <= 0 and is_sunny:
    print("It is cold outside")
    print("It is sunny")
elif 28 > temperature > 0 and not is_sunny:
    print("The weather is great")
