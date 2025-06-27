while True:
    word = input("Please type in a string:")
    if len(word) == 0:
        break
    print(word)
    print(len(word) * "-")