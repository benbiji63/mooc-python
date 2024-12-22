# Write your solution here

list1 = [1, 2, 3, 4, 5]

while True:
    index = int(input("Index:"))
    if index == -1:
        break
    newValue = int(input("New value:"))
    list1[index] = newValue
    print(list1)
