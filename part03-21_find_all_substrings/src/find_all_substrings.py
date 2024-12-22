# Write your solution here
word = input("Please type in a word: ")
char = input("Please type in a character: ")

while len(word) > 0:
    indexOfChar = word.find(char)
    if indexOfChar == -1:
        break
    if len(word) - indexOfChar > 2:
        print(word[indexOfChar : indexOfChar + 3])
    word = word[indexOfChar+1:]
    