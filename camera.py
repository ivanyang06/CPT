class camera(object):
    xkey = False 
    ykey = False 
    x = 0 
    y = 0 
    counter = 0 
    deathcounter = 0
    speedX = 0 
    speedY = 0 
    movement = "down" 
    
    def __init__(self, x, y):
        self.x = x 
        self.y = y 
     
    
    def update(self, background, frameheight, tora, gameStatus):
        if self.xkey == False:
            self.speedX = 0 
         
        if self.ykey == False: 
            self.speedY = 0 
         
        if background.height - frameheight > self.y: 
            if self.movement == "down":  
                self.speedY += 2
         
         
        if tora.bigTreasure and self.counter < 100:
            self.movement = "up" 
            self.counter+=1
        #if self.counter == 100:  
        #    Game.bgm.close() 
        #    Game.playSound("TigerTigerUp.wav", "bgm") 
         
         
        if self.movement == "up" and self.counter == 100:  
            self.speedY -= 3 
         
        if self.y <= 0 and tora.bigTreasure:  
            self.movement = "stop"
            gameStatus = "done"
         
        if tora.health <= 0:
            self.movement = "dead"
            
        if self.movement == "dead":
            self.deathcounter+=1
            if self.deathcounter == 50:
                gameStatus = "lost"
            
         
        if self.movement == "stop" and gameStatus == "done":
            tora.y -= 4 
            tora.lastDir = "up" 
            tora.speedX = 0 
            tora.speedY = 0 
            tora.moving = False 
            if tora.y <= -50:
                gameStatus = "won"
            
            
        self.x += self.speedX 
        self.y += self.speedY 
        
        return gameStatus
     
