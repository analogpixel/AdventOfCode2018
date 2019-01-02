#!/usr/bin/env python



# pip install pypng

# 36983 is wrong

# 21509 is too low
# 40427 is too high
# 40432 is too high

import numpy as np 
from asciimatics.screen import Screen
import png
import re

input_file = "input.txt"
w=2000
h=2000
ymax=0
ymin=1000
xmax=0
xmin=1000

class drop:
    def __init__(self, x,y, direction, moving=True):
        self.x = x
        self.y = y
        self.direction = direction
        self.moving = moving

def loadMap(filename):
    global ymax,ymin

    ## Build the initil map
    mymap = np.full((w+2,h+2), 0)
    input = list(map( lambda x: x.strip(), open(filename).readlines() ))
    for line in input:    
        (p1,p2) = line.split(',')
        p1 = int(p1.split('=')[1])
        p2 = p2.split('=')[1]
        (p2_1, p2_2) = map(int, p2.split('..'))

        if line[0] == 'x':
            for y in range(p2_1, p2_2+1):
                mymap[y][p1] = 3
                if y > ymax:
                    ymax = y
                if y < ymin:
                    ymin = y
        elif line[0] == 'y':
            for x in range(p2_1, p2_2+1):
                mymap[p1][x] = 3
                if p1 > ymax:
                    ymax = p1
                if p1 < ymin:
                    ymin = p1
    return mymap 

def move(mymap, droplets):
    global ymax
    for d in droplets:
        while d.moving:
            # if you have fallen off the screen stop
            if d.y > ymax:
                d.moving = False
            # if you hit a wall
            elif mymap[d.y][d.x + d.direction] > 1:
                d.moving = False
            # if the block under you doesn't exist, fall
            elif mymap[d.y+1][d.x] < 2:
                while mymap[d.y+1][d.x] < 2:
                    d.y += 1
                    if d.y > ymax:
                        d.moving = False
                        break
                    mymap[d.y][d.x] = 1
                d.moving = False
                # when you hit the ground, spawn off two new drops 
                move(mymap, [drop(d.x, d.y, -1), drop(d.x,d.y, 1)] )
            else:
                d.x += d.direction
                mymap[d.y][d.x] = 1

    # ['.','|','~','#']
    for dd in [ droplets[0].y, droplets[1].y]:
        st = "".join(map(lambda x: str(int(x)), mymap[dd] ))
        m = re.search(r'31+3', st)
        if m:
            (i,j) = m.span()
            for z in range(i+1,j-1):
                mymap[dd][z] = 2
            
    return droplets

def updateMap(mymap, left, right):
    (left, right) = move(mymap, [ drop(500,0, -1), drop(500,0,1)] )

def tran(x):
    a = {0: 90, 1: 150, 2: 200, 3:255}
    return [a[y] for y in x]

def saveMap(mymap, i):
    png.from_array(list(map(tran,mymap)), 'L;8').save("out/map_{:04d}.png".format(i))

def drawMap(screen):
    mymap = loadMap(input_file)
    view_width = 80
    view_height = 40
    view_x = 490
    view_y = 0
    pic = ['.','|','~','#']
    while True:

        
        ev = screen.get_key()
        if ev in (ord('n'), ord('N')):
            if ev == ord('n'):
                cc =1
            else:
                cc = 200

            for ittr in range(0, cc):

                screen.print_at("ittr: {}".format(ittr), 85,6)
                move(mymap, [drop(500, 0, -1), drop(500,0,1,False)] )

                if ittr % 10 == 0:
                    count = 0
                    standing_count = 0
                    for xx in range(0, w):
                        for yy in range(ymin, ymax+1):
                            if mymap[yy][xx] in [1,2]:
                                count +=1
                            if mymap[yy][xx] == 2:
                                standing_count +=1
        
                    screen.print_at( "Total Water Count: {}".format(count), 85,5)
                    screen.print_at( "Standing Water Count: {}".format(standing_count), 85,4)
                    screen.refresh()

                #saveMap(mymap, ittr)
                
            
        if ev in (ord('q'), ord('Q')):
            quit()
  
        # print the map out
        for xx in range(0, view_width):
            for yy in range(0, view_height):
                screen.print_at( pic[mymap[view_y + yy][view_x + xx]] , xx,yy)
        
        screen.refresh()
        




Screen.wrapper(drawMap)
