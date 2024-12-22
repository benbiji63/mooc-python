# Write your solution here
def spruce(size):
    
# Find the maximum width required and the padding to be given to left side 
    width = (2 * size) - 1
    paddingSize = width // 2
    padding = " " * paddingSize

    print("a spruce!")
    if size > 1:
        temporaryPadding = padding
        currentSpruce = "*"
        for i in range(1, size + 1):
            print(temporaryPadding + currentSpruce )
            temporaryPadding = temporaryPadding[: len(temporaryPadding)-1]
            currentSpruce += "**"
    print(padding + "*" + padding)


# You can test your function by calling it within the following block
if __name__ == "__main__":
    spruce(5)
    # print()
    # spruce(5)
