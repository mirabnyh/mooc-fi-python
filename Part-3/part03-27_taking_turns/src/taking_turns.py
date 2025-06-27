number = int(input("Please type in a number:"))
i = 1
j = number
if number % 2 == 0:
    while i < j :
        print(i)
        print(j)
        i += 1
        j -= 1
else:
    while i <= j:
        if i != j:
            print(i)
        print(j)
        i += 1
        j -= 1