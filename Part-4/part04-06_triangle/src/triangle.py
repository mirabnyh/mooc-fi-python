# Copy here code of line function from previous exercise
def line(n, char):
    if char == "":
        print("*" * n)
    else:
        print(char[0] * n)

def triangle(size):
    i = 1
    while i <= size:
    # You should call function line here with proper parameters
        line(i, "#")
        i += 1

# You can test your function by calling it within the following block
if __name__ == "__main__":
    triangle(5)
