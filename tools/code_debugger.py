#!/usr/bin/env python

import copy
import sys
from asciimatics.screen import Screen

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

def debug(screen, input_file=sys.argv[1]):
    input = list(map( lambda x: x.strip().split(' '), open(input_file).readlines() ))

    op_reg = int(input[0][1])
    prgm = input[1:]
    reg = [0,0,0,0,0,0]
    if len(sys.argv) > 1:
        reg = list(map(int, sys.argv[2].split(',')))
    ip = 0
    i = 0
    
    while True:
        # print out the program
        for i in range(0, len(prgm)):
            (fun, a,b,c) = prgm[i]
            if i == ip:
                bgcolor = Screen.COLOUR_RED
            else:
                bgcolor = Screen.COLOUR_BLACK
            screen.print_at("{}: {} {} {} {}".format(i, fun,a,b,c),2, 2+i, bg=bgcolor)

        # print out the registers
        zt = 0
        for i in range(0, len(reg)):
            if i == op_reg:
                bgcolor = Screen.COLOUR_RED
            else:
                bgcolor = Screen.COLOUR_BLUE
            
            z = len(str(reg[i]))
            screen.print_at("R{}".format(i),  zt+20, 2, bg=bgcolor)
            screen.print_at("{}".format(reg[i]),  zt+20, 3, bg=bgcolor)
            zt += z + 2

        (fun, a,b,c) = prgm[ip]
        screen.print_at("fun:{} a:{} b:{} c:{}".format(fun,a,b,c), 60,2)
            
        screen.refresh()

        ev = screen.get_key()
        if ev in (ord('N'), ord('n'), ord('m')):
            screen.clear()
            if ev == ord('m'):
                c = 10000
            elif ev == ord('N'):
                c = 100
            else:
                c = 1
            for i in range(0, c):
                reg[op_reg] = ip
                (fun, a,b,c) = prgm[ip]
                screen.print_at("fun:{} a:{} b:{} c:{}".format(fun,a,b,c), 60,2)
                globals()[fun]([0,int(a),int(b),int(c)], reg)
                ip = reg[op_reg]
                ip +=1 
                reg[op_reg] = ip
            
        elif ev in (ord('Q'), ord('q')):
            return
                

Screen.wrapper(debug)
