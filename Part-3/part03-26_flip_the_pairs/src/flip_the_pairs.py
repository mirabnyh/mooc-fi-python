number = int(input("Please type in a number:"))
i = 1
if number % 2 == 0:
    while i <= number:
        print(i + 1)
        print(i)
        i += 2
else:
    while i <= number:
        if i + 2 <= number:
            print(i + 1)
        print(i)
        i += 2