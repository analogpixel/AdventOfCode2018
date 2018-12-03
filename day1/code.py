#!/usr/bin/env python

total = 0
all_num = {}
found = False
firstRun = True

while not found:
	for lines in open("input1.txt"):
		if lines[0] == "+":
			total += int(lines[1:])
		else:
			total -= int(lines[1:])

		if total in all_num:
			if not found:
				print("twice:", total)
			found = True
		else:
			all_num[total] = True
	if firstRun:
		print(total)
		firstRun = False