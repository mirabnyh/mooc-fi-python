l = []
i = 1
while True:
    print(f"The list is now {l}")
    op = input("a(d)d, (r)emove or e(x)it: ")
    if op == "x":
        print("Bye!")
        break
    elif op == "d":
        l.append(i)
        i += 1
    elif op == "r":
        i -= 1
        l.remove(i)

