''' 
Problem 03. What is the largest prime factor of the number 600851475143?
'''

n = 2
target = 600851475143
result = 600851475143
factors = []


while result != 1:
    if target % n == 0:
        result = target / n
        factors.append(n)
        target = result
    else:
        n += 1

# for i in factors:
#     prime_factors = []
#     m = 2
#     check_prime = i
#     if check_prime % m == 0:
#         prime_result = check_prime / m
#         prime_factors.append(m)
#         check_prime = prime_result
#     else:
#         m += 1

print(factors)