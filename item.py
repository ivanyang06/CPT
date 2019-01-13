from character import *
class Item(object):
    src = "red.png"
    def __init__(self, x, y, width, height, type, src):
        self.src = src
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.type = type
    
    
    def setup(self):
        self.loadedimage = loadImage("yellow.png")
    
    
    def update(self,tora,Camera,treasures,collectedTreasure, collectedTreasures , bigChest):
        if tora.x + tora.width >= self.x and tora.x <= self.x + self.width and tora.y + tora.height + Camera.y >= self.y and tora.y + Camera.y <= self.y + self.height:
            if self.type == "bigTreasure":
                tora.bigTreasure = True
                treasures.remove(self)
                bigChest.src = "yellow.png"
                return
        
            if self.type == "smallTreasure": 
                treasures.remove(self)
                collectedTreasure.append(character((collectedTreasures % 2) * 34 + 599, (collectedTreasures - collectedTreasures % 2) * 17 + 266, 32, 32, "yellow.png","blank"))
                collectedTreasures+=1
                print("item!")
                return
            
    def paint(self):
        image(self.loadedimage,self.x,self.y,self.width,self.height)
