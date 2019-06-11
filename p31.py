import itertools
from timeit import default_timer as timer

coins = [1,2,5,10,20,50,100,200]
total = []
def waysToFind(lst,amount):
    global total
    # for amount in amounts:
    candidates = []
    if amount == 0:
        # print(lst)
        total.append(lst)
        return 0
    elif amount == 1:
        lst.append(1)
        amount -= 1
        total.append(lst)
        # print(lst)
        return 0
    else:
        for coin in coins[::-1]:
            if amount - coin >= 0:
                candidates.append(coin)

    for coin in candidates:
        waysToFind(lst+[coin],amount-coin)
        

change = 200
start = timer()
waysToFind([],change)
end1 = timer()
total.sort()
for item in total:
    item.sort()

unique = []
for item in total:
    if item not in unique:
        unique.append(item)
end = timer()
print(len((unique)))
print("Time taken total:", end-start, "s")
print("Time taken calculations:", end1-start, "s")
# for coin in coins[::-1]:
#     if change - coin > 0:
#         print(coin,5-coin)