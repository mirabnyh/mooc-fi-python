def squared(text, n):
    t = text * len(text) * (2*n)
    i = 0
    for _ in range(n):
        print(t[i: i + n ])
        i += n



if __name__=="__main__":
    squared("ab", 3)
    print()
    squared("aybabtu", 5)