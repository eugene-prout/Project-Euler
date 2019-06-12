length = 0

for i in range(1000,1,-1):
    if length >= i:
        break
    
    foundRemain = [None] * i
    value = 1
    position = 0
    while(foundRemain[value] == 0 and value != 0):
        foundRemain[value] = position
        value *= 10
        value = value % i
        position += 1
    try:
        if position-foundRemain[value] > length:

            length = position - foundRemain[value] 
    except TypeError:
        pass

print(length)