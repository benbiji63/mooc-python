# Write your solution here

list1 = []
numberOfItems = int(input("How many items:"))

for i in range(1, numberOfItems + 1):
    item = int(input(f"Item {i}"))
    list1.append(item)
print(list1)
