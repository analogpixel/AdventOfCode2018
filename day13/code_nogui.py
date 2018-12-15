#!/usr/bin/env python

import pprint
import time

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
        print ( set([x for x in tmp if tmp.count(x) > 1]) )
        crashing = True
    
