def findVowel(vowel, string):
    if vowel in string:
        print(f"{vowel} found")
    else:
        print(f"{vowel} not found")


string = input("Please type in a string:")

findVowel("a", string)
findVowel("e", string)
findVowel("o", string)
