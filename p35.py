from euler import generatePrimes,sumOfFactors
import itertools



def testCircle(n,primes):
    lst = list(str(n))
    for x in [0,2,4,5,6,8]:
        if x in lst:
            return False
    perms = [list(t) for t in itertools.permutations(list(str(x)))]
    for term in perms:

        if sumOfFactors(int(''.join(str(i) for i in term)),primes) > 1:
            return False
    return True

primes = generatePrimes(250)
for x in primes:
    perms = list(itertools.permutations(list(str(x))))
    if not testCircle(x,primes):
        for term in perms:
            try:
                primes.remove(int(''.join(str(i) for i in term)))
            except ValueError:
                pass
        
print(primes)