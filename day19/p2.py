#!/usr/bin/env python

# all this program is doing, is finding every number divisible by whatever is
# in R1 and adding them together.
t = 0 
num = 10551292
for i in range(1,num+1):
    if num % i == 0:
        print(i)
        t += i

print(t)
