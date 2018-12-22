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

num_inst = 0

lc = 0
try:
    while ip < p_len:
        (fun, a,b,c) = prgm[ip]
        globals()[fun]([0,int(a),int(b),int(c)], reg)
        ip = reg[op_reg]
        ip +=1 
        reg[op_reg] = ip
        num_inst +=1

        """
        28 [3345460, 3345459, 28, 1, 1, 1]
        28 [3345460, 8214606, 28, 1, 51, 1]
        28 [3345460, 15026246, 28, 1, 77, 1]
        28 [3345460, 16029669, 28, 1, 35, 1]
        28 [3345460, 16568932, 28, 1, 29, 1]
        28 [3345460, 16733608, 28, 1, 171, 1]
        28 [3345460, 16775101, 28, 1, 163, 1]
        28 [3345460, 16775284, 28, 1, 77, 1]
        28 [3345460, 16777194, 28, 1, 179, 1]
        """
        
        # find the values every time we get to instruction 28, 
        # registrer 1 tells us what we need to set r0 to cause the program to exit
        if ip == 28:
            print("ip:{} num_inst:{} regs:{}".format( ip, num_inst, str(reg)  ))
            
            if reg[1] in ll:
                print("Loop detected")
                break
            else:
                ll.append(reg[1])

            num_inst = 0
            #if reg[1] > maxx: 
            #    print(ip, num_inst, reg  )
            #    maxx = reg[1]
            #num_inst = 0
except KeyboardInterrupt:
    #print(sorted(set(ll)))
    pass

print(i, num_inst)
print(ip, reg  )
