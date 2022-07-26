inputFile = open("bendin.txt", "r")
outputFile = open("bendout.txt", "w")

line1 = inputFile.readline().split()
line2 = inputFile.readline().split()

x11 = int(line1[0])
x21 = int(line1[2])
y11 = int(line1[1])
y21 = int(line1[3])

x12 = int(line2[0])
x22 = int(line2[2])
y12 = int(line2[1])
y22 = int(line2[3])

# area of 1st rectanble
area1 = (x21 - x11) * (y21 - y11)

# area of 2nd rectanble
area2 = (x22 - x12) * (y22 - y12)

# difference in area and subtracting it away

# finding overlapping x values
# 2 cases, 2nd rectangle's left x is inside 1st rectangle's range or 2nd rectangle's right x is inside 1st rectangle's range
# just use two for loops
overlapX = 0
overlapY = 0

for i in range(x11, x21 + 1):
    for j in range(x12, x22 + 1):
        if i == j:
            overlapX += 1
overlapX -= 1

for i in range(y11, y21 + 1):
    for j in range(y12, y22 + 1):
        if i == j:
            overlapY += 1
overlapY -= 1

totalArea = area1 + area2 - overlapX * overlapY

outputFile.write("%d\n" % (totalArea))
# vice versa for y

inputFile.close()
outputFile.close()