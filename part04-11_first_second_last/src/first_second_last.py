# Write your solution here


def first_word(sentence):
    indexOfFirstSpace = sentence.find(" ") # Find the index of first space
    if indexOfFirstSpace == -1: # Changing the index if there is no subsequent space
        indexOfFirstSpace = len(sentence)
    return sentence[:indexOfFirstSpace]  # Return string from beginning till first space


def second_word(sentence):
    indexOfFirstSpace = sentence.find(" ")  # Find the index of first space
    sentence = sentence[indexOfFirstSpace + 1 :]  # Restructure the sentence from second word onwards
    indexOfSecondSpace = sentence.find(" ")  # Find the index of Second space
    if indexOfSecondSpace == -1: # Changing the index if there is no subsequent space
        indexOfSecondSpace = len(sentence)
    return sentence[:indexOfSecondSpace] # Return string from beginning of second word till second space

def last_word(sentence):
    reverseSentence = sentence[::-1] # Reverse the  sentence
    index = reverseSentence.find(" ")  # Find the index of first space in reversed sentence
    if index  == -1:
        index  = len(sentence)
    firstWord = reverseSentence[:index] # Find first word in reversed sentence
    return  firstWord[::-1] # Return the first word after reversing it back to original state
    
# You can test your function by calling it within the following block
if __name__ == "__main__":
    sentence = "once upon a time there was a programmer"
    # print(first_word(sentence))
    print(second_word(sentence))
    # print(last_word(sentence))
