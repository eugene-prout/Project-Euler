def createNum():
    lst = []
    for x in range(1,1000000):
        for digit in [int(z) for z in str(x)]:
            lst.append(digit)
    return lst

lst = createNum()
d1 = lst[0]
d10 = lst[9]
d100 = lst[99]
d1000 = lst[999]
d10000 = lst[9999]
d100000 = lst[99999]
d1000000 = lst[999999]
total = d1 * d10 * d100 * d1000 * d10000 * d100000 * d1000000
print(total)