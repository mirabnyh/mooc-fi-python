n = int(input("What is your age?"))
if n >= 5:
    print(f"Ok, you're {n} years old")
elif 0 <= n < 5:
    print("I suspect you can't write quite yet...")
else:
    print("That must be a mistake")