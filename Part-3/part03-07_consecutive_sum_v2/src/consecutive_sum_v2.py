limit = int(input("limit: "))
n = 1
s = 0
sentence = ""
while s < limit:
    s += n
    if s < limit:
        sentence += f"{n} + "
    else:
        sentence += f"{n}"
    
    n += 1
print(f"The consecutive sum: {sentence} = {s}")