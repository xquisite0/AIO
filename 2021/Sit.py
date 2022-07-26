file = open("sitin.txt", "r")

firstline = file.readline().split()
seats = int(firstline[0]) * int(firstline[1])

patrons = int(file.readline())
sitting = standing = 0

if seats >= patrons:
    sitting = patrons
else:
    sitting = seats
    standing = patrons - seats

outputFile = open("sitout.txt", "w")
outputFile.write("%d %d\n" % (sitting, standing))