l = [1, 2, 3, 4, 5]

while True:
    index = int(input("Index: "))
    # if user enters negative index, then break
    if index < 0:
        break
    new_value = int(input("New value: "))
    l[index] = new_value
    print(l)

