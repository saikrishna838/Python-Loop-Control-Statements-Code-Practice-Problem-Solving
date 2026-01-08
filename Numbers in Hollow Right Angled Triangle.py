n = int(input())

num = 1
count = 0

for i in range(1, n + 1):
    
    if(i == n or i == 1):
        for j in range(1, i + 1):
            print(str(j), end= " ") 
    else:
        spaces = "  " * count
        print((str(num) + (" ")) + spaces + str(i), end= "")
        count = count + 1
    print()