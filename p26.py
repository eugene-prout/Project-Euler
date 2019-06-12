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
    sublist = lst[:]
    sublist.pop(0)
    
    return len(sublist)

def decimal(num,denom):
    x = num
    y = denom
    _decimal = []

    while True:
        z = x // y
        _decimal.append(z)
        x = x % y
        x *= 10
        if _decimal.count(0) == 10:
            break
        tail = 0
        if len(_decimal) > 10:
            tail = checkDecimal(_decimal[:])
            if tail > 0:
                print("Reoccuring", denom, tail)
                break


def decimalNew(num,denom):
    found = 0
    

decimalNew(76,4995)
        