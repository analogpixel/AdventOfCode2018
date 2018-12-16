#!/usr/bin/env python


ar = [3,7]

e1 = 0
e2 = 1
after=170641
#after=9

while True:
    # create new
    ar = ar + list(map(int, list(str(ar[e1] + ar[e2]))))

    # move the elves
    e1 = (e1 + ar[e1] + 1) % len(ar)
    e2 = (e2 + ar[e2] + 1) % len(ar)

    #print(ar,e1,e2)
    if len(ar) > after + 10:
        print(  "".join(map(str, ar[after:after+10])))
        break