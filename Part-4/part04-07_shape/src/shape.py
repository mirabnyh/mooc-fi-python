# Copy here code of line function from previous exercise and use it in your solution
def line(n, char):
    if char == "":
        print("*" * n)
    else:
        print(char[0] * n)

def shape(n1, character1, n2, character2):
    i = 1
    while i <= n1:
        line(i, character1)
        i += 1

    for _ in range(n2):
        line(n1, character2)

# You can test your function by calling it within the following block
if __name__ == "__main__":
    shape(5, "x", 2, "o")