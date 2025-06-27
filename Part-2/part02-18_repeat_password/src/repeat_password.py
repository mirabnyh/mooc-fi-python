password = input("Password: ")
while True:
    rpass = input("Repeat password: ")
    if rpass == password:
        print("User account created!")
        break
    print("They do not match!")