#!/usr/bin/env python

serial = 1309
#serial=18
height=300
width=300

def calc(x,y,serial):
    rid = x + 10
    pl = y * rid
    return int(str((serial + pl) * rid)[-3]) - 5


puz = []
for y in range(1, height+1 ):
    tmp = []
    for x in range(1,width+1):
        tmp.append( calc(x,y,serial) )
    puz.append(tmp)


x = 0
y = 0
xwin=-1
ywin=-1
totalmax=0
sizewin=0

for y in range(0, height):
    for x in range(0, width):
        largetstBox = min([height-y, width-x])

        # all the boxes we can make here
        for boxes in range(1,largetstBox):
            total = sum(map( lambda z: sum(z[x:x+boxes]), puz[y:y+boxes]))
        
            if total > totalmax:
                xwin = x 
                ywin = y
                totalmax = total
                sizewin=boxes
                print("x:", xwin+1, " y:", ywin+1, " box size:", boxes, totalmax, serial)
            
            x += 1
            if (x+3) > len(puz[0]):
                x = 0
                y += 1
            if (y+3) > len(puz):
                break



print(xwin+1, ywin+1, sizewin)




