# libraries
from urllib.request import Request, urlopen
import json


# functions
def maxConsecutive0(res):
    return max(map(len, res.split("1")))

def maxConsecutive1(res):
    return max(map(len, res.split("0")))


# main code
req = Request('https://drand.cloudflare.com/public/latest', headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; '
                                                                                   'WOW64; rv:31.0) Gecko/20130401 '
                                                                                   'Firefox/31.0'})
strData = urlopen(req).read()
strData = strData.decode()

data = []
for i in range(1, 101, 1):
    data.append(0)
data.insert(100, json.loads(strData)) # converts a JSON string (containing all the latest data from League of Entropy) into a Python dictionary

print("Last round:", data[100]["round"])
round = data[100]["round"]
print("Last round's randomness:", data[100]["randomness"], "\n")

# lines 31-39: the data list is filled with data from the previous 99 rounds
i = 99
for r in range(round-1, round-100, -1):
    req = Request(f'https://drand.cloudflare.com/public/{r}', headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; '
                                                                                     'WOW64; rv:31.0) Gecko/20130401 '
                                                                                     'Firefox/31.0'})
    strData = urlopen(req).read()
    strData = strData.decode()
    data[i] = json.loads(strData)
    i -= 1

data = data[1:] # data[0] is zero for some reason
with open("dataUsed.txt", "w") as f:
    for i in range(len(data)):
        f.write(str(data[i])+"\n")

tmp = "".join(str(data[i]["randomness"]) for i in range(len(data))) # concatenates the strings, containing the randomness of 100 rounds

res = "".join(format(ord(i), "08b") for i in tmp) # converts previous string into a binary sequence
print("After string to binary conversion:", res, "\n")

print("Maximum length of sequence with consecutive 0’s:", maxConsecutive0(res))
print("Maximum length of sequence with consecutive 1’s:", maxConsecutive1(res))
