def distinct_numbers(l):
    L = []
    for i in range(len(l)):
        if l[i] not in L:
            L.append(l[i])
    return sorted(L)

if __name__ == "__main__":
    my_list = [3, 2, 2, 1, 3, 3, 1]
    print(distinct_numbers(my_list)) # [1, 2, 3]