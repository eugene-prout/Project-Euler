from euler import generatePrimes,sumOfFactors
from timeit import default_timer as timer
primes = generatePrimes(1000)

def formula(n,a,b):
    return n**2 + n*a + b

def chain(a,b):
    n = 0
    prime = True
    while prime:
        result = formula(n,a,b)
        sumF = sumOfFactors(result,primes)
        if sumF != 1:
            prime = False  
        n += 1
    n -= 1 #zero indexed
    return n
mx = 0
a_max = 0
b_max = 0

start = timer()
for a in range(-1000,1000):
    for b in primes:
        if a % 2 == 1 and b != 2:

            leng = chain(a,b)
            if leng > mx:
                mx = leng
                a_max = a
                b_max = b
    
end = timer()
print(a_max,b_max)
print("Time taken:", end-start, "s")