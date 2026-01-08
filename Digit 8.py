n = int(input())
rows = 2 * n + 1
cols = n

for i in range(rows):
    if i == 0 or i == rows // 2 or i == rows - 1:
        print("* " * cols)
    else:
        print("* " + "  " * (cols - 2) + "*") 
