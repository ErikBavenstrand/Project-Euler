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
def numberOfDivisors(number):
    factorsList = prime_factors(number)
    factorsList.sort()
    numberOfFactorsList = []
    numberOfFactorsList.append(0)
    prevFactor = factorsList[0]
    factorNo = 0
    for i in range(0, len(factorsList)):
        factor = factorsList[i]
        if prevFactor == factor:
            numberOfFactorsList[factorNo] += 1
        else:
            factorNo += 1
            numberOfFactorsList.append(1)
        prevFactor = factor
    sum = 1
    for number in numberOfFactorsList:
        sum *= (number + 1)
    return sum
def triangularNumberOf(number):
    sum = 0
    for i in range(1, number + 1):
        sum += i
    return sum

i = 1
while numberOfDivisors(triangularNumberOf(i + 1)) <= 500:
    i += 1 
print(triangularNumberOf(i + 1))