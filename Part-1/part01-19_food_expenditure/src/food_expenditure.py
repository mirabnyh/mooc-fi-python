n = int(input("How many times a week do you eat at the student cafeteria? "))
lunch_price = float(input("The price of a typical student lunch? "))
grocery = float(input("How much money do you spend on groceries in a week? "))

weekly_expenditure = n * lunch_price + grocery
print("Average food expenditure:")
print(f"Daily: {weekly_expenditure / 7} euros")
print(f"Weekly: {weekly_expenditure} euros")