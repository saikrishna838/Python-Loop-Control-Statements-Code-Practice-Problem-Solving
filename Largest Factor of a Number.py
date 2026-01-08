number = int(input())

for each_number in range(1, number):
    if number % each_number == 0:
        largest_factor = each_number
        
print(largest_factor)