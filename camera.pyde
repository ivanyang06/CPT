class camera(object):
    xkey = False 
    ykey = False 
    x = 0 
    y = 0 
    counter = 0 
    speedX = 0 
    speedY = 0 
    movement = "down" 
    
    def __init__(self, x, y):
        self.x = x 
        self.y = y 
     
    
    def update(self):
        if self.xkey == False:
            self.speedX = 0 
         
        if self.ykey == False: 
            self.speedY = 0 
         
        if Game.background.height - Game.frameheight > self.y: 
            if self.movement == "down":  
                self.speedY += 2 
         
         
        if Game.tora.bigTreasure == true and self.counter < 100:  
            self.movement = "up" 
            self.counter+=1
        #if self.counter == 100:  
        #    Game.bgm.close() 
        #    Game.playSound("TigerTigerUp.wav", "bgm") 
         
         
        if self.movement == "up" and self.counter == 100:  
            self.speedY -= 3 
         
        if self.y <= 0 and Game.tora.bigTreasure:  
            self.movement = "stop" 
         
        if Game.tora.health <= 0:
            self.movement = "dead" 
            Game.gameStatus = "lost" 
         
        if self.movement == "stop":
            Game.tora.y -= 4 
            Game.tora.lastDir = "up" 
            Game.tora.speedX = 0 
            Game.tora.speedY = 0 
            Game.tora.moving = false 
            
            
            x += speedX 
            y += speedY 
        
     
