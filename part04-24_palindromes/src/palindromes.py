# Write your solution here
# Note, that at this time the main program should not be written inside
# if __name__ == "__main__":
# block!


def palindromes(str1):
    return str1 == str1[::-1]


def main():
    while True:
        string = input("Please type in a palindrome: ")
        if palindromes(string):
            print(f"{string} is a palindrome!")
            break
        print("that wasn't a palindrome")


main()
