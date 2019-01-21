#!/usr/bin/env python

import re
import numpy as np 
input_file = "input.txt"

input = list(map( lambda x: x.strip(), open(input_file).readlines() ))


bot_map = {}

for i in range(0, len(input)):
    m = re.match( r'pos=<(.*)>, r=(.*)' , input[i])
    size = int(m.group(2)) // 1000000
    pos = list(map(lambda x: int(x)//1000000, m.group(1).split(',')))

    for x in range(-size, size+1):
        for y in range(-size, size+1):
            for z in range(-size, size+1):
                key = str(x) + "," + str(y) + "," + str(z)
                if key in bot_map:
                    bot_map[key] += 1
                else:
                    bot_map[key] = 1


mm = 0
kk= []
for k in bot_map:
    if bot_map[k] == mm:
        kk.append(k)
    elif bot_map[k] > mm:
        kk = [k]
        mm = bot_map[k]

# pos=<32066369,-29553295,30877308>, r=91230974

print(kk)
#print("max:{} key:{}".format(mm,kk))