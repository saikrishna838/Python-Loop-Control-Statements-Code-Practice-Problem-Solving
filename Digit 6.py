n = int(input())

for i in range(2 * n - 1):
    if i == 0 or i == n-1 or i == 2 * n - 2:
        print("* " * n)
    elif i < n - 1:
        print("*")
    else:
        print("*" + " " * (2 * (n - 1) - 1)  + "*")