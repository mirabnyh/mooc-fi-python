# Copy here code of line function from previous exercise
def line(n, char):
    if char == "":
        print("*" * n)
    else:
        print(char[0] * n)


def box_of_hashes(height):
    i = 0
    while i < height:
    # You should call function line here with proper parameters
        line(10, "#")
        i += 1

# You can test your function by calling it within the following block
if __name__ == "__main__":
    box_of_hashes(5)
