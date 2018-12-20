class camera(object):
    xkey = False 
    ykey = False 
    x = 0 
    y = 0 
    counter = 0 
    speedX = 0 
    speedY = 0 
    movement = "down" 
    
    def camera(int x, int y): 
        self.x = x 
        self.y = y 
     
    
    def update():
        if xkey == False:
            speedX = 0 
         
        if ykey == False: 
            speedY = 0 
         
        if Game.background.height - Game.frameheight > self.y: 
            if movement == "down":  
                speedY += 2 
         
         
        if Game.tora.bigTreasure == true && counter < 100:  
            movement = "up" 
            counter++ 
        ifcounter == 100:  
            Game.bgm.close() 
            Game.playSound("TigerTigerUp.wav", "bgm") 
         
         
        if movement == "up" && counter == 100:  
            speedY -= 3 
         
        if self.y <= 0 && Game.tora.bigTreasure:  
            movement = "stop" 
         
        if Game.tora.health <= 0:
            movement = "dead" 
            Game.gameStatus = "lost" 
         
        if movement == "stop":  
            Game.tora.y -= 4 
            Game.tora.lastDir = "up" 
            Game.tora.speedX = 0 
            Game.tora.speedY = 0 
            Game.tora.moving = false 
            
            
            x += speedX 
            y += speedY 
        
     
