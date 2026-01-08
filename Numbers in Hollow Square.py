n = int(input())

for i in range(1, n + 1):
    if (i == 1 or i ==n):
        for j in range(1, n + 1):
            print(j, end=" ")
        print()
    else:
        count = n - 2
        print("1 " + count * "  " + str(n))