from timeit import default_timer as timer

def permute(k,a,lst):
    if k == 1:
        lst.append(a[:])

    else:
        permute(k-1,a,lst)
        for i in range(k-1):
            if k % 2 == 0:
                a[i], a[k-1] = a[k-1], a[i]
            else:
                a[0], a[k-1] = a[k-1], a[0]
            permute(k-1,a,lst)
    
start = timer()
v = [0,1,2,3,4,5,6,7,8,9]
# k must equal total len of v
x = []
permute(10,v,x)
x.sort()
end = timer()
print(x[999999])
print("Time taken:", end-start, "s")