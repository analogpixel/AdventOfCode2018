0 goto 17 # addi 2 16 2
1 r5 = 1 # seti 1 8 5
2 r3 = 1 # seti 1 0 3
3 r4 = r5 * r3 # mulr 5 3 4
4 r4 = 1 if r4 == r1 else 0 # eqrr 4 1 4
5 goto (r4 + r2 +1 ) # addr 4 2 2
6 goto 8 # addi 2 1 2
7 r0 = r5 + r0 # addr 5 0 0
8 r3 = r3 + 1 # addi 3 1 3
9 r4 = goto 12 if r3 > r1 goto 2 # gtrr 3 1 4
10 . # addr 2 4 2
11 . # seti 2 1 2
12 r5 = r5 + 1 # addi 5 1 5
13 if r5 > r1 goto 16 else goto 1
14 . #addr 4 2 2
15 .  # seti 1 1 2
16 r2 = r2 * r2 # mulr 2 2 2 (exit?)
17 r1 = r1 + 2 #addi 1 2 1
18 r1 = r1 * r1 # mulr 1 1 1
19 r1 = r2 * r1 #mulr 2 1 1
20 r1 = r1 * 11 # muli 1 11 1
21 r4 = r4 + 2 #addi 4 2 4
22 r4 = r4 * 2 # mulr 4 2 4
23 r4 = r4 + 12 # addi 4 12 4
24 r1 = r1 + r4 #addr 1 4 1
25 r2 = r2 + r0 #addr 2 0 2
26 goto 1
