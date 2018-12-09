#!/usr/bin/env python

class task:
    def __init__(self,task_name, task_time=False, task_worker=False):
        self.time_add = 0
        self.task_name = task_name

        if task_time:
            self.task_time = task_time
        else:
            self.task_time =  (ord(task_name) - 64) + self.time_add

        self.task_worker = task_worker
        self.task_finished = False
        self.task_requires = []
    
    def tick(self):
        if not self.task_finished:
            if self.task_worker:
                self.decrement_time()

    def set_finished(self):
        self.task_finished = True
        self.task_worker = False
    
    # True: the task complted
    # False: the task is still running
    def decrement_time(self, amt=1):
        self.task_time -= amt 
        print(self.task_name + ": is working")

        if self.task_time <= 0:
            self.set_finished()
            print(self.task_name + ": is finished")

    def is_finished(self):
        return self.task_finished
        
    def add_dependency(self, task_name):
        self.task_requires.append(task_name)

    # false : not blocked
    # true  : blocked 
    def check_blocked(self, completed_tasks):
        if all(map(lambda x: x in completed_tasks , self.task_requires)):
            return False
        else:
            return True

    def __str__(self):
        return self.task_name + " requires: " + ",".join(self.task_requires) +  " current worker: " +  str(self.task_worker) + "\n"

class tasks:
    def __init__(self,file_name):
        self.file_name = file_name
        self.all_tasks = {}    
        self.loadFile()
        self.completed_tasks = []
        self.num_workers = 2
        self.working = 1
        self.timer = 0

    def next_unblocked_task(self):
        for task in self.all_tasks:
            if not self.all_tasks[task].check_blocked(self.completed_tasks):
                if self.all_tasks[task].task_worker == False:
                    return task
        
        # no tasks found at this time
        return False

    def tick(self):
        
        while self.working < self.num_workers:
            t = self.next_unblocked_task()

            if t:
                self.all_tasks[t].task_worker = self.working
                print(str(self.working) +  "to start working on ", str(t))
                self.working += 1
            else:
                # no work to do at this time
                break

        for t in self.all_tasks:
            # allow the task to work if needed
            self.all_tasks[t].tick()

            # update the task if it finished
            if self.all_tasks[t].task_finished and t not in self.completed_tasks:
                self.completed_tasks.append(t)
                self.working -= 1
                print("dec working:", self.working)

        # increment the timer
        self.timer += 1

        print("end of tick  working:", self.working)

        # if we are done return true
        if len(self.completed_tasks) == len(self.all_tasks):
            return True
        else:
            return False

    def loadFile(self):
        input = list(map( lambda x: x.strip(), open(self.file_name).readlines() ))
        for lines in input:
            (l1, l2) = (lines[5], lines[36])
        
            if not l2 in self.all_tasks:
                self.all_tasks[l2] = task(l2)
            self.all_tasks[l2].add_dependency(l1)

            if not l1 in self.all_tasks:
                self.all_tasks[l1] = task(l1)

    def __str__(self):
        out = ""
        for n in self.all_tasks:
            out += str(self.all_tasks[n])
        return out

elf_tasks = tasks("test_input.txt")

while True: 
    if  elf_tasks.tick():
        break
print(elf_tasks.timer)
    


