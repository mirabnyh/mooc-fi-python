def list_of_stars(l):
    for i in range(len(l)):
        print("*" * l[i])


if __name__=="__main__":
    list_of_stars([2,5,7,9,10])