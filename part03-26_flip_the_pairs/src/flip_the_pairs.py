# Write your solution here
number = int(input("Please type in a number: "))

upper = 2
lower = 1

while True:
    if upper > number:
        break
    print(upper)
    print(lower)
    upper += 2
    lower += 2
if number % 2 != 0:
    print(lower)