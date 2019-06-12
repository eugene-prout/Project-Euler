num = [1,0]
denom = [1,0]
denom_i = 10

def findCommon(lst1,lst2):
    for e1 in lst1:
        if e1 in lst2:
            return e1
    return False

def canCancel(num_i,denom_i):
    num = [int(x) for x in str(num_i)]
    denom = [int(x) for x in str(denom_i)]
    frac = num_i/denom_i
    if frac > 1:
        return False
    common = findCommon(num,denom)
    # No common element
    if common == 0:
        return False
    # Cases such as: 55/66 (trivial)
    if num.index(common) == denom.index(common):
        return False
    num.remove(common)
    denom.remove(common)
    if denom[0] == 0:
        return False
    if num[0] / denom[0] == frac:
        return True
   

for num_i in range(10,100):
    for denom_i in range(10,100):
        if canCancel(num_i,denom_i):
            print(num_i,denom_i)
    