#!/usr/bin/env python
import sys
sys.setrecursionlimit(1000000000)

#
# Solution Template for Robot Vacuum
# 
# Australian Informatics Olympiad 2021
# 
# This file is provided to assist with reading and writing of the input
# files for the problem. You may modify this file however you wish, or
# you may choose not to use this file at all.
#

# K is the number of instructions.
K = None

# instrs contains the sequence of instructions.
instrs = None

answer = None

# Open the input and output files.
input_file = open("robotin.txt", "r")
output_file = open("robotout.txt", "w")

# Read the value of K and the sequence of instructions from the input file.
K = int(input_file.readline().strip())
instrs = input_file.readline().strip()

# TODO: This is where you should compute your solution. Store the fewest number
# of instructions you need to add to the end of the sequence into the variable
# answer.
vert = hori = 0
for instr in instrs:
    if instr == 'N':
        vert += 1
    elif instr == 'S':
        vert -= 1
    elif instr == 'E':
        hori += 1
    else:
        hori -= 1
answer = abs(vert) + abs(hori)

# Write the answer to the output file.
output_file.write("%d\n" % (answer))

# Finally, close the input/output files.
input_file.close()
output_file.close()