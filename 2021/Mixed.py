inputFile = open("mixin.txt", "r")
outputFile = open("mixout.txt", "w")

line = inputFile.readline().split()
numerator = int(line[0])
denominator = int(line[1])

if denominator == 0:
    outputFile.write("%d\n" % (numerator))
else:
    quotient = numerator // denominator
    remainder = numerator % denominator
    if remainder == 0:
        outputFile.write("%d\n" % (quotient))
    else:
        outputFile.write("%d %d/%d\n" % (quotient, remainder, denominator))

inputFile.close()
outputFile.close()