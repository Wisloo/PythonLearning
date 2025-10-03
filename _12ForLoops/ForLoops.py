# for loops  = execute a block of code a fixed number of times.
#              you can iterate over a range, string, sequences, etc.

for cnt in range(1, 11): # first number is beginning while second is exclusive ending
    print(cnt)
print("Happy Birthday")

for backCnt in reversed(range(1, 11, 2)):
    print(backCnt)

credit_card = "1234-5678-9012-3456"

for num in credit_card:
    print(num)

for x in range(1, 21):
    if x == 13:
        continue # skip an iteration
    else:
        print(x)

for x in range(1, 21):
    if x == 13:
        break # stops the loop after a certain condition is met
    else:
        print(x)