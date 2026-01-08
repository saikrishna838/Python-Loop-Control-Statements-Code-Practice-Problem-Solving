n = int(input())

for i in range(1, n + 1):
    if (i == 1 or i == n):
        spaces = " " * (n - i)
        print(spaces, end="")
        for j in range(1, i +1):
            star = "* "
            print(star, end="")
        print()
        
    else:
        spaces = " " * (n - i)
        print(spaces, end="")
        for j in range(1):
            spaces = "  " * (i - 2)
            row = "* " + spaces + "*"
            print(row)