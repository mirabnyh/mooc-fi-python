# Write your solution here
def greatest_number(x, y, z):
    if x <= y and z <= y:
        return y
    elif x <= z and y <= z:
        return z
    else:
        return x

# You can test your function by calling it within the following block
if __name__ == "__main__":
    greatest = greatest_number(5, 4, 8)
    print(greatest)