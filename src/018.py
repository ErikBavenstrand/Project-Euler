inputFile = open(r'./resources/018.txt', 'r')
triangleList = [[]]
for line in inputFile.readlines():
    triangleList.append(line.split(" "))
triangleList.remove([])
triangleList.reverse()
upper = 0
lower = 0
line = 0
while line < len(triangleList):
    while upper + 1 < len(triangleList[line]):
        if int(triangleList[line][upper]) + int(triangleList[line + 1][lower]) < int(triangleList[line][upper + 1]) + int(triangleList[line + 1][lower]):
            triangleList[line + 1][lower] = int(triangleList[line][upper + 1]) + int(triangleList[line + 1][lower])
        else:
            triangleList[line + 1][lower] = int(triangleList[line][upper]) + int(triangleList[line + 1][lower])
        upper += 1
        lower += 1
    line += 1
    upper = 0
    lower = 0
triangleList.reverse()
print "The maximum sum is ", triangleList[0][0]