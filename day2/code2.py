#!/usr/bin/env python

def dif(s1,s2):
	t = 0
	for i in range(0, len(s1)):
		if not s1[i] == s2[i]:
			t = t + 1

	return t

def com(s1,s2):
	out = ""
	for i in range(0, len(s1)):
		if s1[i] == s2[i]:
			out += s1[i]
	return out

input = list(map( lambda x: x.strip(), open("input.txt").readlines() ))

minCount = len(input[0])
packId = ""
for i in input:
	for j in input:
		if i == j:
			continue
		else:
			d = dif(i,j)
			if d < minCount:
				minCount= d
				packId = (i,j)
				#print (dif(i,j), i, j)


print( packId, minCount)
print( com(packId[0], packId[1] ) )