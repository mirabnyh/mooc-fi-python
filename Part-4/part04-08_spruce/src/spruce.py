# Write your solution here
def spruce(size):
    print("a spruce!")
    i = size - 1
    j = 1
    while i >= 0:
        print(" "* i + "*" * j)
        i -= 1
        j += 2
    print(" " * (size - 1) + "*")

# You can test your function by calling it within the following block
if __name__ == "__main__":
    spruce(5)