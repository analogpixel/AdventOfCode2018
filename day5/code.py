#!/usr/bin/env python

import string
import re

import llist

input = list(map( lambda x: x.strip(), open("input.txt").readlines() ))[0]

myList = llist.dllist(input)

i =0
while True:
    if (i< myList.size -1) and (abs(ord(str(myList[i])) - ord(str(myList[i+1] ))) == 32):
        myList.remove(myList.nodeat(i))
        myList.remove(myList.nodeat(i))
        i = i - 2
        if i < 0:
            i = 0
        continue
    
    i +=1
    
    if i > myList.size:
        break
    
#print(myList)
print(myList.size)
# dabAcCaCBAcCcaDA

