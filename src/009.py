value = 0
c = 0
for a in range(1, 1001):
    for b in range(1, 1001):
        c = 1000 - a - b
        if a*a + b*b == c*c:
            value = a*b*c
            break
    if value != 0:
        break
print(value)