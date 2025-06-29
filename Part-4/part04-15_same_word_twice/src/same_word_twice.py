list_words = []
while True:
    word = input("Word: ")
    if word not in list_words:
        list_words.append(word)
    else:
        break

print(f"You typed in {len(list_words)} different words")