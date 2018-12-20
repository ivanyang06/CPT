class Obstacle(object):
    xkey = false
    ykey = false
    speedX = 0
    speedY = 0
    src = "Red.png"
    type = "blank"
    counter = 0
    lastDir = "up"
    direction = 2

    def __init__(self, x, y, width, height, src, movetype, type):
        self.src = src
        self.x = x
        self.y = y
        self.width = width 
        self.height = height 
        self.type = type 
        self.movetype = movetype 
   

    def setSource(String source):
        src = source 
   

    def move():
        if True: 
            x += speedX 
     
        if True:  
            y += speedY 
     
        if self.movetype == "movingenemy":
            self.x += direction 
     
   

    def animate():

   
    animate()
    
    def update(): 
        if xkey == False: 
            speedX = 0 
     
        if ykey == False:
            speedY = 0 
    
        if ((speedX == 0 and speedY == 0) or (counter == 22)):  
            counter = 0 
        else:  
            counter++ 
     
        if Game.tora.x + Game.Camera.x < self.x + self.width - 3 and Game.tora.x + Game.tora.width + Game.Camera.x > self.x + 3: 
          if Game.tora.y + Game.Camera.y <= self.y + self.height - 2and Game.tora.y + Game.tora.height + Game.Camera.y >= self.y + 10: 
            if self.type == "wall":  
                Game.tora.y += 3 
                Game.tora.up = false 
                Game.tora.loseHealth(2, 100) 
            
            if self.type == "urchon":
                Game.tora.loseHealth(10, 100) 
            
            if self.type == "aligo": 
                Game.tora.loseHealth(4, 100) 
            
            if self.type == "turtle":  
                Game.tora.loseHealth(3, 100) 
            
        
        if Game.tora.y + Game.Camera.y <= self.y + self.height - 10 and Game.tora.y + Game.Camera.y + Game.tora.height >= self.y + 2: 
            if self.type == "wall":  
                Game.tora.y -= 3 
                Game.tora.down = false 
                Game.tora.loseHealth(1, 100) 
                
            if self.type == "urchon":
                Game.tora.loseHealth(10, 100) 
            
            if self.type == "aligo": 
                Game.tora.loseHealth(3, 100) 
            
            if self.type == "turtle": 
                Game.tora.loseHealth(3, 100) 
            
        
        
        if Game.tora.y + Game.Camera.y < self.y + self.height - 3 and Game.tora.y + Game.tora.height + Game.Camera.y > self.y + 3:  
            if Game.tora.x + Game.Camera.x <= self.x + self.width - 2 and Game.tora.x + Game.Camera.x + Game.tora.width >= self.x + 10:
                if self.type == "wall": 
                    Game.tora.x += 3 
                    Game.tora.left = false 
                    Game.tora.loseHealth(1, 100) 
                
                if self.type == "urchon":  
                    Game.tora.loseHealth(10, 100) 
                
                if self.type == "aligo":  
                    Game.tora.loseHealth(3, 100) 
                
                if self.type == "turtle":
                    Game.tora.loseHealth(3, 100) 
            
        
        if Game.tora.x + Game.Camera.x <= self.x + self.width - 10 and Game.tora.x + Game.Camera.x + Game.tora.width >= self.x + 2:  
            if self.type == "wall":  
                Game.tora.x -= 3 
                Game.tora.right = false 
                Game.tora.loseHealth(1, 100) 
            
            if self.type == "urchon":  
                Game.tora.loseHealth(10, 100) 
            
            if self.type == "aligo":
                Game.tora.loseHealth(3, 100) 
            
            if self.type == "turtle": 
                Game.tora.loseHealth(3, 100) 
            
        
        
        if self.movetype == "movingenemy":
            if Game.weapon.attack == true and Game.weapon.x <= self.x + self.width and Game.weapon.x + Game.weapon.width >= self.x and Game.weapon.y + Game.Camera.y <= self.y + self.width and Game.weapon.y + Game.weapon.height + Game.Camera.y >= self.y):  
                if (self.type == "aligo"):
                    print("hit") 
                    Game.obstacles.remove(self) 
                elif self.type == "turtle" and Game.tora.attackDir == "up":  
                    print("hit") 
                    Game.obstacles.remove(self) 
            
        
        if direction > 0 and self.x + self.width + 10 > 512 or direction < 0 and self.x - 10 < 0: 
            direction *= -1 
        
        for i in Game.obstacles:
            if Game.obstacles.get(i).type == "wall":
                if self.y < Game.obstacles.get(i).y + Game.obstacles.get(i).height and self.y + self.width > Game.obstacles.get(i).y:
                    if direction > 0 and self.x + self.width + 10 > Game.obstacles.get(i).x and self.x + self.width + 10 < Game.obstacles.get(i).x + Game.obstacles.get(i).width:
                    direction *= -1 
                    break 
                
                if direction < 0 and self.x - 10 > Game.obstacles.get(i).x and self.x - 10 < Game.obstacles.get(i).x + Game.obstacles.get(i).width:  
                    direction *= -1 
                    break 
                

    def paint(Graphics2D g):
        ImageIcon picture = new ImageIcon(src) 
        Image MyCharacter = picture.getImage() 
        g.drawImage(MyCharacter, x, y, width, height, null) 
    
    
    def keyReleased(KeyEvent e):
        if e.getKeyCode() == KeyEvent.VK_LEFT or e.getKeyCode() == KeyEvent.VK_RIGHT: 
            xkey = false 
        else:
            ykey = false 

     
   

  public void keyPressed(KeyEvent e)  
    if (e.getKeyCode() == KeyEvent.VK_LEFT)  
      xkey = true 
      speedX = 1 
     
    if (e.getKeyCode() == KeyEvent.VK_RIGHT)  
      xkey = true 
      speedX = -1 
     
    if (e.getKeyCode() == KeyEvent.VK_UP)  
      ykey = true 
      speedY = 1 
     
    if (e.getKeyCode() == KeyEvent.VK_DOWN)  
      ykey = true 
      speedY = -1 
     
   
 
