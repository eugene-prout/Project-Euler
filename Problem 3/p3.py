from timeit import default_timer as timer
# From the wikipedia - Sieve of Eratosthenes. Only used description of algorithm
# Own implementation
def generatePrimes(_range):
    candidates = list(range(2, _range+1))
    p = 2
    start = timer()
    while (p < len(candidates)):

        for number in candidates:
            if number % p == 0 and number != p:
                candidates.remove(number)
        p = candidates[candidates.index(p) + 1]
    end = timer()
    print("Primes generated!")    
    print("Time taken:", end-start, "s")
    return candidates

# Own algorithm
def factor(numberToFactor, primes):
    factors = []
    start = timer()
    while numberToFactor > 1:
        for number in primes:
            if numberToFactor % number == 0:
                numberToFactor /= number
                factors.append(number)
    end = timer()
    print("Factors generated!")    
    print("Time taken:", end-start, "s")
    return factors

while True:
    x = int(input("Which number would you like to prime factor: "))
    print(factor(x, generatePrimes(10000)))