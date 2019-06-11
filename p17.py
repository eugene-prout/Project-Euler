values = {
    0: "",
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine"

}

teens = {
    0: "",
    10: "ten",
    11: "eleven",
    12: "twelve",
    13: "thirteen",
    14: "fourteen",
    15: "fiften",
    16: "sixteen",
    17: "seventeen",
    18: "eighteen",
    19: "nineteen"
}
tens = {
    0: "",
    2: "twenty",
    3: "thirty",
    4: "forty",
    5: "fifty",
    6: "sixty",
    7: "seventy",
    8: "eighty",
    9: "ninety"
}

def words(num,values,teens,tens):
    y = num
    leng = len(y)
    place = len(y)  # place value of number
    word = []
    hundred = False
    while place > 0:
        # If integer is in teens

        if int(''.join(map(str,y))) in teens:
            if hundred:
                word.append("and")
            word.append(teens[int(''.join(map(str,y)))])
            break
        else:
            front = y.pop(0)
            if place == 3:
                word.append(values[front])
                word.append("hundred")
                hundred = True
           
            if place == 2:
                if hundred:
                    word.append("and")
                    
                word.append(tens[front])
            if place == 1:
                word.append(values[front])

        place -= 1
    counter = 0
    for item in word:
        counter += len(item)
    return counter


class NumberCounter:
    def __init__(self):
        
        self.values = {
        0: "",
        1: "one",
        2: "two",
        3: "three",
        4: "four",
        5: "five",
        6: "six",
        7: "seven",
        8: "eight",
        9: "nine"
        }
        self.teens = {
            0: "",
            10: "ten",
            11: "eleven",
            12: "twelve",
            13: "thirteen",
            14: "fourteen",
            15: "fifteen",
            16: "sixteen",
            17: "seventeen",
            18: "eighteen",
            19: "nineteen"
        }
        self.tens = {
            0: "",
            2: "twenty",
            3: "thirty",
            4: "forty",
            5: "fifty",
            6: "sixty",
            7: "seventy",
            8: "eighty",
            9: "ninety"
        }

    def count(self,num):
        self.lst = [int(x) for x in str(num)]

        self.y = self.lst
        self.leng = len(self.y)
        self.place = len(self.y)  # place value of number
        self.word = []
        self.hundred = False
        while self.place > 0:
            # If integer is in teens

            if int(''.join(map(str,self.y))) in self.teens:
                if self.hundred:
                    self.word.append("and")
                    self.hundred = False
                self.word.append(self.teens[int(''.join(map(str,self.y)))])
                break
            else:
                self.front = self.y.pop(0)
                if self.place == 3:
                    self.word.append(values[self.front])
                    self.word.append("hundred")
                    if self.y.count(0) == 2:
                        break
                    self.hundred = True
            
                if self.place == 2:
                    if self.hundred:
                        self.word.append("and")
                        self.hundred = False
                        
                    self.word.append(tens[self.front])
                if self.place == 1:
                    self.word.append(values[self.front])

            self.place -= 1
        self.counter = 0
        for item in self.word:
            self.counter += len(item)
            
        return self.counter

if __name__ == "__main__":
    total = 0
    count = NumberCounter()
    for i in range(1,1000):
        total += count.count(i)
    print(total)
    # for i in range(700,1000):
    #     print(count.count(i))