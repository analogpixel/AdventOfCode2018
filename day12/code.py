#!/usr/bin/env python

input_file = "input.txt"

input = list(map( lambda x: x.strip(), open(input_file).readlines() ))

padding=200

#plants = ['.','.'] + list(input[0]) + ['.','.']
plants = ['.'] * padding + list(input[0]) + ['.'] * padding

for i in input[2:]:
    print(i)

for ittr  in range(0,20):
   
    new_plants = ['.'] * len(plants)
    for i in range(2,len(plants)-2):
        thisPlant='.'
        for check in input[2:]:
            (check_data, check_type) = map(lambda x: x.strip(), check.split('=>'))  
            if "".join(plants[i-2:i+3]) == check_data:
                thisPlant=check_type
                break
        
        new_plants[i] = thisPlant

    plants = new_plants
    #if ittr % 1000 == 0:
    #    print(ittr)

#for i in range(0, len(out)):
#    print(i, "".join(out[i][2:-2]))

total =0
for i in range(0, len(plants)):
    if plants[i] == '#':
        total += (i-padding)

print(total)