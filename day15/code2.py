#!/usr/bin/env python

from recordclass import recordclass
from pprint import pprint
from dijkstar import Graph, find_path

MyStruct = recordclass('system', 'type x y attack hp alive reading')
game_map = {}
players = []
x=0
y=0
width=0
height=0
boost={'E': 15, 'G': 3}

input_file = 'input.txt'

def attack(game_map, width, height, player, players):
    # is anyone in range if so don't move
    inRange = []
    for d in [ (0,-1), (-1,0), (1,0), (0,1) ]:
      key = "{}_{}".format(player.x+d[0], player.y+d[1]) 
      if key in game_map and game_map[key] not in ['.', '#', player.type ]:
          enemy = list(filter( lambda x: x.x == player.x+d[0] and x.y == player.y+d[1], players))[0]
          # 0, hp, x,y, reading order, []
          inRange.append(  [0, enemy.hp, enemy.x, enemy.y, enemy.x + (enemy.y * width), [] ])

    if len(inRange) >0:
      return sorted( inRange, key=lambda x: (x[1], x[4]))[0]
    else:
      return None

def find_closest(game_map, width, height, player, players):

    # is anyone in range if so don't move
    inRange = []
    for d in [ (0,-1), (-1,0), (1,0), (0,1) ]:
      key = "{}_{}".format(player.x+d[0], player.y+d[1]) 
      if key in game_map and game_map[key] not in ['.', '#', player.type ]:
          enemy = list(filter( lambda x: x.x == player.x+d[0] and x.y == player.y+d[1], players))[0]
          return [0, enemy.x, enemy.y, []]

    # build a map
    graph = Graph()
    for x in range(0, width):
        for y in range(0, height):
            for d in [ (0,-1), (-1,0), (1,0), (0,1) ]:
                key = "{}_{}".format(x+d[0], y+d[1]) 
                if key in game_map and game_map[key] == '.':
                    graph.add_edge("{}_{}".format(x,y), key, 1)

    path_data = []
    for p in players:
        # don't attack your friends (or self)
        if p.type == player.type:
            continue
        # don't attack dead people
        if not p.alive:
            continue
        # look around the target for a free space
        for d in [ (0,-1), (-1,0), (1,0), (0,1) ]:
            key = "{}_{}".format(p.x+d[0], p.y+d[1]) 
            # if this block is valid and empty
            if key in game_map and game_map[key] == '.':
                try:
                  pdata = find_path( graph, "{}_{}".format(player.x, player.y), "{}_{}".format(p.x+d[0], p.y+d[1]))
                  path_data.append( [ pdata.total_cost, p.x+d[0], p.y+d[1], pdata.nodes, p.reading])
                except:
                  continue
   
    # sort by the shortest distance, and then the lowest y value, and then the lowest x value
    path_data = sorted(path_data, key=lambda x: (x[0], x[4]))
    if len(path_data) >0:
        return path_data[0]           
    else:
        return None
            

def draw_map(game_map, width, height):
    for y in range(0, height):
      for x in range(0, width):
          key = "{}_{}".format(x,y)
          if key in game_map:
            print(game_map[key],  end='')
          else:
            print(key, "outside of map")

      for p in sorted(players, key=lambda x: (x.x, x.y)):
        if p.y == y and p.hp > 0:
          print("  {}({})".format(p.type, p.hp), end='')

      print()

def player_status(players):
    for p in players:
        print(p)


x = 0
y= 0
with open(input_file) as f:
    while True:
        c = f.read(1)

        if not c:
            break
        else:
            if c == "\n":
                width=x
                x = 0
                y +=1
                height+=1
            else:
                game_map[ "{}_{}".format(x,y) ] = c
                if c in ['G','E']:
                    players.append( MyStruct(type=c, x=x, y=y, attack=boost[c], hp=200, alive=True, reading=x+y*width))
                x+=1

# print(game_map)
#print(players)
# print(width,height)
# draw_map(game_map, width, height)
# quit()

def gameOver(players):
    if len(list(filter( lambda x: x.alive and x.type == 'E', players))) == 0:
        print("Elf Lost")
        winner = 'G'
        return 'G'
    if len(list(filter( lambda x: x.alive and x.type == 'G', players))) == 0:
        print("Goblin Lost")
        winner = 'E'
        return 'E'

    return False


rounds=0
winner=False
while True:
    for p in list(sorted(players, key=lambda x: (x.reading))):

        # skip over dead people
        if not p.alive:
            continue

        # Move phase
        data = find_closest( game_map, width, height, p, players)
        if data and not data[0] == 0:
            current_position = "{}_{}".format( p.x, p.y)
            new_x, new_y = map(int, data[3][1].split('_'))
            new_position = "{}_{}".format( new_x, new_y)

            #print("move from {},{} to {},{}".format(p.x,p.y, new_x, new_y))
            #print("from map {} to map {}".format( game_map[current_position], game_map[new_position]))

            game_map[ current_position ] = '.'
            game_map[ new_position ] = p.type
            p.x = new_x
            p.y = new_y
            p.reading = p.x + (p.y*width)

        # Attack Phase
        data = attack( game_map, width, height, p, players)
        if data:
            attack_x = data[2]
            attack_y = data[3]
            enemy = list(filter( lambda x: x.x == attack_x and x.y == attack_y and x.alive, players))[0]
            #print(p , "to attack:", enemy)
            enemy.hp -= p.attack
            if enemy.hp <= 0:
                if enemy.type == 'E':
                    print("Elf Died game over")
                    quit()

                #print("enemy:", enemy, " is dead")
                enemy.alive = False
                game_map[ "{}_{}".format(enemy.x, enemy.y) ] = "."

                cgo = gameOver(players)
                if cgo:
                    print("winner:", cgo)
                    winner=True
                    break
    
    if winner:
        break

    #draw_map(game_map, width, height)
    rounds +=1
    
draw_map(game_map, width, height)
total = sum([ x.hp for x in (filter(lambda x: x.type == cgo and x.alive, players))] )
print("Rounds:", rounds, " Total Winner:", total)
print( rounds * total)
