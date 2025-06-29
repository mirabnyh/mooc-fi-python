def shortest(l):
    short = l[0]
    for i in range(len(l[1:])):
        if len(short) > len(l[i]):
            short = l[i]
    return short
    
if __name__ == "__main__":
    my_list = ["adele", "mark", "dorothy", "tim", "hedy", "richard"]

    result = shortest(my_list)
    print(result)