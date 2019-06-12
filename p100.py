import functools

@functools.lru_cache(maxsize=None)
def forumla(b,r):
    return b**2-b-2*b*r-r**2+r

for b in range(0,10000000000000):
    if b % 100000:
        print(b)
    for r in range(0,10000000000000):
        if forumla(b,r) == 0 and b+r>1000000000000:
            print(b,r)