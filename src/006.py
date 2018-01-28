import math
value = 100
powerOfSum = 0
sumOfPower = 0
for i in range(1, value + 1):
    powerOfSum += i
    sumOfPower += math.pow(i, 2)
powerOfSum = math.pow(powerOfSum, 2)
diff = powerOfSum - sumOfPower
print(int(diff))