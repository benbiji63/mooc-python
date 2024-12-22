# Write your solution here
def greatest_number(num1, num2, num3):
    if num1 >= num2:
        largest = num1
    else:
        largest = num2

    if num3 >= largest:
        largest = num3
    return largest


# You can test your function by calling it within the following block
if __name__ == "__main__":
    greatest = greatest_number(5, 4, 8)
    print(greatest)
