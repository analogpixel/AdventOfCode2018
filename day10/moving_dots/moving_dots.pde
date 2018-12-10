PVector [] points;
PVector [] velocity;
float maxx=0;
float minx=Float.POSITIVE_INFINITY;;
float maxy=0;
float miny=Float.POSITIVE_INFINITY;;
float counter=0;

void setup() { 
  //size(398*4,289*4);
  //size(1592, 1156);
  //size(398, 289);
  size(200,100);
  String[] lines = loadStrings("input.txt");
  
  points = new PVector[lines.length];
  velocity = new PVector[lines.length];
  
  for (int i = 0 ; i < lines.length; i++) {
    //println(lines[i]);
    String[] m = match(lines[i], "position=<(.*?), (.*?)> velocity=<(.*), (.*)>");
    
    points[i] = new PVector(0,0);
    velocity[i] = new PVector(0,0);
    points[i].x = Integer.parseInt(m[1].replaceAll("\\s",""));
    points[i].y = Integer.parseInt(m[2].replaceAll("\\s",""));
    velocity[i].x = Integer.parseInt(m[3].replaceAll("\\s",""));
    velocity[i].y = Integer.parseInt(m[4].replaceAll("\\s",""));
    
    if (points[i].x > maxx) { maxx = points[i].x;}
    if (points[i].x < minx) { minx = points[i].x;}
    if (points[i].y > maxy) { maxy = points[i].y;}
    if (points[i].y < miny) { miny = points[i].y;}
      
    println(points[i].x, points[i].y, velocity[i].x, velocity[i].y);
    
  }
  println(minx,maxx, miny, maxy);
}

void draw() {
  
}

void keyPressed() {
  background(255);
  int z = 0;
  if (key == '1') {
    z = 1;
  }
  
  if (key == '2') {
    z = 10391;
    }
  
  if (key == '3') {
    z = 1000;
  }
  
  if (key == '4') {
    z = 10000;
  }
  
  if (key == '5') {
    z = 100000;
  }
  
  if (key == '6') {
    z = 1000000000;
  }
  
  counter+=z;
  println("Counter:", counter);
  
  
    maxx=0;
    minx=Float.POSITIVE_INFINITY;;
    maxy=0;
    miny=Float.POSITIVE_INFINITY;;
  
    for (int i=0; i < points.length; i++) {
      points[i].x += velocity[i].x * z;
      points[i].y += velocity[i].y * z;
      
       if (points[i].x > maxx) { maxx = points[i].x;}
       if (points[i].x < minx) { minx = points[i].x;}
       if (points[i].y > maxy) { maxy = points[i].y;}
       if (points[i].y < miny) { miny = points[i].y;}
  
    }
    
    
    for (int i=0; i < points.length; i++) {
      float x = map(points[i].x, minx,maxx, 20, width-20);
      float y = map(points[i].y, miny,maxy, 20, height-20);
      fill(0);
      ellipse(x,y,5,5);
    }
  
}
