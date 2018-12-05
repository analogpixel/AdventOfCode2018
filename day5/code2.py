#!/usr/bin/env python

import string
import re

import llist

input = open("input.txt").readlines()[0].strip()


myList = llist.dllist(list(input))

minList = myList.size
minListItem = False
i=0
for a in string.ascii_lowercase:
    i = 0
    myList = llist.dllist( list( re.sub(a.upper(), '', re.sub(a, '', input))))
    while True:
        if (i< myList.size -1) and (abs(ord(str(myList[i])) - ord(str(myList[i+1] ))) == 32):
            myList.remove(myList.nodeat(i))
            myList.remove(myList.nodeat(i))
            i = i - 1
            if i < 0:
                i = 0
            continue
        
        i +=1

        if i > myList.size:
            break

    #print(a, myList.size )
    if myList.size < minList:
        minList = myList.size
        minListItem = a

    
#print(myList)
print( minList, minListItem)
# dabAcCaCBAcCcaDA

