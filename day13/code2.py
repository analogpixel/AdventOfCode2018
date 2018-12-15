#!/usr/bin/env python

import pprint
import time

#input_file = "test_input2.txt"
input_file = "input.txt"


class cart:
    def __init__(self, x,y,d, id=None):
        self.x = x
        self.y = y
        self.d = d
        self.id = id
        self.crossCount = 0
        self.dead = False
        self.turn = False # have i moved this turn?

    def move(self, map):
        if self.dead:
            return

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
        
        self.turn = True

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

while True:
    # reset all the carts to move
    for ww in carts:
        ww.turn = False
    for y in range(0, len(cart_map)):
        for x in range(0, len(cart_map[0])):
            for c in carts:
                if c.dead or c.turn == True:
                    continue
                if (c.loc() == (x,y)):
                    c.move(cart_map)
                    for d in carts:
                        if (not d.dead) and (d.loc() == c.loc()) and (not d.id == c.id):
                            d.dead = True
                            c.dead = True
                            print("{} crashed into {} at {},{}".format(c.id, d.id, d.loc()[0], d.loc()[1]) )

                            q = list(map(lambda i: i.loc(), filter(lambda o: o.dead==False, carts)  ))
                            if len(q) == 1:
                                print("at time of crash:", q)
                                break

            
    q = list(map(lambda i: i.loc(), filter(lambda o: o.dead==False, carts)  ))
    if len(q) == 1:
        print(q)
        break


for c in carts:
        if not c.dead:
            print("{} {}".format(c.id, c.dead))

#q = list(map(lambda i: i.loc(), filter(lambda o: o.dead==False, carts)  ))
#print(q)
    
