# Write your solution here
limit = int(input("Upper Limit: "))
base = 1
increment = 2
str = 'The consecutive sum: 1'
while base < limit:
    str+=f' + {increment}'
    base += increment
    increment += 1

print(str+f' = {base}')