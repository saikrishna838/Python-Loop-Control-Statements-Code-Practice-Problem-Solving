n = int(input())

count = 0

for i in range(1, n+1):
    stars = count + 2
    spaces = n - i
    count = stars + 0
    row = "  " * spaces +  "* " * stars
    print(row)