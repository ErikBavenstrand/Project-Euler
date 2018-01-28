listData = [[0 for x in range(21)] for y in range(41)]
def binomial(overNumber, underNumber):
    if overNumber == underNumber or underNumber == 0:
        return 1
    if listData[overNumber][underNumber] != 0:
        return listData[overNumber][underNumber]
    if listData[overNumber][underNumber] == 0:
        listData[overNumber][underNumber] = binomial(overNumber - 1, underNumber - 1) + binomial(overNumber - 1, underNumber)
    return listData[overNumber][underNumber]
ways = binomial(40, 20)
print(ways)