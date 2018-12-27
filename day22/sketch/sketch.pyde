
depth=7863
elf_x=14
elf_y=760

"""
depth=510
elf_x=10
elf_y=10
"""
bs = 40
geo_index = []
ero_index = []
for y in range(0, elf_y+6):
    geo_index.append( [0] * (elf_x + 6))
    ero_index.append( [0] * (elf_x + 6))

# 0: rock : climbing gear(2) or torch(1)
# 1: wet : climbing gear(2) or neither(0)
# 2: narrow : torch(1) or neither(0)
def drawBlock(t,x,y):
    pushMatrix()
    translate(x,y)
      
    #bw = bs // 4
    bw = 10
    d = (0,0,0)
    
    if t == 0:
        d = (1,1,0)
    elif t == 1:
        d = (1,0,1)
    elif t == 2:
        d = (0,1,1)
    
    noStroke()

    if d[2] == 1:
        fill(0,0,255)
        rect((bw*3+10),0, bw,bs)
        rect(0,(bw*3+10), bs,bw)
    
    
    if d[1] == 1:
        fill(0,255,0)
        rect(bw*2+5,0, bw,bs)
        rect(0,bw*2+5, bs,bw)
    
    if d[0] == 1:
        fill(255,0,0)
        rect(0,0, bs,bw)
        rect(0,0, bw,bs)
    
    noFill()
    stroke(255)
    strokeWeight(2)
    rect(0,0,bs,bs)
    
    """
    if d[2] == 1:
        fill(0,0,255)
        rect((bw*2),(bw*2), bs,bw)
        rect((bw*2),(bw*2), bw,bs)
    """
    popMatrix()
    
def setup():
    size((elf_x+6)* bs, (elf_y+6) * bs)
    
    t = ['.', '=', '|']
    
    for x in range(0, elf_x+6):
        for y in range(0, elf_y+6):
            if (x==elf_x) and (y==elf_y):
                geo_index[y][x] = 0
            elif x==0 and y==0:
                geo_index[y][x] == 0
            elif y == 0:
                geo_index[y][x] = x * 16807
            elif x == 0:
                geo_index[y][x] = y * 48271
            else:
                geo_index[y][x] = ero_index[y][x-1] * ero_index[y-1][x]
    
            ero_index[y][x] = ((geo_index[y][x] + depth) % 20183) 
    
    for e in ero_index:
        print("".join(map(lambda x: t[x%3], e)))

def draw():
    background(255)
    for x in range(0, elf_x + 6):
        for y in range(0, elf_y + 6):
            drawBlock(ero_index[y][x]%3, x*bs,y*bs)
    
    fill(255,0,255,100)
    rect(elf_x*bs, elf_y*bs, bs,bs)
