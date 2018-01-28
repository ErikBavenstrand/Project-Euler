def collatzChain(startNumber):
    number = startNumber
    count = 1
    while number != 1:
        count += 1
        number = getNextCollatz(number)
    return count
def getNextCollatz(number):
    if number % 2 == 0:
        return (number / 2)
    return (number * 3) + 1
i = 1
longestChainNumber = 0
longestChain = 0
for i in range(1, 100000):
    count = collatzChain(i)
    if count > longestChain:
        longestChain = count
        longestChainNumber = i
    print(longestChainNumber)
print(longestChainNumber)