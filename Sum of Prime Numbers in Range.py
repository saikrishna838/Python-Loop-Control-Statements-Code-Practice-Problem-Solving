m = int(input())
n = int(input())

sum_of_prime_numbers = 0

for i in range(m, n + 1):
    factors = 0
    
    for j in range(2, i):
        if i % j == 0:
            factors = factors + 1
    
    if factors == 0:
        sum_of_prime_numbers = sum_of_prime_numbers + i
        
print(sum_of_prime_numbers)