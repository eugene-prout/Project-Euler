import json
from timeit import default_timer as timer

# int: stepToEnd
correctNumbers = {}

def PrintDict(dictToPrint):
    print(json.dumps(dictToPrint, indent=4, sort_keys=True))

def Collatz(count,currentNumber,sequence):
    count = count + 1
    sequence.append(currentNumber)
    
    # if currentNumber in list(correctNumbers.keys()):
    #     for index,number in enumerate(sequence):
    #         #print(number,index+1, len(sequence))
    #         stepsFromCurrent = correctNumbers[currentNumber]

    #         amountFromCurrent = abs(index-len(sequence)+1)
    #         correctNumbers[number] = amountFromCurrent + stepsFromCurrent
    #     return 0
      
    
    if currentNumber == 1:
        # Base Case
        
        for index,num in enumerate(reversed(list(range(count)))):
            correctNumbers[sequence[num]] = index+1


        
        # PrintDict(correctNumbers)
        # print(count)

    elif currentNumber % 2 == 0:
        # Even
        Collatz(count, currentNumber/2,sequence)
        
    else:
        # Odd
        Collatz(count,currentNumber*3+1,sequence)

def test():
    start = timer()
    for x in range(1,1000000):
        if x % 10000 == 0:
            print(x)
        Collatz(0,x,[])
    print(x)


    print(max(correctNumbers, key=correctNumbers.get))
    end = timer()
    print("Time: ", end-start)

def REPL():
    while 1:
        x = int(input("Start term:"))
        Collatz(0,x,[])
        PrintDict(correctNumbers)



for x in range(1,1000000):
    print(x)
    Collatz(0,x,[])

print(max(correctNumbers, key=correctNumbers.get))