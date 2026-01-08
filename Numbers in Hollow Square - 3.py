s = int(input())
n = int(input())

spaces = 2 * n - 3

for row in range(1, n + 1):
    each_row = ""
    for each_number in range(1, n + 1):
        if row == 1 or row == n:
            each_row = each_row + str(s) + " "
        else:
            each_row = str(s - n + 1) + " " * spaces + str(s)
        s = s + 1
                
    print(each_row)
            
        