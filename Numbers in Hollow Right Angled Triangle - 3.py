start_number = int(input())
n = int(input())

for row in range(1, n + 1):
    if row == n:
        last_row = ""
        for column in range(n):
            start_number = start_number + 1
            last_row = last_row + str(start_number) + " "
        print(last_row)
    elif row == 1:
        first_row = str(start_number) + " "
        print(first_row)
    else:
        start_number = start_number + 1
        each_row = str(start_number) + " "
        hollow_spaces = "  " * (row - 2)
        each_row = each_row + hollow_spaces
        start_number = start_number + 1
        each_row = each_row + str(start_number) + " "
        
        print(each_row)