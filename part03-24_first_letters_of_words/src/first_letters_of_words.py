# Write your solution here
sentence = input("Please type in a sentence: ")
while True:
    print(sentence[0])
    indexOfNextWord = sentence.find(" ")+1
    sentence = sentence[indexOfNextWord:]
    if indexOfNextWord < 1:
        break
