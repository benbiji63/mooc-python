number = int(input("Please type in a number: "))

initialValue = 1
while True:
    if initialValue >= number:
        break
    print(initialValue)
    print(number)
    number -= 1
    initialValue += 1
if initialValue == number:
    print(number)
