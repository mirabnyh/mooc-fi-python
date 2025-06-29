
def main():
    while True:
        word = input("Please type in a palindrome: ")
        if palindromes(word):
            print(f"{word} is a palindrome!")
            break
        print("that wasn't a palindrome")

def palindromes(w):
    if w == w[::-1]:
        return True
    return False
    
main()


