#!/usr/bin/env python

# pip install z3-solver
# https://www.josephkirwin.com/2017/11/16/constraint-solver-tips/

import re
from z3 import *

input_file = "input.txt"
#input_file = "test_input2.txt"

input = list(map( lambda x: x.strip(), open(input_file).readlines() ))

bots = []
maxx,minx,maxy,miny,maxz,minz = (0,0,0,0,0,0)

for i in range(0, len(input)):
    m = re.match( r'pos=<(.*)>, r=(.*)' , input[i])
    size = int(m.group(2))
    pos = list(map(lambda x: int(x), m.group(1).split(',')))
    bots.append([pos, size])
    maxx = max( [ pos[0], maxx] )
    minx = min( [ pos[0], minx] )
    maxy = max( [ pos[1], maxy] )
    miny = min( [ pos[1], miny] )
    maxz = max( [ pos[2], maxz] )
    minz = min( [ pos[2], minz] )


o = Optimize()

x = Int('x')
y = Int('y')
z = Int('z')
o.add( x > minx)
o.add( x < maxx)
o.add( y > miny)
o.add( y < maxy)
o.add( z > minz)
o.add( z < maxz)

# abs that returns a z3 data type
def zabs(x):
    return If(x >= 0,x,-x)


# we need a list of values that can hold the condition of if <x,y,z> is in range of a robot, later
# in the program we'll take an x,y,z and populate the values with all the bots in range (1) or not (0)
# This is a list of Z3 Int types
# for example, if you had 6 bots:
# [bot_in_range_0, bot_in_range_1, bot_in_range_2, bot_in_range_3, bot_in_range_4, bot_in_range_5]
inRange = [ Int('bot_in_range_{}'.format(x)) for x in range(0,len(bots) )]


## Add checks for if a <x,y,z> position is in range to a bot
for i in range(len(bots)):
    # x,y,z are the z3 variable being optmized
    # 
    nx = bots[i][0][0]
    ny = bots[i][0][1]
    nz = bots[i][0][2]
    nr = bots[i][1]
    # can't use abs since it doesn't return a z3 data type, so write a custom z3 abs function that returns 
    # a valid z3 datatype
    # == adds a Static Single Assignment
    # assign 1 to the list item if <x,y,z> is in range of <nx,ny,nz>
    o.add( inRange[i] == If(zabs(x-nx) + zabs(y-ny) + zabs(z-nz) <= nr, 1, 0)) 

# sum up all the values in the inRange list (all 1's and 0's) and assign it to the botsInRange variable
botsInRange = Int('botsInRange')
o.add(botsInRange == sum(inRange) )

# create a variable to hold the distance of <x,y,z> from <0,0,0>
distanceFromZero = Int('dfz')
# calculate the distance from <0,0,0> and store it in the distanceFromZero variable
o.add(distanceFromZero == zabs(x) + zabs(y) + zabs(z))

max1 = o.maximize(botsInRange)
min1 = o.minimize(distanceFromZero)

print( o.check() )
#print( o.lower(min1), o.upper(min1))

print( o.model() )
