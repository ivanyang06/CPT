from character import *
tempcollectedtreasures = 0
score = 0


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
        if self.type == "gems":
            self.loadedimage = loadImage("gem.png")
        else:
            self.loadedimage = loadImage("treasure.png")

    def update(self, tora, Camera, treasures, collectedTreasure, collectedTreasures, bigChest):
        global tempcollectedtreasures
        global score
        if tora.x + tora.width >= self.x and tora.x <= self.x + self.width and tora.y + tora.height + Camera.y >= self.y and tora.y + Camera.y <= self.y + self.height:
            if self.type == "bigTreasure":
                tora.bigTreasure = True
                treasures.remove(self)
                chest = loadImage("treasure.png")
                bigChest.currentimage = chest

            if self.type == "smallTreasure":
                treasures.remove(self)
                collectedTreasure.append(character((tempcollectedtreasures % 2) * 65 + 569, (tempcollectedtreasures - tempcollectedtreasures % 2) * 18 + 266, 32, 32, "treasure.png", "blank"))
                collectedTreasures += 1
                tempcollectedtreasures += collectedTreasures
                collectedTreasure[tempcollectedtreasures-1].setup()
                print("item!")

            if self.type == "gems":
                treasures.remove(self)
                collectedTreasures += 1
                collectedTreasure.append(1)
                score += 100
        return tempcollectedtreasures

    def paint(self):
        image(self.loadedimage, self.x, self.y, self.width, self.height)
