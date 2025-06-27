n = int(input("Number: "))
if n % 5 != 0 and n % 3 == 0:
    print("Fizz")
elif n % 5 == 0 and n % 3 != 0:
    print("Buzz")
elif n % 5 == 0 and n % 3 == 0:
    print("FizzBuzz")