#!/usr/bin/env python

import sys
sys.setrecursionlimit(22500)
input_file = "input.txt"
input = list(map( lambda x: x.strip(), open(input_file).readlines() ))

input_1 = "^WNE$"
input_2 = "^ENWWW(NEEE|SSE(EE|N))$"
input_3 = "(^ENNWSWW(NEWS|)SSSEEN(WNSE|)EE(SWEN|)NNN$)" #18
input_4 = "^ESSWWN(E|NNENN(EESS(WNSE|)SSS|WWWSSSSE(SW|NNNE)))$" #23
input_5 = "^WSSEESWWWNW(S|NENNEEEENN(ESSSSW(NWSW|SSEN)|WSWWN(E|WWS(E|SS))))$" #31

w = 300
h = 300
mymap = []
for i in range(0,h):
    mymap.append(list('#' * w))

path = list(input[0])

locs = []
x=w//2
y=h//2
while len(path) != 0:
    c = path.pop(0)
    if c == '(':
        locs.append( (x,y) )
    if c == ')':
        (x,y) = locs.pop()
    if c == '|':
        (x,y) = locs[-1]
    if c == 'N':
        mymap[y-1][x] = "-"
        mymap[y-2][x] = '.'
        y = y - 2
    if c == 'S':
        mymap[y+1][x] = "-"
        mymap[y+2][x] = '.'
        y = y + 2
    if c == 'W':
        mymap[y][x-1] = "|"
        mymap[y][x-2] = '.'
        x = x - 2
    if c == 'E':
        mymap[y][x+1] = "|"
        mymap[y][x+2] = '.'
        x = x + 2

mymap[15][15] = "X"

#for l in mymap:
#    print("".join(l))


door = ['|','-']

def walkMap(i,block,x,y,d):
    
    if d >= 1000:
        print(d,i)

    ds = [d]
    if mymap[y][x+1] in door and not block == 'W':
        #print(i, "Move east",  x+2,y)
        ds.append( walkMap(i+1,'E', x+2, y,d+1) )

    if mymap[y][x-1] in door and not block == 'E':
        #print(i, "move west", x- 2,y)
        ds.append( walkMap(i+1,'W', x-2, y, d+1))

    if mymap[y+1][x] in door and not block == 'N':
        #print(i, "Move south", x,y+2, block)
        ds.append( walkMap(i+1,'S', x,y+2, d+1) )

    if mymap[y-1][x] in door and not block == 'S':
        #print(i, "move north", x,y-2)
        ds.append( walkMap(i+1,'N', x,y-2, d+1) ) 
    
   
    return max(ds)


#print("start", w//2, h//2)
print(walkMap(0, '0', w//2, h//2, 0 ))