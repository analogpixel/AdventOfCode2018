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

op_code = { 5: banr,
            1: bani,
            8: setr,
            12: gtir,
            10: eqrr,
            4: eqir,
            14: gtri,
            13: gtrr,
            0: eqri,
            2: seti,
            15: mulr,
            9: addr,
            6: borr,
            3: bori,
            11: addi,
            7: muli}

def test(before, after, opcodes):
    allCommands = [addr,addi,mulr,muli,banr,bani,borr,bori,setr,seti,gtir,gtri,gtrr,eqir,eqri,eqrr]
    count = 0
    print("-----")
    for c in allCommands:
        reg = copy.deepcopy(before)
        t = c(opcodes, reg)
        if t == after:
            count+=1
            print(opcodes[0], t,c)
    print("-----")
    return count >= 3

input_file = "input.txt"
input = list(map( lambda x: x.strip(), open(input_file).readlines() ))
counter=0
for i in range(0, len(input), 4):
    before = eval(input[i].split(':')[1].strip())
    opcodes = list(map(int, input[i+1].split(' ')))
    after = eval(input[i+2].split(':')[1].strip())
    #print(before, opcodes, after)
    if test(before, after, opcodes):
        counter +=1

print("count:", counter)    