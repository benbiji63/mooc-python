# Write your solution here
import math

while True:
    num = int(input("Please type in a number: "))
    if num <= 0:
        print("Thanks and bye!")
        break
    fact = math.factorial(num)
    print(f"The factorial of the number {num} is {fact}")
