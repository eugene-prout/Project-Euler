from timeit import default_timer as timer

tree = [
] 


FILE = open("p067_triangle.txt", "r")
for blob in FILE: 
    tree.append([int(i) for i in blob.split(" ")])

start = timer()
for rIndex in range(100,1,-1):
    for index in range(1,rIndex):
        mx = max(tree[rIndex-1][index], tree[rIndex-1][index-1])
        tree[rIndex-2][index-1] += mx
end = timer()
print(tree[0][0])
print("Time taken:", end-start, "s")