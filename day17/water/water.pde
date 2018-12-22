char [][] v_map;

void drawMap() {
  background(255);
  color c = color(0,0,0);
  for (int x=0; x < width; x++) {
    for (int y=0; y < height; y++) {
      if (v_map[x][y] == '.') c = color(255,0,0);
      if (v_map[x][y] == '#') c = color(0,255,0);
      if (v_map[x][y] == '+') c = color(0,0,255);
      
      set(x,y,c);
    }
  }
}

void setup() {
  size(2000,2000);

  v_map = new char[width][height];
  
  for(int x=0; x < width; x++) {
    for(int y=0; y < height; y++) {
      v_map[x][y] = '.';
    }
  }
  
  v_map[500][0] = '+';
    
  String[] lines = loadStrings("input.txt");

  for (int i = 0 ; i < lines.length; i++) {
    // x=392, y=96..123

    // if the line starts with an x
    if (lines[i].charAt(0) == 'x') {
      String[] m = match(lines[i], "x=(.*?), y=(.[^\\.]*?)\\.\\.(.[^\\.]*?)");
      println(m[0]);
      int x = Integer.parseInt(m[1].replaceAll("\\s",""));
      int y1 = Integer.parseInt(m[2].replaceAll("\\s",""));
      int y2 = Integer.parseInt(m[3].replaceAll("\\s",""));
      
      if (y1 > y2) {
        int t = y1;
        y1 = y2;
        y2 = t;
      }
      
      for (int yy=y1; yy<= y2; yy++) {
         v_map[x][yy] = '#';
      }
    }
    
    
    
  }  
  
}

void draw() {
  drawMap();
}
