def checkReoccuring(decimal):
    lst = decimal[:]
    if 0 in lst:
        lst.remove(0)
    while len(lst) > 0:
        for splice in range(len(lst)):
            if lst[splice:] in lst[:splice] or lst[splice:] == lst[:splice] :
                #print("Recoccuring", lst[splice:])
                return True
        lst.pop(0)
    return False

def checkDecimal(lst):
    for x in range(1,len(lst)):
        substring = lst[x:]
        if lst.count(substring) > 1:
            count = len(substring)
            return count
    return 0

def decimal(num,denom):
    x = num
    y = denom
    _decimal = []

    while True:
        z = x // y
        _decimal.append(z)
        x = x % y
        #print(_decimal)
        x *= 10
        if _decimal.count(0) == 10:
            break
        tail = checkDecimal(_decimal)
        if tail > 0:
            print("Reoccuring", denom, tail)
            break

decimal(1,6)
for x in range(1,20):
    decimal(2,x)

        