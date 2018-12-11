#!/usr/bin/env python

import llist

elfs = 462
last_marble = 71938 * 100

#elfs=9
#last_marble=25

current_num = 1
ring = llist.dllist([0])
elf_scores = {}

for i in range(0, elfs):
    elf_scores[i] = 0

while current_num < last_marble:
    for i in range(0,elfs):
        
        """
        current_node = ring[0]
        x = 0
        while True:
            ring.rotate(1)
            x +=1
            if ring[0] == 0:
                break
        print("elf ", i, " stack", ring, " current node:", current_node) 
        ring.rotate(-1 * x)
        """

        if (current_num % 23) == 0 and current_num != 0:
            elf_scores[i] += current_num
            ring.rotate(7)
            elf_scores[i] += ring.popleft()     
        else:
            ring.rotate(-2)
            ring.appendleft(current_num)

        current_num+=1

        if current_num == last_marble:
            break
        
        
        #if current_num % 10000 == 0:
        #   print("{:,}".format(current_num) , " of ", "{:,}".format(last_marble))

print(max(elf_scores.values()))
