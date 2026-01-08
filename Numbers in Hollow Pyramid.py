n = int(input())

for i in range(1, n):
    
    left_spaces = n - i
    middle_spaces = (2 * n - 1) - ( (2 * left_spaces ) + 2 )
    
    if i == 1:
        print(" " * left_spaces + "5")
    else:
        print(" " * left_spaces + "5" + " " * middle_spaces + str(5 + i - 1))
        
final_line = ""

for j in range(n):
    
    final_line = final_line + str(5 + j) + " "
    
print(final_line)