rows = int(input())
columns = int(input())

for row in range(1, rows + 1):
    
    next_number = 8
    each_row = "7 "
    
    if row ==1 or row == rows:
        
        for column in range(2, columns + 1):
            each_row = each_row + str(next_number) + " "
            next_number = next_number + 1
            
        print(each_row)
    else:
        hollow_spaces = "  "  * (columns - 2)
        each_row = each_row + hollow_spaces + str(7 + columns - 1) + " "
        
        print(each_row)
        
        