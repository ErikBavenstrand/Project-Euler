import math
listOfPrimes = []
def isPrime(number):
    for prime in listOfPrimes:
        if prime > int(math.sqrt(number)):
            break
        if number % prime == 0:
            return False
    listOfPrimes.append(number)
    return True
sum = 0
for i in range(2, 2000000):
    if isPrime(i):
        sum += i
print(sum)