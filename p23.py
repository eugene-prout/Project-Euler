from euler import generatePrimes, sumOfFactors

def isAbudant(num,primes):
    if sumOfFactors(num,primes) > num:
        return True
    else:
        return False

primeLst = generatePrimes(10000)
abuntants = []
for x in range(2,28123):
    if isAbudant(x,primeLst):
        abuntants.append(x)

cannotBeWritten = list(range(28124))

for i in range(0,len(abuntants)):
    for j in range(0, len(abuntants)):
        if (abuntants[i] + abuntants[j] <= 28123):
            try:
                cannotBeWritten.remove(abuntants[i]+abuntants[j])
            except ValueError:
                pass  # do nothing!
        else:
            break

_sum = 0
print(sum(cannotBeWritten))