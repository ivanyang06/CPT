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
    
    def update(self, tora, Camera, obstacles, weapon): 
        if self.xkey == False: 
            self.speedX = 0 
     
        if self.ykey == False:
            self.speedY = 0 
    
        if ((self.speedX == 0 and self.speedY == 0) or (self.counter == 22)):  
            self.counter = 0 
        else:  
            self.counter+=1
     
        if tora.x + Camera.x < self.x + self.width - 3 and tora.x + tora.width + Camera.x > self.x + 3: 
          if tora.y + Camera.y <= self.y + self.height - 3 and tora.y + tora.height + Camera.y >= self.y + 10: 
            if self.type == "wall":  
                tora.y += 5
                tora.up = False 
                tora.loseHealth(2, 100) 
            
            if self.type == "urchon":
                tora.loseHealth(10, 100) 
            
            if self.type == "aligo": 
                tora.loseHealth(4, 100) 
            
            if self.type == "turtle":  
                tora.loseHealth(3, 100) 
            
        
          if tora.y + Camera.y <= self.y + self.height - 10 and tora.y + Camera.y + tora.height >= self.y + 3: 
            if self.type == "wall":  
                tora.y -= 5
                tora.down = False 
                tora.loseHealth(1, 100) 
                
            if self.type == "urchon":
                tora.loseHealth(10, 100) 
            
            if self.type == "aligo": 
                tora.loseHealth(4, 100) 
            
            if self.type == "turtle": 
                tora.loseHealth(3, 100) 
            
        
        
        if tora.y + Camera.y < self.y + self.height - 3 and tora.y + tora.height + Camera.y > self.y + 3:  
            if tora.x + Camera.x <= self.x + self.width - 3 and tora.x + Camera.x + tora.width >= self.x + 10:
                if self.type == "wall": 
                    tora.x += 3
                    tora.left = False 
                    tora.loseHealth(1, 100) 
                
                if self.type == "urchon":  
                    tora.loseHealth(10, 100) 
                
                if self.type == "aligo":  
                    tora.loseHealth(4, 100) 
                
                if self.type == "turtle":
                    tora.loseHealth(3, 100) 
            
        
            if tora.x + Camera.x <= self.x + self.width - 10 and tora.x + Camera.x + tora.width >= self.x + 3:  
                if self.type == "wall":  
                    tora.x -= 3
                    tora.right = False 
                    tora.loseHealth(1, 100) 
            
                if self.type == "urchon":  
                    tora.loseHealth(10, 100) 
            
                if self.type == "aligo":
                    tora.loseHealth(4, 100) 
            
                if self.type == "turtle": 
                    tora.loseHealth(3, 100) 
            
        
        
        if self.movetype == "movingenemy":
            if weapon.attack == True and weapon.x <= self.x + self.width and weapon.x + weapon.width >= self.x and weapon.y + Camera.y <= self.y + self.width and weapon.y + weapon.height + Camera.y >= self.y:  
                if (self.type == "aligo"):
                    print("hit") 
                    obstacles.remove(self) 
                elif self.type == "turtle" and tora.attackDir == "up":  
                    print("hit") 
                    obstacles.remove(self) 
            
        
        if self.direction > 0 and self.x + self.width + 10 > 512 or self.direction < 0 and self.x - 10 < 0: 
            self.direction *= -1 
        
        for i in obstacles:
            if i.type == "wall":
                if self.y < i.y + i.height and self.y + self.width > i.y:
                    if self.direction > 0 and self.x + self.width + 10 > i.x and self.x + self.width + 10 < i.x + i.width:
                        self.direction *= -1 
                        break             
                    if self.direction < 0 and self.x - 10 > i.x and self.x - 10 < i.x + i.width:  
                        self.direction *= -1 
                        break 

    def paint(self):
        image(self.loadedimage,self.x,self.y,self.width,self.height)
    
    
    def keyReleased(e):
        if e.getKeyCode() == KeyEvent.VK_LEFT or e.getKeyCode() == KeyEvent.VK_RIGHT: 
            xkey = False 
        else:
            ykey = False 
