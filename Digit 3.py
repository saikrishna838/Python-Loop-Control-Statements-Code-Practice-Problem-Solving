n = int(input())
left_spaces = "  " * (n - 1)

for row in range(2 * n - 1):
    if row == 0 or row == n - 1 or row == 2 * n -2:
        each_row = "* " * n
    else:
        each_row = left_spaces + "*"
    print(each_row)