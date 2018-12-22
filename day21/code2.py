#!/usr/bin/env python

import copy

# opCode
# 0 : opcode
# 1 : a (input register)
# 2 : b (input register)
# 3 : c (output register)

def addr(opCode, reg):
    reg[ opCode[3] ] = reg[ opCode[1] ] + reg[ opCode[2] ]
    return reg

def addi(opCode, reg):
    reg[ opCode[3] ] = reg[ opCode[1] ] + opCode[2]
    return reg

def mulr(opCode, reg):
    reg[ opCode[3] ] = reg[ opCode[1] ] * reg[ opCode[2] ]
    return reg

def muli(opCode, reg):
    reg[ opCode[3] ] = reg[ opCode[1] ] * opCode[2]
    return reg

def banr(opCode, reg):
    reg[ opCode[3] ] = reg[ opCode[1] ] & reg[ opCode[2] ]
    return reg

def bani(opCode, reg):
    reg[ opCode[3] ] = reg[ opCode[1] ] & opCode[2]
    return reg

def borr(opCode, reg):
    reg[ opCode[3] ] = reg[ opCode[1] ] | reg[ opCode[2] ]
    return reg

def bori(opCode, reg):
    reg[ opCode[3] ] = reg[ opCode[1] ] | opCode[2]
    return reg

def setr(opCode, reg):
    reg[ opCode[3] ] = reg[ opCode[1] ] 
    return reg

def seti(opCode, reg):
    reg[ opCode[3] ] = opCode[1]
    return reg

def gtir(opCode, reg):
    reg[ opCode[3] ] = 1 if opCode[1] > reg[ opCode[2]] else 0
    return reg

def gtri(opCode, reg):
    reg[ opCode[3] ] = 1 if reg[opCode[1]] > opCode[2] else 0
    return reg

def gtrr(opCode, reg):
    reg[ opCode[3] ] = 1 if reg[opCode[1]] > reg[opCode[2]] else 0
    return reg

def eqir(opCode, reg):
    reg[ opCode[3] ] = 1 if opCode[1] == reg[ opCode[2]] else 0
    return reg

def eqri(opCode, reg):
    reg[ opCode[3] ] = 1 if reg[opCode[1]] == opCode[2] else 0
    return reg

def eqrr(opCode, reg):
    reg[ opCode[3] ] = 1 if reg[opCode[1]] == reg[opCode[2]] else 0
    return reg

input_file = "input.txt"
input = list(map( lambda x: x.strip().split(' '), open(input_file).readlines() ))

op_reg = int(input[0][1])
prgm = input[1:]
reg = [0,0,0,0,0,0]
ip = 0
i = 0
brk_count = 0

p_len = len(prgm)

maxx=0
reg = [3345459,0,0,0,0,0]
reg = [0,0,0,0,0,0]
ll = []
brk_count = 0
high = 0
for i in [168540, 196081, 634966, 813317, 966072, 1348289, 1527039, 1565243, 1726936, 1831490, 1897936, 1970389, 2281636, 2384551, 2476639, 2544080, 2578583, 2650867, 2727446, 2846570, 2872613, 2905464, 2970169, 2978655, 3000304, 3345459, 3391011, 3403863, 3408950, 3436646, 3516629, 3556991, 3767882, 4219160, 4288766, 4401665, 4488407, 4751285, 4767157, 4865163, 5108921, 5182610, 5450974, 5589796, 5677984, 6159135, 6224541, 6246944, 6252007, 6256876, 6387648, 6634383, 6900305, 7064809, 7637529, 7874210, 8072286, 8214606, 8342318, 8345870, 8391018, 8833538, 9096469, 9355454, 9406515, 9414288, 9612420, 9838440, 9901943, 9906182, 10206092, 10345275, 10622610, 10677778, 10703597, 10827860, 10863672, 10911374, 10975167, 11208142, 11589747, 12125387, 12226466, 12601902, 12620121, 12654292, 12695950, 13054525, 13055150, 13329325, 13490773, 13601367, 13638723, 14153270, 14176241, 14244182, 14295546, 14463836, 14485567, 14517421, 14902408, 14916993, 15026246, 15345944, 15382646, 15406989, 15447812, 15763639, 15788055, 16029669, 16568932, 16662551, 16733608, 16775101]:
    num_inst = 0
    ip = 0
    reg = [i,0,0,0,0,0]
    while ip < p_len:
        (fun, a,b,c) = prgm[ip]
        globals()[fun]([0,int(a),int(b),int(c)], reg)
        ip = reg[op_reg]
        ip +=1 
        reg[op_reg] = ip
        num_inst +=1

    print(i, "{:,}".format(num_inst))
    if num_inst > high:
        print("New High:", i, num_inst)
        high = num_inst
print(ip, reg  )
