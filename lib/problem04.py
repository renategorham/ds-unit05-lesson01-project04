'''
Find the largest palindrome made from the product of two 3-digit numbers.
'''
pal = []
for i in range(1000):
    for j in range(1000):
        prod = i * j
        x = str(prod)
        y = ''
        for k in reversed(x):
            y += k
            prod_flip = int(y)
        if prod == prod_flip:
            pal.append(prod)

print(max(pal))