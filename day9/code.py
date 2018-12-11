#!/usr/bin/env python


elfs = 462
current_marble = 0
current_num = 1
ring = [0]
elf_scores = {}
last_marble = 71938 * 100

while current_num < last_marble:
    for i in range(0,elfs):
        
        if (current_num % 23) == 0 and current_num != 0:
            if i in elf_scores:
                elf_scores[i] += current_num
            else:
                elf_scores[i] = current_num

            seven_counterclock = (current_marble - 7) % (len(ring))
            
            t = ring[seven_counterclock]
            elf_scores[i] += ring[seven_counterclock]
            i = ring.index(t)
            ring.remove(t)
            current_marble = i
            current_num +=1
            continue

        two_clockwise = (current_marble + 2) % (len(ring))
        if two_clockwise == 0:
            ring.append(current_num)
            current_marble=len(ring)-1
        else:
            ring.insert(two_clockwise, current_num)
            current_marble = ring.index(current_num)
        current_num+=1

        if current_num == last_marble:
            break

        #print(current_num-1, ring)

print(max(elf_scores.values())) 