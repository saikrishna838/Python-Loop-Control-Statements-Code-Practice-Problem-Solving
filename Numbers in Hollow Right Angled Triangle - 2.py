rows = int(input())

for row in range(1, rows + 1):
    if row == rows:
        each_row = ""
        
        for column in range(rows):
            each_row = each_row + str(rows - column) + " "
            
        print(each_row)
    elif row == 1:
        spaces = " " * (2 * rows - 2)
        each_row = spaces + "1 "
        
        print(each_row)
    else:
        spaces = " " * (2 * (rows - row))
        hollow_spaces = "  " * (row - 2)
        each_row = spaces + (str(row) + " ") + hollow_spaces + "1 "
        
        print(each_row)
        