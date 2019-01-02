#!/usr/bin/env python

# pip install pypng


import numpy as np 
import png
from asciimatics.screen import Screen

input_file = "test_input.txt"
w=2000
h=2000

class drop():
    def __init__(self, x,y):
        self.x = x
        self.y = y
        self.t = '|'
        self.moving = True

    def update(self, mymap):

        if not self.moving:
            return

        if mymap[self.y+1][self.x] in ['#','~']:
            if mymap[self.y][self.x+1] == '.':
                self.x += 1
            elif mymap[self.y][self.x-1] == '.':
                self.x -= 1
            elif mymap[self.y][self.x-1] in ['#','~']:
                 self.t = '~'
                 self.moving=False
        else:
            self.y += 1

def loadMap(filename):
    ## Build the initil map
    mymap = np.full((w,h), '.')
    mymap[0][500] = 'o'
    input = list(map( lambda x: x.strip(), open(input_file).readlines() ))
    for line in input:    
        (p1,p2) = line.split(',')
        p1 = int(p1.split('=')[1])
        p2 = p2.split('=')[1]
        (p2_1, p2_2) = map(int, p2.split('..'))

        if line[0] == 'x':
            for y in range(p2_1, p2_2+1):
                mymap[y][p1] = '#'
        elif line[0] == 'y':
            for x in range(p2_1, p2_2+1):
                mymap[p1][x] = '#'
    return mymap 

def drawMap(screen):
    mymap = loadMap("test_input.txt")
    view_width = 40
    view_height = 20
    view_x = 490
    view_y = 0
    drops = [ drop(500,0) ]

    while True:
        
        for d in drops:
            mymap[d.y][d.x] = d.t

        for xx in range(0, view_width):
            for yy in range(0, view_height):
                screen.print_at( mymap[view_y + yy][view_x + xx] , xx,yy)
        
        ev = screen.get_key()
        if ev in (ord('n'), ord('N')):
            screen.clear()
            r=0
            for d in drops:
                # update the position
                screen.print_at( "x:{} y:{}".format(d.x, d.y), 50,10+r)
                r+=1
                d.update(mymap)
            # add another drop
            drops.append(drop(500,0))
        if ev in (ord('q'), ord('Q')):
            quit()
    
        
        screen.refresh()


Screen.wrapper(drawMap)
