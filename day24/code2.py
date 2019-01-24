#!/usr/bin/env python

import re
from recordclass import recordclass
from pprint import pprint 
import math
import copy
import sys

MyStruct = recordclass('system', 'id systemType weakTo immuneTo units hitPoints attack attackType init effectivePower selected defendingGroup')

#inputFile = "test_input.txt"
inputFile = "input.txt"


def damage(a,b):
    if a.attackType in b.weakTo:
        mult = 2
    else:
        mult = 1

    if a.attackType in b.immuneTo:
        mult = 0
    
    #print("{} {} {}".format(a.id, b.id, a.effectivePower * mult) )
    return a.effectivePower * mult 

if len(sys.argv) > 1:
    boost = int(sys.argv[1])
else:
    boost = 0
    

# read in input file
data=[]
currentType = False
id_counter = {'immune': 1, 'infection': 1}
for line in map(lambda x: x.strip(), open(inputFile)):
  if line == 'Immune System:':
    currentType = 'immune'
  elif line == 'Infection:':
    currentType = 'infection'
  else:
    m = re.match(r'(.*) units each with (.*) hit points *(\(.*\))* with an attack that does (.*) (.*) damage at initiative (.*)$', line)
    if m:
      weakTo = []
      immuneTo=[]
      
      stats = m.group(3)
      if stats:
          for s in map(lambda x: x.strip(), stats[1:-1].split(';')):
              if s[0] == 'w':
                  weakTo =list(map(lambda x: x.strip(), s[7:].split(',')))
              if s[0] == 'i':
                  immuneTo  = list(map(lambda x: x.strip(), s[9:].split(',')))
      
      s = MyStruct(systemType=currentType, units=int(m.group(1)),
                   hitPoints=int(m.group(2)), attack=int(m.group(4)),
                   attackType=m.group(5), init=int(m.group(6)),
                   effectivePower=0, weakTo=weakTo, immuneTo=immuneTo,
                   selected=False, id=0, defendingGroup=-1)
 
      if s.systemType == 'immune':
          s.attack += boost

      s.effectivePower = s.units * s.attack 
      s.id = id_counter[currentType]
      id_counter[currentType] +=1
      data.append(s)

data = sorted(data, key=lambda x: (x.effectivePower, x.init), reverse=True)
#pprint(data)
#pprint( damage(data[1], data[2] ))

def check_done(d):
    z = []
    for a in d:
       z.append(a.systemType)
    return len(set(z)) == 2

while check_done(data):
    print("----")
    for d in data:
        d.selected = False
        
    # Selection Phase
    # priority of selection starts with effective power, and if there is a tie,
    # then the initiative is used
    for player in sorted(data, key=lambda x: (x.effectivePower, x.init), reverse=True):
        enemy = list(filter( lambda x: x.systemType!=player.systemType and x.selected == False, data))
        selected = list(sorted(enemy, key=lambda y: (damage(player,y),y.effectivePower,y.init), reverse=True))
        if len(selected) > 0 and damage(player,selected[0]) > 0:
            selected = selected[0]
        else:
            continue
        selected.selected = True
        player.defendingGroup = selected.id
        #print("type: {} id {} will deal {} damage to type:{} id:{}".format(player.systemType, player.id, damage(player, selected), selected.systemType, selected.id))
        #print("---")

    # Attack Phase
    totalDamage = 0
    for player in sorted(data, key=lambda x: x.init, reverse=True):
        if player.defendingGroup == -1:
            continue
        enemy = list(filter(lambda x: x.systemType != player.systemType and x.id == player.defendingGroup, data))[0]
        d = damage( player, enemy)
        units = math.floor( d / enemy.hitPoints  )
        if units > enemy.units:
            units = enemy.units 
        totalDamage += units
        print("{} group {} attacks defending group {}, killing {} units".format(player.systemType, player.id, player.defendingGroup, units))
        enemy.units -= units 
        enemy.effectivePower = enemy.units * enemy.attack

    if totalDamage == 0:
        print("Stalemate")
        pprint(data)
        quit()

    # remove all dead units
    newData = []
    for d in data:
        if d.units > 0: 
            d.selected = False
            d.effectivePower = d.units * d.attack
            d.defendingGroup = -1
            newData.append(d)
    data = copy.deepcopy(newData)
    #pprint(data)

pprint(data)
winner = list(set([x.systemType for x in data]))[0]
print ( winner, sum([d.units for d in data] ) )
