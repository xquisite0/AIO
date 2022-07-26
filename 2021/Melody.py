#!/usr/bin/env python
import sys

sys.setrecursionlimit(1000000000)

#
# Solution Template for Melody
# 
# Australian Informatics Olympiad 2021
# 
# This file is provided to assist with reading and writing of the input
# files for the problem. You may modify this file however you wish, or
# you may choose not to use this file at all.
#

# N is the number of notes.
N = None

# K is the largest number which could be a note.
K = None

# S contains the sequence of notes forming the song.
S = []

answer = None

# Open the input and output files.
input_file = open("melodyin.txt", "r")
output_file = open("melodyout.txt", "w")

# Read the value of N and K.
input_line = input_file.readline().strip()
N, K = map(int, input_line.split())

# Read each note in the song.
for i in range(0, N):
    S.append(int(input_file.readline().strip()))

# TODO: This is where you should compute your solution. Store the smallest
# possible number of notes Melody can change so that her song is nice into the
# variable answer.

seen_first = {}
seen_second = {}
seen_third = {}

for i in range(0, len(S), 3):
    curFirst = str(S[i])
    curSecond = str(S[i+1])
    curThird = str(S[i+2])
    if curFirst not in seen_first:
        seen_first[curFirst] = 0
    seen_first[curFirst] += 1
    if curSecond not in seen_second:
        seen_second[curSecond] = 0
    seen_second[curSecond] += 1
    if curThird not in seen_third:
        seen_third[curThird] = 0
    seen_third[curThird] += 1

currentFirstHighest = 0
usedFirst = None
for first, occurrences in seen_first.items():
    if occurrences > currentFirstHighest:
        usedFirst = first
        currentFirstHighest = occurrences

currentSecondHighest = 0
usedSecond = None
for second, occurrences in seen_second.items():
    if occurrences > currentSecondHighest:
        usedSecond = second
        currentHighest = occurrences

currentThirdHighest = 0
usedThird = None
for third, occurrences in seen_third.items():
    if occurrences > currentThirdHighest:
        usedThird = third
        currentThirdHighest = occurrences

usedTriplet = usedFirst + usedSecond + usedThird

pointer = answer = 0

usedTriplet = list(usedTriplet)
for index in range(len(S)):
    if S[index] != int(usedTriplet[pointer]):
        answer += 1
    if pointer == 2:
        pointer = 0
    else:
        pointer += 1

# Write the answer to the output file.
output_file.write("%d\n" % (answer))

# Finally, close the input/output files.
input_file.close()
output_file.close()