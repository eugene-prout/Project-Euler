_sum = 0

for x in range(2,1000000):
    lst = [int(x) for x in str(x)]
    total = sum([x**5 for x in lst])
    if total == x:
        _sum += x
    
print(_sum)