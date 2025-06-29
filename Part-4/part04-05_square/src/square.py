# Copy here code of line function from previous exercise
def line(n, char):
    if char == "":
        print("*" * n)
    else:
        print(char[0] * n)

def square(size, character):
    for i in range(size):
    # You should call function line here with proper parameters
        line(size, character)

# You can test your function by calling it within the following block
if __name__ == "__main__":
    square(5, "x")