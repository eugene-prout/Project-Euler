from timeit import default_timer as timer
from functools import lru_cache
import sys
import math

#lru_cache(maxsize=None)
def triangle(n):
    if n == 1:
        return 1
    else:
        return n + triangle(n-1)

def factor(numberToFactor):
    factors = []
    for x in range(1,numberToFactor+1):
        if numberToFactor % x == 0:
            y = numberToFactor / x
            factors.append(y)
    return factors

def triangle2(n):
    return n*(n+1)/2

def get_factors(n):
    count = 0


    for i in range(1, round(math.sqrt(n)+1)):
        if n % i == 0:
            count += 2
        if i * i == n:
            count -= 1

    return count


if __name__ == "__main__":
    sys.setrecursionlimit(30000)
    for x in range(1,10000000000):
        if x % 1000 == 0:
            print(x)
        trig = triangle2(x)
        facts = get_factors(trig)

        if  facts > 499:
            print(x,trig,facts)

    print("Done")
