attempt = 0
while True:
    pin = input("Wrong")
    attempt += 1
    if pin == "4321":
        break
    print("Wrong")
if attempt == 1:
    print("Correct! It only took you one single attempt!")
else:
    print(f"Correct! It took you {attempt} attempts")