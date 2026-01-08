n = int(input())


total_count = 0

for nums in range(n):
    each_row_count = n - nums
    total_count = total_count + each_row_count
    
for row in range(1, n + 1):
    if row == 1:
        first_row = ""
        for column in range(n):
            first_row = first_row + str(total_count) + " "
            total_count = total_count - 1
        print(first_row)
    elif row == n:
        last_row = str(1) + " "
        print(last_row)
    else:
        each_row = str(total_count) + " "
        hollow_spaces = "  " * (n - row - 1)
        each_row += hollow_spaces 
        total_count -= int(len(hollow_spaces) / 2) + 1
        each_row += str(total_count) + " "
        total_count -= 1
        print(each_row)
    