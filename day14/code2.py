#!/usr/bin/env python

# the string approach (instead of list) is 27seconds faster than the list approach (on my sample input)

# run with profiling: python -m cProfile code2.py

ar = "37"
ar_size=2

e1 = 0
e2 = 1
after='170641'
#after='59414' # 2018
after_size = len(after)
count = 0

## instead of doing string->int and int->string conversions, I just do hash lookups which seem to go much faster
dd = {'0': 0, 
      '1': 1,
      '2': 2,
      '3': 3,
      '4': 4,
      '5': 5,
      '6': 6,
      '7': 7,
      '8': 8,
      '9': 9,
      '0': 0
       }
ee = {}
for i in range(0,20):
    ee[i] = str(i)

while True:
    # create new
    t = ee[ dd[ar[e1]] + dd[ar[e2]]  ]
    #t = str(int(ar[e1]) + int(ar[e2]))
    ar_size += len(t)
    ar = ar + t
    #ar = ''.join([ar,t])
    count +=1

    # move the elves
    e1 = (e1 + int(ar[e1]) + 1) % ar_size
    e2 = (e2 + int(ar[e2]) + 1) % ar_size

    if ar_size > after_size:
        #tmp = ar.find(after[-(after_size+3):]) ## oops, pretty bad bug, will find correct answeres, but traverses the entire string each time.
        # this line takes something that'll run forever down to something that runs in 31 seconds.
        tmp = ar[-(after_size+3):].find(after)
        if tmp != -1:
            tmp = ar.find(after)
        #if ar_size > after_size and ar[-after_size:].find(after) != -1:
            print( len(ar[0:tmp]))
            break

    