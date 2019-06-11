lst = []

for x in range(2,101):
    for y in range(2,101):
        lst.append(x**y)

st = set(lst)
print(len(st))