num = [1,0]
denom = [1,0]

while num < 100:
    while denom < 100:
        frac = num/denom
        if num[0]/denom[0] == frac or num[1]/denom[0] == frac or num[0]/denom[1] == frac or num[1]/denom[1] == frac:
            print(num,denom)