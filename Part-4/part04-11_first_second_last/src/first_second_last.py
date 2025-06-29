# Write your solution here
def first_word(s):
    for i in range(len(s)):
        if s[i] == " ":
            return s[0:i]

def second_word(s):
    space = s.count(" ")
    if space == 1:
        sp = s.find(" ")
        return s[sp+1: ]
    space1 = s.find(" ")
    space2 = s.find(" ", space1 + 1)
    return s[space1+1 : space2]

def last_word(s):
    i = len(s) - 1
    while i >= 0:
        if s[i] == " ":
            return s[i+1 : ]
        i -= 1
# You can test your function by calling it within the following block
if __name__ == "__main__":
    sentence = "once upon a time there was a programmer"
    print(first_word(sentence))
    print(second_word(sentence))
    print(last_word(sentence))