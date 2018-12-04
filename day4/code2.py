#!/usr/bin/env python

import re
from datetime import datetime
import operator
from collections import Counter

"""
[1518-11-01 00:00] Guard #10 begins shift
[1518-11-01 00:05] falls asleep
[1518-11-01 00:25] wakes up
[1518-11-01 00:30] falls asleep
[1518-11-01 00:55] wakes up
[1518-11-01 23:58] Guard #99 begins shift
[1518-11-02 00:40] falls asleep
[1518-11-02 00:50] wakes up
[1518-11-03 00:05] Guard #10 begins shift
[1518-11-03 00:24] falls asleep
[1518-11-03 00:29] wakes up
[1518-11-04 00:02] Guard #99 begins shift
[1518-11-04 00:36] falls asleep
[1518-11-04 00:46] wakes up
[1518-11-05 00:03] Guard #99 begins shift
[1518-11-05 00:45] falls asleep
[1518-11-05 00:55] wakes up
"""


def parseDate(str):
	dt = str.split(']')[0][1:]
	datetime_object = datetime.strptime(dt, '%Y-%m-%d %H:%M')
	return datetime_object.timestamp()


def getMin(str):
	g = re.match(r'\[.*-.*-.* (..):(..)\].*', str)
	#print(g.group(1), g.group(2))
	if g.group(1) == '23':
		return 0
	else:
		return g.group(2)


inputs = list(map( lambda x: x.strip(), open("input.txt").readlines() ))
inputs.sort(key=parseDate)

currentG = False
sleepStart = False
minStart = False
minEnd = False

gTime = {}
gMins = {}

for g in inputs:
	m = re.match(r'.*Guard #(.*) begins shift', g)
	if m:
		currentG = int(m.group(1))
		continue

	if re.match(r'.*falls asleep', g):
		sleepStart = parseDate(g)
		minStart = getMin(g)
		#print(currentG, 'is sleeping', sleepStart)
	elif re.match(r'.*wakes up', g):
		awakeStart = parseDate(g)
		sleepTime = ( abs(sleepStart) - abs(awakeStart))/60
		minEnd = getMin(g)
		#print(currentG, 'wakes up, sleep time', sleepTime )
		if currentG in gTime:
			gTime[currentG] += sleepTime
		else:
			gTime[currentG] = sleepTime


		if not currentG in gMins:
			gMins[currentG] = []
		for x in range(int(minStart), int(minEnd)):
			gMins[currentG].append(x)


## find out what guard sleeps the most at the same time each day
## the second number in the tupl that is returned to b is what we are
## looking for;  find the max value there, and then mulitple the
## first value in the tupl by the guard number.
for g in gTime:
	b = Counter(gMins[g] )
	print(g, b.most_common(1))




