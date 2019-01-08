class character(object):
  xkey = False
  ykey = False
  xdir = ""
  ydir = ""
  up = True
  down = True
  left = True
  right = True
  leftpressed = False
  rightpressed = False
  uppressed = False
  downpressed = False
  moving = True
  attack = False
  attackDir = ""
  speedX = 0
  speedY = 0
  counter = 0
  attackcounter = 0
  lastDir = "up"
  bigTreasure = False
  health = 10
  invincible = 0
  attackposition = 1
  src = loadImage("red.png")
  loadedimage = ""

  directionqueue = []
  verticalqueue = []
  horizontalqueue = []
  
  def __init__(self, x, y, width, height, src, type):
      self.x = x
      self.y = y
      self.width = width
      self.height = height
      self.src = src
      self.type = type

  def setup(self):
      self.loadedimage = loadImage(self.src)

  def move(self,framewidth,frameheight):
    #if ((self.x - 2 >= 0 and self.speedX < 0) or (self.x + self.width + 2 <= 512 and self.speedX > 0)):
     # if ((self.left == True and self.xdir == "left") or (self.right == True and self.xdir == "right")):
        self.x += self.speedX
    #if ((self.y - 2 >= 0 and self.speedY < 0) or (self.y + self.height + 2 <= frameheight and self.speedY > 0)) :
     # if ((self.up == True and self.ydir == "up") or (self.down == True and self.ydir == "down")) :
        self.y += self.speedY
  

  def animate(self) :
    if (self.type == "character") :
      if (self.invincible % 10 > 7) :
        self.src = "yellow.png"
      elif (Game.weapon.attack == True) :
        if (attackDir == "up") :
          if (Game.animationcounter <= 10) :
            self.src = "toraupattack1.png"
          elif (Game.animationcounter <= 20) :
            self.src = "toraupattack2.png"
          
        elif (attackDir == "down") :
          if (Game.animationcounter <= 10) :
            self.src = "toradownattack1.png"
          elif (Game.animationcounter <= 20) :
            self.src = "toradownattack2.png"
          
        elif (attackDir == "left") :
          if (Game.animationcounter <= 10) :
            self.src = "toraleftattack1.png"
          elif (Game.animationcounter <= 20) :
            self.src = "toraleftattack2.png"
          
        elif (attackDir == "right") :
          if (Game.animationcounter <= 10) :
            self.src = "torarightattack1.png"
          elif (Game.animationcounter <= 20) :
            self.src = "torarightattack2.png"
          
        
      elif (not directionqueue) :
        if (directionqueue.get(0) == "up") :
          if (Game.animationcounter <= 10) :
            self.src = "toraup1.png"
          elif (Game.animationcounter <= 20) :
            self.src = "toraup2.png"
          
        elif (directionqueue.get(0) == "down") :
          if (Game.animationcounter <= 10) :
            self.src = "toradown1.png"
          elif (Game.animationcounter <= 20) :
            self.src = "toradown2.png"
          
        elif (directionqueue.get(0) == "left") :
          if (Game.animationcounter <= 10) :
            self.src = "toraleft1.png"
          elif (Game.animationcounter <= 20) :
            self.src = "toraleft2.png"
          
        elif (directionqueue.get(0) == "right") :
          if (Game.animationcounter <= 10) :
            self.src = "toraright1.png"
          elif (Game.animationcounter <= 20) :
            self.src = "toraright2.png"
        
      else :
        if (lastDir == "up") :
          if (Game.animationcounter <= 10) :
            self.src = "toraup1.png"
          elif (Game.animationcounter <= 20) :
            self.src = "toraup2.png"
          
        elif (lastDir == "down") :
          if (Game.animationcounter <= 10) :
            self.src = "toradown1.png"
          elif (Game.animationcounter <= 20) :
            self.src = "toradown2.png"
          
        elif (lastDir == "left") :
          if (Game.animationcounter <= 10) :
            self.src = "toraleft1.png"
          elif (Game.animationcounter <= 20) :
            self.src = "toraleft2.png"
          
        elif (lastDir == "right") :
          if (Game.animationcounter <= 10) :
            self.src = "toraright1.png"
          elif (Game.animationcounter <= 20) :
            self.src = "toraright2.png"

  def loseHealth(self, healthAmount, invincibleAmount):
    return 
      
    if (self.invincible == 0):
      self.health -= healthAmount
      self.invincible += invincibleAmount
      if (not game.collectedTreasure):
        Game.collectedTreasure.remove(Game.collectedTreasure.size() - 1)
        Game.collectedTreasures-=1
      elif (Game.tora.bigTreasure == True):
        Game.bigChest.src = ""

  def update(self, frameheight, framewidth):
    #if (self.invincible > 0):
    #  self.invincible-=1
    #if (Game.weapon.attack == True):
    #  attackcounter += attackposition
    #  if (attackcounter == 15):
    #    attackposition = -1
    #    
    #  if (attackDir == "up"):
    #    Game.weapon.y = Game.tora.y - attackcounter * 10
    #    Game.weapon.x = Game.tora.x + Game.tora.width / 2 - Game.weapon.width / 2
    #    
    #  if (attackDir == "down"):
    #    Game.weapon.y = Game.tora.y + attackcounter * 10
    #    Game.weapon.x = Game.tora.x + Game.tora.width / 2 - Game.weapon.width / 2
    #    
    #  if (attackDir == "left"):
    #    Game.weapon.x = Game.tora.x - attackcounter * 10
    #    Game.weapon.y = Game.tora.y + Game.tora.height / 2 - Game.weapon.height / 2
    #    
    #  if (attackDir == "right"):
    #    Game.weapon.x = Game.tora.x + attackcounter * 10
    #    Game.weapon.y = Game.tora.y + Game.tora.height / 2 - Game.weapon.height / 2
    #    
    #  if (((attackDir == "up" or attackDir == "down") and Game.weapon.y == Game.tora.y) or ((attackDir == "left" or attackDir == "right") and Game.weapon.x == Game.tora.x)):
    #    Game.weapon.attack = False
    #    attackcounter = 0
    #    attackposition = 1
    #    Game.weapon.src = ""
    #  else:
    #    Game.weapon.y = Game.tora.y
    #    Game.weapon.x = Game.tora.x

    if (self.y + self.height > frameheight):
      self.y = frameheight - self.height
    if (self.y < 0 and self.moving == True):
      self.y = 0
      
    if (len(self.horizontalqueue)==0):
      self.speedX = 0
    elif (self.horizontalqueue[0] == "left"):
      self.speedX = -3
    elif (self.horizontalqueue[0] == "right"):
      self.speedX = 3

    if (len(self.verticalqueue) == 0):
      self.speedY = 0
    elif (self.verticalqueue[0] == "up"):
      self.speedY = -3
    elif (self.verticalqueue[0] == "down"):
      self.speedY = 3

    #animate()

    if ((self.speedX == 0 and self.speedY == 0) or (self.counter == 22)):
      self.counter = 0
    else:
      self.counter+=1

    # System.out.println(horizontalqueue)
    # System.out.println(verticalqueue)
    # System.out.println(directionqueue)

  def paint(self):
    image(self.loadedimage,self.x,self.y,self.width,self.height)

  def keyReleased(self):
    if (key == 'a'):
      try:
        self.xkey = False
        self.directionqueue.remove("left")
        self.horizontalqueue.remove("left")
        self.leftpressed = False
        lastDir = "left"
      except:
        pass
      
    if (key == 'd'):
      try:
        self.xkey = False
        self.directionqueue.remove("right")
        self.horizontalqueue.remove("right")
        self.rightpressed = False
        lastDir = "right"
      except:
        pass
      
    if (key == 'w'):
      try:
        self.ykey = False
        self.directionqueue.remove("up")
        self.verticalqueue.remove("up")
        self.uppressed = False
        lastDir = "up"
      except:
        pass
      
    if (key == 's'):
      try:
        self.ykey = False
        self.directionqueue.remove("down")
        self.verticalqueue.remove("down")
        self.downpressed = False
        lastDir = "down"
      except:
        pass

  def keyPressed(self):
    #print(key)
    if (self.moving == True):
      if (key == 'a' and self.left == True and self.leftpressed == False):
        self.directionqueue.insert(0, "left")
        self.horizontalqueue.insert(0, "left")
        self.xkey = True
        self.xdir = "left"
        self.leftpressed = True
        
      if (key == 'd' and self.right == True and self.rightpressed == False):
        self.directionqueue.insert(0, "right")
        self.horizontalqueue.insert(0, "right")
        self.xkey = True
        self.xdir = "right"
        self.rightpressed = True
        
      if (key == 'w' and self.up == True and self.uppressed == False):
        self.directionqueue.insert(0, "up")
        self.verticalqueue.insert(0, "up")
        self.ykey = True
        self.ydir = "up"
        self.uppressed = True
        
      if (key == 's' and self.down == True and self.downpressed == False):
        self.directionqueue.insert(0, "down")
        self.verticalqueue.insert(0, "down")
        self.ykey = True
        self.ydir = "down"
        self.downpressed = True
        
#      if (Game.Camera.movement == "down" and keyCode == ' ' and Game.weapon.attack == False):
#        Game.weapon.attack = True
#        if (not directionqueue):
#          attackDir = directionqueue.get(0)
#        else:
#          attackDir = lastDir
#        Game.playSound("attack.wav", "attack")
#        if(attackDir == "up"):
#          Game.weapon.src = "upattack.png"
#        elif(attackDir == "down"):
#          Game.weapon.src = "downattack.png"
#        elif(attackDir == "left"):
#          Game.weapon.src = "leftattack.png"
#        elif(attackDir == "right"):
#          Game.weapon.src = "rightattack.png"
#    
