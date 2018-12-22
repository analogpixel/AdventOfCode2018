#!/usr/bin/env python

#input_file = "test_input.txt"
#input = list(map( lambda x: x.strip(), open(input_file).readlines() ))


input_1 = "^WNE$"
input_2 = list("^ENWWW(NEEE|SSE(EE|N))$")

input_3 = list("(^ENNWSWW(NEWS|)SSSEEN(WNSE|)EE(SWEN|)NNN$)")

def walk(path,x,y):
    scores = []
    score = 0
    while(True):
        c = path.pop(0)
        if c in ['E','N','S','W']:
            score +=1 
            
            if c == 'E':
                x = x + 1
            if c == 'W':
                x = x - 1
            if c == 'S':
                y = y + 1
            if c == 'N':
                y = y - 1
            
            print("x:{} y:{} score:{} dist:{}".format( x,y, score, abs(x) + abs(y) ) )
            
        elif c == '(':
            score = score + walk(path,x,y)
        elif c == '|':
            scores.append(score)
            score = 0
        elif c in  [')','$']:
            scores.append(score)
            return max(scores)

print( walk(input_3,0,0) )