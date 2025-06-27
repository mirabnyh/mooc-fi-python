sentence = ""
last_word = ""
while True:
    word = input("Please type in a word:")
    if word == "end" or word == last_word:
        break
    last_word = word
    sentence +=  word + " "

print(sentence)