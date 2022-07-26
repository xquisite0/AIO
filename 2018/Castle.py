from collections import Counter
inputFile = open("cavalryin.txt", "r")
outputFile = open("cavalryout.txt", "w")
lines = inputFile.readlines()
lines.pop(0);
for i, line in enumerate(lines):
    lines[i] = line.strip('\n')


counter = Counter(lines)
answer = ""
for item, count in counter.items():
    if count % int(item) != 0:
        answer = "NO"

if answer == "":
    answer = "YES"
outputFile.write("%s\n" % (answer))


inputFile.close()
outputFile.close()