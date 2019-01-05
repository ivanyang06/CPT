class Item(object):
    src = "red.png"
    def __init__(self, x, y, width, height, type, src):
        self.src = src
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.type = type
    
    
    def setSource(source):
        src = source
    
    
    def update():
        if Game.tora.x + Game.tora.width >= self.x and Game.tora.x <= self.x + self.width and Game.tora.y + Game.tora.height + Game.Camera.y >= self.y and Game.tora.y + Game.Camera.y <= self.y + self.height:
            if self.type == "bigTreasure":
                Game.tora.bigTreasure = true
                Game.treasures.remove(this)
                Game.bigChest.src = "yellow.png"
                return
        
        if self.type == "smallTreasure": 
            Game.treasures.remove(this)
            Game.collectedTreasure.add(character((Game.collectedTreasures % 2) * 34 + 599, (Game.collectedTreasures - Game.collectedTreasures % 2) * 17 + 266, 32, 32, "yellow.png","blank"))
            Game.collectedTreasures+=1
            print("item!")
            
    def paint(self):
        loadedimage = loadImage(self.src)
        image(loadedimage,self.x,self.y,self.width,self.height)
