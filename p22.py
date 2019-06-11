from pprint import pprint
import string
values = dict(zip(string.ascii_lowercase, range(1,27)))
names = []
with open("p022_names.txt", "r") as file:
    for line in file:
        names.append(line.replace('"', '').split(","))

def sumWord(word):
    lst = list(word.lower())
    score = 0
    for char in lst:
        score += (values[char])
    return score


names[0].sort()
names = names[0]
scores = []
total = 0
for x in range(0,len(names)):
    _score = sumWord(names[x]) * (x+1)
    if names[x] == "COLIN":
        print(_score)
    scores.append(_score)

print(scores[937])
print(sum(scores))