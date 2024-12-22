# Write your solution here
limit = int(input("Upper Limit: "))
base = 1
increment = 2
while base < limit:
    base += increment
    increment += 1
print(base)