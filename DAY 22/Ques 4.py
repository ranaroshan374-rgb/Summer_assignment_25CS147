import re

s      = input("Enter a string: ")

# Remove all whitespace (spaces, tabs, newlines)
result = re.sub(r'\s+', '', s)
print("After removing all whitespace:", result)

# Remove only spaces
result2 = re.sub(r' ', '', s)
print("After removing spaces only  :", result2)