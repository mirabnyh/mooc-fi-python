while True:
    editor = input("Editor: ").lower().strip()
    if editor == "visual studio code":
        break
    elif editor == "notepad" or editor == "word":
        print("awful")
    elif editor == "vim" or editor == "emacs":
        print("not good")

print("an excellent choice!")