start_number = int(input())
n = int(input())

for row in range(1, n + 1):
    initial_spaces = "  " * (row - 1)
    
    if row == 1:
        first_row = ""
        
        for column in range(n):
            first_row = first_row + str(start_number) + " "
            start_number = start_number + 1
        print(initial_spaces + first_row)
        
    elif row == n:
        last_row = str(start_number) + " "
        print(initial_spaces + last_row)
        
    else:
        each_row = str(start_number) + " "
        hollow_spaces = "  " * (n - row - 1)
        each_row = each_row + hollow_spaces
        start_number = start_number + 1
        each_row = each_row + str(start_number) + " "
        start_number = start_number + 1
        print(initial_spaces + each_row)
        
