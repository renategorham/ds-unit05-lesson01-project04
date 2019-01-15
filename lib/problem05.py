'''
What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20
'''
factors = []
for i in range(2,21):
    n = 2
    target = i
    result = i
    while result != 1:
        if target % n == 0:
            result = target / n
            factors.append(n)
            target = result
        else:
            n += 1
print(factors)
        
