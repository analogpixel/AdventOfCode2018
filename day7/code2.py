#!/usr/bin/env python

import texttable

num_workers  = 5
time_add = 60
tasks    = {}  # tasks and dependencies
workers  = ["."] * num_workers # which worker is working on which task
timers   = {} # how much longer each task has
finished = [] # if a task is finished
seconds  = 0
table    = texttable.Texttable()
done     = ""
input_file = "input.txt"

input = list(map( lambda x: x.strip(), open(input_file).readlines() ))
for lines in input:
    (l1, l2) = (lines[5], lines[36])
    if l2 in tasks:
        tasks[l2].append(l1)
    else:
        tasks[l2] = [l1]

    if not l1 in tasks:
        tasks[l1] = []

    timers[l2] = (ord(l2) - 64) + time_add
    timers[l1] = (ord(l1) - 64) + time_add

t = list(map(lambda x: "worker " + str(x+1), range(0, len(workers) ) ))
table.add_row( ["Second"] + t  + ["Done"] )


while len(finished) < len(tasks):

    # assign works to tasks
    for k in sorted(tasks):
        # if task is finished then move on to the next task
        if k in finished or k in workers:
            continue

        # can we kick off a new worker?
        elif all(map(lambda x: x in finished , tasks[k])):
            # if we have a worker, assign a task to it
            if '.' in workers:
                workers[ workers.index('.') ] = k    

    newRow = [seconds] + workers + [done] 
    table.add_row( newRow)
    
    # let workers work on tasks
    for k in workers:
        # if this isn't an idle worker update the work
        if k != '.':
            timers[k] -= 1
            if timers[k] == 0:
                finished.append(k) # move the task to finished
                workers[workers.index(k)] = "." # update the worker to be free
                done = done + k  # update done
                i = 0 # reset the counter and start again
                continue

    
    seconds +=1

newRow = [seconds] + workers + [done] 
table.add_row( newRow)

print( table.draw() )


