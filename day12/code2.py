#!/usr/bin/env python

## This code will get there eventually maybe? it's at least faster than code.py
# but the trick is to figure out that at some point the pattern starts
# repeating over and over
# So i took a point in time (itteration 161) and then subtracted 50 billion 
# and then 1 since I started at 0, and then multiplied
# it by the ammount it increases each step (12203 is where the total was at step 161)
#
# 12203 + (50000000000-161-1) * 73

input_file = "input.txt"

input = list(map( lambda x: x.strip(), open(input_file).readlines() ))

pos_side =  list(map(lambda x: 0 if x =='.' else 1, list(input[0])) ) + [0,0]

data = {-2:0, -1:0}
for i in range(0, len(pos_side)):   
    data[i] = pos_side[i]

#print(data)
max_size=len(pos_side)
min_size=-2

grow_checks   = []
nogrow_checks = []
for check in input[2:]:
    (check_d, c_type) = map(lambda x: x.strip(), check.split("=>"))
    check_d = list(map(lambda x: 0 if x =='.' else 1, list(check_d)) )
    
    x = 0b00000000
    for z in check_d:
        x  = x << 1
        x = x ^ z
       
    if c_type == '.':
        nogrow_checks.append(x)
    else:
        grow_checks.append(x)

#print(grow_checks)
#print(nogrow_checks)


last_score=0
for zz in range(0,50000000000):
    new_data = {}
    for i in range(min_size, max_size+2):
        if not i-2 in data:
            data[i-2] = 0
        if not i-1 in data:
            data[i-1] = 0
        if not i+1 in data:
            data[i+1] = 0
        if not i+2 in data:
            data[i+2] = 0

        x = 0b00000000
        for z in [data[i-2], data[i-1], data[i], data[i+1], data[i+2]]:
            x = x << 1
            x = x ^ z
            
        if x in grow_checks:
            new_data[i] = 1
            if i < min_size:
                min_size = i
            if i > max_size:
                max_size = i
        else:
            new_data[i] = 0
        
    data = new_data

    #if zz % 10000 == 0:
    #   print(50000000000 - zz)
    total = 0
    for x in data.keys():
        if data[x] == 1:
            total += x
    print(total)

    print(zz,total, last_score, total - last_score)
    last_score= total

total = 0
for x in data.keys():
    if data[x] == 1:
        total += x
print(total)
