# Write your solution here

list1 = []
while True:
    newItem = int(input("New item: "))
    if newItem == 0:
        print("Bye!")
        break
    list1.append(newItem)
    print(f"The list now: {list1}")
    print(f"The list in order: {sorted(list1)}")
