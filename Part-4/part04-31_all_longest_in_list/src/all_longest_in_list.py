def all_the_longest(l):
    longest_length = len(l[0])
    for i in range(len(l[1:])):
        if longest_length < len(l[i]):
            longest_length = len(l[i])

    long_strings = []
    for i in range(len(l)):
        if len(l[i]) == longest_length:
            long_strings.append(l[i])
            
    return long_strings

if __name__ == "__main__":
    my_list = ["adele", "mark", "dorothy", "tim", "hedy", "richard"]

    result = all_the_longest(my_list)
    print(result) # ['dorothy', 'richard']