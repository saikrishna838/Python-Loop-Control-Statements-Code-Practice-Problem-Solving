n = int(input())

for i in range(1, n + 1):
    spaces = " " * (n - i)
    print(spaces, end="")
    for j in range(1, i + 1):
        print(str(j), end= " ")
    print()