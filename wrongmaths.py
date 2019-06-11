def formula(m,y,z):
    return m ** 2 - m * (z+y) + 10 * y + z

for m in range(1,100):
    for y in range(1,100):
        for z in range(1,10):
            if formula(m,y,z) == 0:
                print(m,y,z)