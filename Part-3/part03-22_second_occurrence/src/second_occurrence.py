word = input("Please type in a string: ")
substring = input("Please type in a substring:")
index = word.find(substring) + len(substring)
i = word[index:].find(substring)
if i >= 0:
    print(f"The second occurrence of the substring is at index {index+i}.")
else:
    print("The substring does not occur twice in the string.")