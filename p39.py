# a^2 + b^2 = c^2

def checkForTriple(a,b,c):
    if a**2 + b**2 == c:
        return True
    else:
        return False

triples = []
for x in range(1,1000):
    for y in range(1,1000):
        c = x**2 + y**2
        if c**0.5 == int(c**0.5):
            triples.append([x,y,c**0.5])

for triple in triples:
    triple.sort()


found = []
max_count = 0
max_p = 0
for p in range(1,1000):
    for triple in triples:
        if triple[0] + triple[1] + triple[2] == p and triple not in found:
            found.append(triple)
            print(triple)
    if len(found) > max_count:
        max_count = len(found)
        max_p = p
    found.clear()
        
print(max_p)