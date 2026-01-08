n =int(input())
count = 1
for i in range(1, n + 1):
    if (i == 1 or i == n):
        for j in range(1, (n + 2) - i):
            print(j, end= " ")
        print()
    else:
        spaces = "  " * (n - (i + 1))
        nums = (n - i) + count  
        row = "1 " + spaces + str(nums) 
        print(row)