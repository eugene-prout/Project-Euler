from math import sqrt, floor
primes = []

def isPrime(n):
    if n == 1:
        return False
    elif n < 4:
        return True
    elif n % 2 == 0:
        return False
    elif n < 9:
        return True
    elif n % 3 == 0:
        return False
    else:
        root = floor(sqrt(n))
        factor = 5
        while factor <= root:
            if n % factor == 0:
                return False
            if n % (factor+2) == 0:
                return False
            factor += 6

        return True

        
for x in range(1,10):
    if x % 100000 == 0:
        print(x)
    if isPrime(x):
        print(x)
        primes.append(x)

print(sum(primes))