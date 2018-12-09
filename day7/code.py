#!/usr/bin/env python


workers = {}

input = list(map( lambda x: x.strip(), open("test_input.txt").readlines() ))
for lines in input:
    (l1, l2) = (lines[5], lines[36])
    if l2 in workers:
        workers[l2].append(l1)
    else:
        workers[l2] = [l1]

    if not l1 in workers:
        workers[l1] = []

finished = []
out=""

while len(finished) < len(workers):

    for k in sorted(workers):
        
        if k in finished:
            continue

        waiting = workers[k]
        if len(waiting) == 0 and not k in finished:
            finished.append(k)
            print(k, " is now unblocked")
            out += k
            break

        # are we still waiting on someone?
        if all(map(lambda x: x in finished , waiting)):
            finished.append(k)
            print(k, " is now unblocked.")
            out += k
            break
    

print(out)

