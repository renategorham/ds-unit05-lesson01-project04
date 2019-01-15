'''
Euler project problem 2. Sum of the even value elements of the Fibonacci sequence
less than 4 million.
'''

lim = 4000000
a = 0
b = 1
c = 0
fib = []

while c < lim:
    c = a + b
    a = b
    b = c

    fib.append(c)

    summed = sum(x for x in fib if x % 2 == 0)

print(summed)

