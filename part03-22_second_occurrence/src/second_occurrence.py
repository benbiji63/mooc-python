# Write your solution here
string = input("Please type in a string:")
subString = input("Please type in a substring:")

indexOfSubstring = string.find(subString)
count = indexOfSubstring+len(subString)
string = string[count :]
indexOfSubstring = string.find(subString)

if indexOfSubstring == -1:
    print("The substring does not occur twice in the string.")
else:
  print(f'The second occurrence of the substring is at index {indexOfSubstring+count}.')