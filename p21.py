from euler import sumOfFact, generatePrimes

def testAmi(num):
    # a = num
    d_a = sumOfFact(num) # b
    d_b = sumOfFact(d_a) # a
    if d_b == num and d_a != num:
        return True
    else:
        return False

ami = []
for x in range(2,10000):
    if x % 1000 == 0:
        print(x)
    if testAmi(x):
        ami.append(x)
print(ami)
print(sum(ami))