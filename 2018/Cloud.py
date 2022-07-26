inputFile = open("cloudin.txt", "r")
outputFile = open("cloudout.txt", "w")
line = inputFile.readline().split()
N = int(line[0])
K = int(line[1])

lines = inputFile.readlines();
for i, l in enumerate(lines):
    lines[i] = int(l.strip('\n'))

# min contiguous subarray of size K
distances = []
for i in range(len(lines) - K + 1):
    print(i)
    print(K)
    if distances == []:
        distances.append(sum(lines[i:K]))
    else:
        distances.append(distances[-1] - lines[i - 1] + lines[i + K - 1])

outputFile.write("%d\n" % (min(distances)))


# output max distance + the max of the distances from both ends of the group


inputFile.close()
outputFile.close()