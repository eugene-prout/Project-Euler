from timeit import default_timer as timer

def generatePrimes(_range):
    candidates = list(range(2, _range+1))
    successful = []
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
    return successful

primes = generatePrimes(110000)
print(primes[10000])