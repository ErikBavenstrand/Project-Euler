import math
listofprimes = []
def isPrime(number):
    for i in listofprimes:
        if i > int(math.sqrt(number)):
            break
        if number % i == 0:
            return False
    listofprimes.append(number)
    return True
value = 0
i = 2
primeNo = 0 
while primeNo < 10001:
    if isPrime(i):
        primeNo += 1
        value = i
    i += 1
print(value)