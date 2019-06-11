def topLeft(n):
    return (2*n+1)**2 - 2*n

def topRight(n):
    return (2*n+1)**2

def botLeft(n):
    return (2*n+1)**2 - 4*n

def botRight(n):
    return (2*n+1)**2 - 6*n

def sumDegree(n):
    return botLeft(n) + botRight(n) + topLeft(n) + topRight(n)

def sumTotal(n):

    counter = 1
    for x in range(1,n+1):
        counter += sumDegree(x)
    return counter

print(sumTotal(500))