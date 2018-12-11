#!/usr/bin/env python

serial = 1309

def calc(x,y,serial):
    rid = x + 10
    pl = y * rid
    return int(str((serial + pl) * rid)[-3]) - 5


puz = []
for y in range(1, 301):
    tmp = []
    for x in range(1,301):
        tmp.append( calc(x,y,serial) )
    puz.append(tmp)


x = 0
y = 0
xwin=-1
ywin=-1
totalmax=0
while True:
    
    total = sum(puz[y][x:x+3]) + sum(puz[y+1][x:x+3]) + sum(puz[y+2][x:x+3])
    
    if total > totalmax:
        xwin = x 
        ywin = y
        totalmax = total
    
    x += 1
    if (x+3) > len(puz[0]):
        x = 0
        y += 1
    if (y+3) > len(puz):
        break



print(xwin+1, ywin+1, totalmax)




