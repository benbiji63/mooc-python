# Write your solution here
number = int(input("Please type in a number: "))

for i in range(number):
    for j in range(number):
        print(f"{i+1} x {j+1} = {(i+1)*(j+1)}")