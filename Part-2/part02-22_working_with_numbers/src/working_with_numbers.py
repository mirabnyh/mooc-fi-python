count = 0
somme = 0
negative_number = 0
positive_number = 0
print("Please type in integer numbers. Type in 0 to finish.")
while True:
    number = int(input("Number: "))
    if number == 0:
        break
    count += 1
    somme += number
    if number < 0:
        negative_number += 1
    else:
        positive_number += 1

print(f"Numbers typed in {count}")
print(f"The sum of the numbers is {somme}")
print(f"The mean of the numbers is {somme / count}")
print(f"Positive numbers {positive_number}")
print(f"Negative numbers {negative_number}")