def same_chars(word, i, j):
    if i >= len(word) or j >= len(word):
        return False
    if word[i] == word[j]:
        return True
    return False

# You can test your function by calling it within the following block
if __name__ == "__main__":
    print(same_chars("coder", 1, 2))