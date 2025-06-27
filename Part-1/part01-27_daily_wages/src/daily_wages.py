hourly_wage = float(input("Hourly wage:"))
hours = int(input("Hours worked: "))

day = input("Day of the week: ")
wage = hourly_wage * hours
if day == "Sunday":
    wage *= 2
print(f"Daily wages: {wage} euros") 