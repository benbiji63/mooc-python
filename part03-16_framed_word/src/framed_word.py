# Write your solution here
content = input("Word: ")
frame = "*" * 30
spacesRequiredForLeftAlignment = int((28 - len(content)) / 2)
spacesRequiredForRighftAlignment = spacesRequiredForLeftAlignment
if len(content) % 2 != 0:
    spacesRequiredForRighftAlignment += 1
print(frame)
print(
    "*"
    + " " * spacesRequiredForLeftAlignment
    + content
    + " " * spacesRequiredForRighftAlignment
    + "*"
)
print(frame)