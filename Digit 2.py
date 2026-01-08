n = int(input())

for row in range(1, 2 * n):
    if row == 1 or row == n or row == (2 * n - 1):
        each_row = "* " * n
    elif row < n:
        spaces = " " * (2 * (n - 1))
        each_row = spaces + "*"
    else:
        each_row = "*"
    print(each_row)
        