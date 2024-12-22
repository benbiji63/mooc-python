# Write your solution here
string = input("Please type in a string: ")
stringLength = len(string)
positionsToAlign = 20 - stringLength
print("*" * positionsToAlign + string)