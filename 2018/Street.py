import math
inputFile = open("streetin.txt", "r")
outputFile = open("streetout.txt", "w")
line = inputFile.readline().split()

chunks = int(line[0])
parks = int(line[1])
houses = chunks - parks

largest = math.ceil(houses / (parks + 1))

outputFile.write("%d\n" % (largest))


inputFile.close()
outputFile.close()