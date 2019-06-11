from timeit import default_timer as timer

longestSeries = []

def Collatz(series):
    global longestSeries
    length = len(series)
    number = series[length-1]
    if number == 1:
        if length > len(longestSeries):
            longestSeries = series
        return 0
    if number in longestSeries:
        # print("Found: ",number)
        if longestSeries.index(number) < (length - 1):
            # print("Updating")
            
            del longestSeries[0:longestSeries.index(number)+1]
            longestSeries = series+ longestSeries 
            return 0
        else:
            # print("No update")
            return 0

    if number % 2 == 0:
        series.append(number/2)
    else:
        series.append(3*number+1)
    Collatz(series)

def test():
    start = timer()
    for x in range(1000000,1,-1):
        if x % 10000 == 0:
            print(x)
        Collatz([x])

    end = timer()
    print("Time: ", end-start)

test()
