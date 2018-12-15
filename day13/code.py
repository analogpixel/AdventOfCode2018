#!/usr/bin/env python

import pprint
from asciimatics.screen import Screen
import time
import pdb


input_file = "input.txt"

# v : facing down
# ^ : facing up
# > : move right
# < : move left

class cart:
    def __init__(self, x,y,d, id=None):
        self.x = x
        self.y = y
        self.d = d
        self.id = id
        self.crossCount = 0

    def move(self, map):

        if map[self.y][self.x] == '/' and self.d == '>':
            self.d = '^'
        elif map[self.y][self.x] == '/' and self.d == '^':
            self.d = '>'
        elif map[self.y][self.x] == '/' and self.d == '<':
            self.d = 'v'
        elif map[self.y][self.x] == '/' and self.d == 'v':
            self.d = '<'
        elif map[self.y][self.x] == '\\' and self.d == '>':
            self.d = 'v'
        elif map[self.y][self.x] == '\\' and self.d == '<':
            self.d = '^'
        elif map[self.y][self.x] == '\\' and self.d == '^':
            self.d = '<'
        elif map[self.y][self.x] == '\\' and self.d == 'v':
            self.d = '>'
        elif map[self.y][self.x] == '+' and self.crossCount == 0:
            # turn left
            if self.d == 'v':
                self.d = '>'
            elif self.d == '^':
                self.d = '<'
            elif self.d == '<':
                self.d = 'v'
            elif self.d == '>':
                self.d = '^'
            self.crossCount +=1
        elif map[self.y][self.x] == '+' and self.crossCount == 1:
            self.d = self.d # just keep moving in the same direction
            self.crossCount += 1
        elif map[self.y][self.x] == '+' and self.crossCount == 2:
            # turn right
            if self.d == 'v':
                self.d = '<'
            elif self.d == '^':
                self.d = '>'
            elif self.d == '<':
                self.d = '^'
            elif self.d == '>':
                self.d = 'v'
            self.crossCount = 0
        
        if self.d == '<':
            self.x -= 1
        elif self.d == '>':
            self.x += 1
        elif self.d == '^':
            self.y -=1
        elif self.d == 'v':
            self.y +=1
        else:
            pass
            #print("no valid move:", self.d)

    def __str__(self):
        return "x:{} y:{} d:{} id:{}".format(self.x, self.y, self.d, self.id)

    def loc(self):
        return (self.x, self.y)

def demo(screen):
    
    
    #
    ## load in the data
    #
    cart_map = []
    carts = []
    line = []
    x=0
    y=0
    i=0
    with open(input_file) as f:
        while True:
            c = f.read(1)
            if not c:
                #print("End of file")
                break
            else:
                
                if c == "\n":
                    cart_map.append(line)
                    line = []
                    y+=1
                    x=0
                elif c in ['<','>','^','v']:
                    carts.append( cart(x,y,c,i) )
                    #print("adding cart {} at {},{}".format(c,x,y))
                    
                    if c in ['<','>']:
                        line.append('-')
                    if c in ['^','v']:
                        line.append('|')
                    i+=1
                    x+=1
                else:
                    line.append(c)
                    x+=1

    crashing = False
    while not crashing:

        
        
        # move all the carts around
        for c in carts:
            c.move(cart_map)

        # check to see if anyone crashed    
        tmp = list(map(lambda x: x.loc(), carts) )
        if not len(set(tmp)) == len(tmp):
            print("crashed at:", tmp)
            time.sleep(12)
            quit()
            crashing == True
        
        screen.clear()
        # draw the map
        for x in range(0, len(cart_map[0])):
            for y in range(0, len(cart_map)):
                screen.print_at(cart_map[y][x], x, y)
        
        # draw the carts
        ii = 0
        for c in carts:
            (x1,y1) = c.loc()
            screen.print_at("{} x:{} y:{} d:{}".format(c.id, x1,y1, c.d), 0, 10+ii)
            screen.print_at('#',x1,y1)
            ii +=1 


        screen.refresh()    

        ev = screen.get_key()
        if ev in (ord('Q'), ord('q')):
            return
        time.sleep(.1   )



Screen.wrapper(demo)
