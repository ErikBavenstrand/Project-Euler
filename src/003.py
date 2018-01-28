import math
def isPrime (number):
    temp = number
    for i in range(2, temp):
        if number % i == 0:
            return False
    return True

value = 600851475143
i = int(math.sqrt(value))
prime = 0
while i > 0:
    if value % i == 0:
        if isPrime(i):
            prime = i
            break
    i -= 1
print(prime)
