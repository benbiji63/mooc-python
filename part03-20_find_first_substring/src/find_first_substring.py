# Write your solution here
word = input("Please type in a word: ")
char = input("Please type in a character: ")

indexOfChar = word.find(char)
if len(word) - indexOfChar > 2:
    print(word[indexOfChar : indexOfChar + 3])