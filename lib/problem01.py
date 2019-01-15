'''
Euler project problem 1. Add all numbers less than 1000 that are divisable by 
3 or 5. Hint only use numbers where 3 and 5 are common divisors once.
'''
def add(n=1000):

        threes_and_fives = sum(x for x in range(n) 
            if x % 3 == 0 and x % 5 == 0)

        threes_only = sum(x for x in range(n) 
            if x % 3 == 0 and x % 5 != 0)

        fives_only = sum(x for x in range(n) 
            if x % 3 != 0 and x % 5 == 0)

        summed = threes_and_fives + threes_only + fives_only
        
        return summed