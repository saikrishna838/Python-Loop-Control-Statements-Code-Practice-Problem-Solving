m = int(input())
n = int(input())

num = m * n
count = n - 2


for row in range(1, m + 1):
    
    if row == 1 or row == m:
        for j in range(1, n + 1):
            each_row = str(num) 
            num = num - 1
            print(each_row, end= " ")
    else:
        spaces = "  " * count
        each_row = ((str(num) + " ") + spaces + str(num - n + 1))
        print(each_row, end= " ")
        num = num -n + 1
        num = num - 1
    print()
            
            