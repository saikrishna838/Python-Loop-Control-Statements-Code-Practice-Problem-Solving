n = int(input())
hollow_spaces = "  " * (n - 2)
for row in range(n):
    if row == 0 or row == n - 1:
        each_row = "* " * n
    else:
        each_row = "* " + hollow_spaces + "*"
    print(each_row)
left_spaces = "  " * (n - 1)
for row in range(1, n):
    if row == n - 1:
        each_row = "* " * n
    else:
        each_row = left_spaces + "*"
    print(each_row)