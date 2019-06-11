def sumOfFactors(number, primes):
    _sum = 1
    p = primes[0]
    i = 0
    j = 0
    n = number
    while (p * p <= n and n > 1 and i < len(primes)):
        p = primes[i]
        i += 1 
        if (n % p == 0):
            j = p * p
            n = n / p
            while (n % p == 0):
                j = j * p
                n = n / p
            _sum = _sum * (j - 1) / (p - 1)
    if n > 1:
        _sum *= n + 1
    return int(_sum - number)

def generatePrimes(_range):
    candidates = list(range(2, _range+1))
    p = 2
    while (p < len(candidates)):

        for number in candidates:
            if number % p == 0 and number != p:
                candidates.remove(number)
        p = candidates[candidates.index(p) + 1]
    return candidates

def inst(string):
    return [int(x) for x in string.split(" ")]