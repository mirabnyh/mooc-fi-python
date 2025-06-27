def chessboard(n):
    if n % 2 == 0:
        for i in range(n):
            if i % 2 == 0:
                print("10" * (n//2))
            else:
                print("01" * (n//2))
            i += 1
    else:
        for i in range(n):
            if i % 2 == 0:
                print("10" * (n // 2) + "1")
            else:
                print("01" * (n// 2) + "0")
            i += 1
# Testing the function
if __name__ == "__main__":
    chessboard(5)
