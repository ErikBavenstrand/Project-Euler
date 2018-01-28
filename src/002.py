maxValue = 4000000
sum = 0
last = 0
prev = 0
curr = 1
while curr < int(maxValue):
    last = prev
    prev = curr
    if curr % 2 == 0:
        sum += curr
    curr = last + prev
print(sum)