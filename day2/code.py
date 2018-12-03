#!/usr/bin/env python

def calc(l):
	t = {}

	for letter in list(l):
		if letter in t:
			t[letter] += 1
		else:
			t[letter] = 1

	twoCount = 0
	threeCount = 0

	for z in t:
		if t[z] == 2:
			twoCount = 1
		if t[z] == 3:
			threeCount = 1

	return (twoCount, threeCount)

two_total = 0
three_total = 0

for lines in open("input.txt"):
	(two,three) = calc(lines.strip())
	two_total += two
	three_total += three

print(two_total * three_total)
