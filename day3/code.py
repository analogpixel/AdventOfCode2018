#!/usr/bin/env python

import numpy as np
import re

input = list(map( lambda x: x.strip(), open("input.txt").readlines() ))

maxX = 1000
maxY = 1000

data = np.zeros((maxY, maxX), dtype=int)
data_sub = np.zeros((maxY, maxX), dtype=int)
overlap = {}

for l in input:
	match     = re.search(r'#(.*)@(.*),(.*): (.*)x(.*)', l)
	if match:
		dataPoint = int(match.group(1))
		left      = int(match.group(2))
		top       = int(match.group(3))
		width     = int(match.group(4))
		height    = int(match.group(5))
		overlap[dataPoint] = False

		for x in range(0,width):
			for y in range(0,height):
				data[y+top][x+left] += 1

				if data[y+top][x+left] > 1:
					overlap[ data_sub[y+top][x+left] ] = True
					overlap[ dataPoint ] = True

				data_sub[y+top][x+left] = dataPoint

		#print(dataPoint, left, top, width, height)
	else:
		print("ERROR")


for i in overlap:
	if not overlap[i] :
		print(i)
