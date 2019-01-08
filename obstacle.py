class Obstacle(object):
    xkey = False
    ykey = False
    speedX = 0
    speedY = 0
    src = "red.png"
    type = "blank"
    counter = 0
    lastDir = "up"
    direction = 2
    loadedimage = ""

    def __init__(self, x, y, width, height, src, movetype, type):
        self.src = src
        self.x = x
        self.y = y
        self.width = width 
        self.height = height 
        self.type = type 
        self.movetype = movetype 
   

    def setup(self):
        self.loadedimage = loadImage(self.src)
   

    def move(self):
        if True: 
            self.x += self.speedX 
     
        if True:  
            self.y += self.speedY 
     
        if self.movetype == "movingenemy":
            self.x += self.direction 
     
   

    def animate():
        print("animate called")
   
    animate()
    
    def update(self, tora, Camera): 
        if self.xkey == False: 
            self.speedX = 0 
     
        if self.ykey == False:
            self.speedY = 0 
    
        if ((self.speedX == 0 and self.speedY == 0) or (self.counter == 22)):  
            self.counter = 0 
        else:  
            self.counter+=1
     
        if tora.x + Camera.x < self.x + self.width - 3 and tora.x + tora.width + Camera.x > self.x + 3: 
          if tora.y + Camera.y <= self.y + self.height - 2 and tora.y + tora.height + Camera.y >= self.y + 10: 
            if self.type == "wall":  
                tora.y += 4
                tora.up = False 
                tora.loseHealth(2, 100) 
            
            if self.type == "urchon":
                tora.loseHealth(10, 100) 
            
            if self.type == "aligo": 
                tora.loseHealth(4, 100) 
            
            if self.type == "turtle":  
                tora.loseHealth(3, 100) 
            
        
          if tora.y + Camera.y <= self.y + self.height - 10 and tora.y + Camera.y + tora.height >= self.y + 2: 
            if self.type == "wall":  
                tora.y -= 4
                tora.down = False 
                tora.loseHealth(1, 100) 
                
            if self.type == "urchon":
                tora.loseHealth(10, 100) 
            
            if self.type == "aligo": 
                tora.loseHealth(4, 100) 
            
            if self.type == "turtle": 
                tora.loseHealth(3, 100) 
            
        
        
        if tora.y + Camera.y < self.y + self.height - 3 and tora.y + tora.height + Camera.y > self.y + 3:  
            if tora.x + Camera.x <= self.x + self.width - 2 and tora.x + Camera.x + tora.width >= self.x + 10:
                if self.type == "wall": 
                    tora.x += 4
                    tora.left = False 
                    tora.loseHealth(1, 100) 
                
                if self.type == "urchon":  
                    tora.loseHealth(10, 100) 
                
                if self.type == "aligo":  
                    tora.loseHealth(4, 100) 
                
                if self.type == "turtle":
                    tora.loseHealth(3, 100) 
            
        
            if tora.x + Camera.x <= self.x + self.width - 10 and tora.x + Camera.x + tora.width >= self.x + 2:  
                if self.type == "wall":  
                    tora.x -= 4
                    tora.right = False 
                    tora.loseHealth(1, 100) 
            
                if self.type == "urchon":  
                    tora.loseHealth(10, 100) 
            
                if self.type == "aligo":
                    tora.loseHealth(4, 100) 
            
                if self.type == "turtle": 
                    tora.loseHealth(3, 100) 
            
        
        
#        if self.movetype == "movingenemy":
#            if Game.weapon.attack == True and Game.weapon.x <= self.x + self.width and Game.weapon.x + Game.weapon.width >= self.x and Game.weapon.y + Game.Camera.y <= self.y + self.width and Game.weapon.y + Game.weapon.height + Game.Camera.y >= self.y:  
#                if (self.type == "aligo"):
#                    print("hit") 
#                    Game.obstacles.remove(self) 
#                elif self.type == "turtle" and Game.tora.attackDir == "up":  
#                    print("hit") 
#                    Game.obstacles.remove(self) 
#            
#        
#        if direction > 0 and self.x + self.width + 10 > 512 or direction < 0 and self.x - 10 < 0: 
#            direction *= -1 
#        
#        for i in Game.obstacles:
#            if Game.obstacles.get(i).type == "wall":
#                if self.y < Game.obstacles.get(i).y + Game.obstacles.get(i).height and self.y + self.width > Game.obstacles.get(i).y:
#                    if direction > 0 and self.x + self.width + 10 > Game.obstacles.get(i).x and self.x + self.width + 10 < Game.obstacles.get(i).x + Game.obstacles.get(i).width:
#                        direction *= -1 
#                        break 
#                
#                if direction < 0 and self.x - 10 > Game.obstacles.get(i).x and self.x - 10 < Game.obstacles.get(i).x + Game.obstacles.get(i).width:  
#                    direction *= -1 
#                    break 

    def paint(self):
        image(self.loadedimage,self.x,self.y,self.width,self.height)
    
    
    def keyReleased(e):
        if e.getKeyCode() == KeyEvent.VK_LEFT or e.getKeyCode() == KeyEvent.VK_RIGHT: 
            xkey = False 
        else:
            ykey = False 
