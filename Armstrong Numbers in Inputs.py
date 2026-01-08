n = int(input())

for each_number in range(n):
    value = int(input())
    
    string = str(value)
    power = len(string)
    sum_of_digits = 0
    
    for integer_char in string:
        sum_of_digits = sum_of_digits + int(integer_char) ** power
        
    if sum_of_digits == value:
        print(value)