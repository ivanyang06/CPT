from obstacle import *
from item import *
import random
class Map(object):
    def createMap(self,obstacles,treasures,background):
        obstacles.append(Obstacle(224, 256, 32, 32, "wall.png", "still", "wall"))
        obstacles.append(Obstacle(256, 256, 32, 32, "wall.png", "still", "wall"))
    
        obstacles.append(Obstacle(96, 448, 32, 32, "wall.png", "still", "wall"))
        obstacles.append(Obstacle(64, 448, 32, 32, "wall.png", "still", "wall"))
        obstacles.append(Obstacle(96, 480, 32, 32, "wall.png", "still", "wall"))
        obstacles.append(Obstacle(64, 480, 32, 32, "wall.png", "still", "wall"))
    
        obstacles.append(Obstacle(416, 448, 32, 32, "wall.png", "still", "wall"))
        obstacles.append(Obstacle(384, 448, 32, 32, "wall.png", "still", "wall"))
        obstacles.append(Obstacle(416, 480, 32, 32, "wall.png", "still", "wall"))
        obstacles.append(Obstacle(384, 480, 32, 32, "wall.png", "still", "wall"))

        layouts = [None] * 5
        chestlayout = [None] * 5
        enemies = [None] * 5
        for i in range(len(layouts)):
            layouts[i] = []
        chestlayout[0] = Item(192, -32, 32, 32, "smallTreasure", "yellow.png")
        layouts[0].append(Obstacle(192, 0, 32, 32, "wall.png", "still", "wall"))
        layouts[0].append(Obstacle(192, 32, 32, 32, "wall.png", "still", "wall"))
        layouts[0].append(Obstacle(224, 0, 32, 32, "wall.png", "still", "wall"))
        layouts[0].append(Obstacle(224, 32, 32, 32, "wall.png", "still", "wall"))
        enemies[0]=(Obstacle(150, 30, 40, 20, "turtle0.png", "movingenemy", "turtle"))
    
        layouts[0].append(Obstacle(64, 192, 32, 32, "wall.png", "still", "wall"))
        layouts[0].append(Obstacle(64, 224, 32, 32, "wall.png", "still", "wall"))
        layouts[0].append(Obstacle(64, 256, 32, 32, "wall.png", "still", "wall"))
        layouts[0].append(Obstacle(96, 192, 32, 32, "wall.png", "still", "wall"))
        layouts[0].append(Obstacle(96, 224, 32, 32, "wall.png", "still", "wall"))
        layouts[0].append(Obstacle(96, 256, 32, 32, "wall.png", "still", "wall"))
    
        layouts[0].append(Obstacle(416, 192, 32, 32, "wall.png", "still", "wall"))
        layouts[0].append(Obstacle(416, 224, 32, 32, "wall.png", "still", "wall"))
        layouts[0].append(Obstacle(416, 256, 32, 32, "wall.png", "still", "wall"))
        layouts[0].append(Obstacle(384, 192, 32, 32, "wall.png", "still", "wall"))
        layouts[0].append(Obstacle(384, 224, 32, 32, "wall.png", "still", "wall"))
        layouts[0].append(Obstacle(384, 256, 32, 32, "wall.png", "still", "wall"))
    
        chestlayout[1] = Item(32, 160, 32, 32, "smallTreasure", "yellow.png")
        layouts[1].append(Obstacle(0, 192, 32, 32, "wall.png", "still", "wall"))
        layouts[1].append(Obstacle(0, 224, 32, 32, "wall.png", "still", "wall"))
        layouts[1].append(Obstacle(0, 256, 32, 32, "wall.png", "still", "wall"))
        layouts[1].append(Obstacle(32, 192, 32, 32, "wall.png", "still", "wall"))
        layouts[1].append(Obstacle(32, 224, 32, 32, "wall.png", "still", "wall"))
        layouts[1].append(Obstacle(32, 256, 32, 32, "wall.png", "still", "wall"))
        enemies[1]=(Obstacle(20, 185, 40, 32, "greenaligo0.png", "movingenemy", "aligo"))
    
        layouts[1].append(Obstacle(480, 192, 32, 32, "wall.png", "still", "wall"))
        layouts[1].append(Obstacle(480, 224, 32, 32, "wall.png", "still", "wall"))
        layouts[1].append(Obstacle(480, 256, 32, 32, "wall.png", "still", "wall"))
        layouts[1].append(Obstacle(448, 192, 32, 32, "wall.png", "still", "wall"))
        layouts[1].append(Obstacle(448, 224, 32, 32, "wall.png", "still", "wall"))
        layouts[1].append(Obstacle(448, 256, 32, 32, "wall.png", "still", "wall"))
    
        chestlayout[2] = Item(256, 128, 32, 32, "smallTreasure", "yellow.png")
        layouts[2].append(Obstacle(0, 192, 32, 32, "wall.png", "still", "wall"))
        layouts[2].append(Obstacle(0, 224, 32, 32, "wall.png", "still", "wall"))
        layouts[2].append(Obstacle(0, 256, 32, 32, "wall.png", "still", "wall"))
        layouts[2].append(Obstacle(480, 192, 32, 32, "wall.png", "still", "wall"))
        layouts[2].append(Obstacle(480, 224, 32, 32, "wall.png", "still", "wall"))
        layouts[2].append(Obstacle(480, 256, 32, 32, "wall.png", "still", "wall"))
        enemies[2]=(Obstacle(390, 248, 40, 32, "greenaligo0.png", "movingenemy", "aligo"))
    
        layouts[2].append(Obstacle(256, 160, 32, 32, "wall.png", "still", "wall"))
        layouts[2].append(Obstacle(256, 192, 32, 32, "wall.png", "still", "wall"))
        layouts[2].append(Obstacle(256, 224, 32, 32, "wall.png", "still", "wall"))
        layouts[2].append(Obstacle(288, 160, 32, 32, "wall.png", "still", "wall"))
        layouts[2].append(Obstacle(288, 192, 32, 32, "wall.png", "still", "wall"))
        layouts[2].append(Obstacle(288, 224, 32, 32, "wall.png", "still", "wall"))
    
        chestlayout[3] = Item(128, 192, 32, 32, "smallTreasure", "yellow.png")
        layouts[3].append(Obstacle(256, 32, 32, 32, "wall.png", "still", "wall"))
        layouts[3].append(Obstacle(256, 0, 32, 32, "wall.png", "still", "wall"))
        layouts[3].append(Obstacle(224, 32, 32, 32, "wall.png", "still", "wall")) 
        layouts[3].append(Obstacle(224, 0, 32, 32, "wall.png", "still", "wall")) 
        enemies[3]=(Obstacle(210, 0, 40, 32, "greenaligo0.png", "movingenemy", "aligo")) 
    
        layouts[3].append(Obstacle(96, 256, 32, 32, "wall.png", "still", "wall")) 
        layouts[3].append(Obstacle(96, 224, 32, 32, "wall.png", "still", "wall")) 
        layouts[3].append(Obstacle(128, 256, 32, 32, "wall.png", "still", "wall")) 
        layouts[3].append(Obstacle(128, 224, 32, 32, "wall.png", "still", "wall")) 
    
        layouts[3].append(Obstacle(384, 256, 32, 32, "wall.png", "still", "wall")) 
        layouts[3].append(Obstacle(384, 224, 32, 32, "wall.png", "still", "wall")) 
        layouts[3].append(Obstacle(352, 256, 32, 32, "wall.png", "still", "wall")) 
        layouts[3].append(Obstacle(352, 224, 32, 32, "wall.png", "still", "wall")) 
        
        layouts[4].append(Obstacle(0, 0, 32, 32, "wall.png", "still", "wall")) 
        layouts[4].append(Obstacle(32, 0, 32, 32, "wall.png", "still", "wall")) 
        layouts[4].append(Obstacle(0, 32, 32, 32, "wall.png", "still", "wall")) 
        layouts[4].append(Obstacle(32, 32, 32, 32, "wall.png", "still", "wall")) 
    
        number = -1 
        prev = -1 
        for j in range(0,7):
            number = random.randint(0,3)
            treasures.append(Item(chestlayout[number].x, chestlayout[number].y + 448 * j + 640, chestlayout[number].width, chestlayout[number].height, "smallTreasure", "yellow.png")) 
            for i in layouts[number]:
                obstacles.append(Obstacle(i.x, i.y + 448 * j + 640, i.width, i.height, "wall.png", "still", "wall")) 
                obstacles.append(Obstacle(enemies[number].x, enemies[number].y + 448 * j + 640, enemies[number].width, enemies[number].height, enemies[number].src, enemies[number].movetype, enemies[number].type)) 
        treasures.append(Item(128, background.height - 416, 32, 32, "smallTreasure", "yellow.png")) 
        obstacles.append(Obstacle(384, (background.height - 192), 32, 32, "wall.png", "still", "wall")) 
        obstacles.append(Obstacle(384, (background.height - 224), 32, 32, "wall.png", "still", "wall")) 
        obstacles.append(Obstacle(384, (background.height - 256), 32, 32, "wall.png", "still", "wall")) 
        obstacles.append(Obstacle(352, (background.height - 192), 32, 32, "wall.png", "still", "wall")) 
        obstacles.append(Obstacle(352, (background.height - 224), 32, 32, "wall.png", "still", "wall")) 
        obstacles.append(Obstacle(352, (background.height - 256), 32, 32, "wall.png", "still", "wall")) 
    
        obstacles.append(Obstacle(352, (background.height - 64), 32, 32, "red.png", "still", "urchon")) 
        obstacles.append(Obstacle(128, (background.height - 64), 32, 32, "red.png", "still", "urchon")) 
    
        obstacles.append(Obstacle(96, (background.height - 320), 32, 32, "wall.png", "still", "wall")) 
        obstacles.append(Obstacle(96, (background.height - 352), 32, 32, "wall.png", "still", "wall")) 
        obstacles.append(Obstacle(96, (background.height - 384), 32, 32, "wall.png", "still", "wall")) 
        obstacles.append(Obstacle(128, (background.height - 320), 32, 32, "wall.png", "still", "wall")) 
        obstacles.append(Obstacle(128, (background.height - 352), 32, 32, "wall.png", "still", "wall")) 
        obstacles.append(Obstacle(128, (background.height - 384), 32, 32, "wall.png", "still", "wall")) 
        
        obstacles.append(Obstacle(210, (background.height-200), 40, 32, "greenaligo0.png", "movingenemy", "aligo")) 
        obstacles.append(Obstacle(210, (background.height-300), 40, 32, "turtle0.png", "movingenemy", "turtle")) 
    
        for i in range(0,16):
            obstacles.append(Obstacle(i * 32, (background.height - 32), 32, 32, "wall.png", "still", "wall")) 
            treasures.append(Item(224, (background.height - 96), 64, 64, "bigTreasure", "yellow.png")) 
