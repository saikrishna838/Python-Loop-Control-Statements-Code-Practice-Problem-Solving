n = int(input())

for row in range(0, n):
    dots = ". " * (n - (row + 1))
    zeroes = "0 " * (2 * row + 1)
    each_row = dots + zeroes +dots
    print(each_row)