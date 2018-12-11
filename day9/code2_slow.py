#!/usr/bin/env python

import llist

elfs = 462
last_marble = 71938 * 100

elfs=9
last_marble=25

current_marble = 0
current_num = 1
#ring = [0]
ring = llist.dllist([0])
elf_scores = {}


while current_num < last_marble:
    for i in range(0,elfs):
        
        print("elf ", i, " stack", ring, " current node:", ring[current_marble])

        if (current_num % 23) == 0 and current_num != 0:
            if i in elf_scores:
                elf_scores[i] += current_num
            else:
                elf_scores[i] = current_num

            seven_counterclock = (current_marble - 7) % ring.size
            
            #t = ring[seven_counterclock]
            elf_scores[i] += ring[seven_counterclock]

            ring.remove( ring.nodeat(seven_counterclock) )
            
            current_marble = seven_counterclock
            current_num +=1
            
            continue

        two_clockwise = (current_marble + 2) % ring.size
        if two_clockwise == 0:
            ring.append(current_num)
            current_marble=ring.size -1
        else:
            ring.insert(current_num, ring.nodeat(two_clockwise))
            current_marble = two_clockwise
        current_num+=1

        

        if current_num == last_marble:
            break

        

        if current_num % 10000 == 0:
           print("{:,}".format(current_num) , " of ", "{:,}".format(last_marble))
        #print(current_num-1, ring)

print(max(elf_scores.values())) 
