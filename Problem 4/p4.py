from math import ceil as ceiling, floor

def testPalin(number):
    number = [int(x) for x in str(number)]
    length = len(number)
    mid = length/2

    if length % 2 == 1:

        mid2 = ceiling(mid)
        mid1 = floor(mid)
        lower = number[0:mid1]
        upper = number[mid2:length][::-1]
    else:
        lower = number[0:int(mid)]
        upper = number[int(mid):length][::-1]

    if (upper == lower):
        return True
    else:
        return False

def generatePalindrones():
    lst = []
    for x in range(100,1000):
        for y in range(100,1000):
            multiple = x * y
            
            if testPalin(multiple) and multiple > 10:
                lst.append(multiple)

    return lst

print(generatePalindrones())