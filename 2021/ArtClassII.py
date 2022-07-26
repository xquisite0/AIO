#!/usr/bin/env python
import sys
sys.setrecursionlimit(1000000000)

#
# Solution Template for Art Class II
# 
# Australian Informatics Olympiad 2021
# 
# This file is provided to assist with reading and writing of the input
# files for the problem. You may modify this file however you wish, or
# you may choose not to use this file at all.
#

# N is the number of holes.
N = None

# x and y contain the locations of the holes.
x = []
y = []

answer = None

# Open the input and output files.
input_file = open("artin.txt", "r")
output_file = open("artout.txt", "w")

# Read the value of N.
N = int(input_file.readline().strip())

# Read the location of each hole.
for i in range(0, N):
    input_line = input_file.readline().strip()
    xvalue, yvalue = map(int, input_line.split())
    x.append(xvalue)
    y.append(yvalue)

# TODO: This is where you should compute your solution. Store the area of the
# smallest poster that will cover all the holes into the variable answer.
print(x)
print(y)
minX, maxX, minY, maxY = min(x), max(x), min(y), max(y)
answer = (maxX - minX) * (maxY - minY)

# Write the answer to the output file.
output_file.write("%d\n" % (answer))

# Finally, close the input/output files.
input_file.close()
output_file.close()