import math
#Finding all prime factors from stackoverflow
def prime_factors(n):
    """Returns all the prime factors of a positive integer"""
    factors = []
    d = 2
    while n > 1:
        while n % d == 0:
            factors.append(d)
            n /= d
        d = d + 1

    return factors

number = 20
primeDivisorsList = [0] * number
templist = []
sum = 1
for i in range(2, number):
    templist = [0] * 20
    for j in prime_factors(i):
        templist[j] += 1
    m = 0
    while m <= i:  
        if templist[m] > primeDivisorsList[m]:
            primeDivisorsList[m] = templist[m]
        m += 1
index = 0
for k in primeDivisorsList:
    sum *= math.pow(index, k)
    index += 1
print(int(sum))