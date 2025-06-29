def length_of_longest(l):
    longest = len(l[1])
    for i in range(len(l[1:])):
        if len(l[i]) > longest:
            longest = len(l[i])
    return longest
    
if __name__ == "__main__":
    my_list = ["adele", "mark", "dorothy", "tim", "hedy", "richard"]

    result = length_of_longest(my_list)
    print(result)