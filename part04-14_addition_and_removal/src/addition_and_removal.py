# Write your solution here

list1 = []
counter = 0
while True:
    print(f"The list is now {list1}")
    action = input("a(d)d, (r)emove or e(x)it: ")
    match action:
        case "d":
            counter += 1
            list1.append(counter)
        case "r":
            list1.remove(counter)
            counter -= 1
        case "x":
            print("Bye!")
            break
