def list_sum(a, b):
    c = []
    for i in range(len(a)):
        c.append(a[i] + b[i])
    return c

if __name__ == "__main__":
    a = [1, 2, 3]
    b = [7, 8, 9]
    print(list_sum(a, b)) # [8, 10, 12]