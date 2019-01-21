from obstacle import *
from item import *
import random


class Map(object):
    def createMap(self, obstacles, treasures, gems, background):
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

        gems.append(Item(160, 256, 28, 28, "gems", "gem.png"))
        gems.append(Item(64, 256, 28, 28, "gems", "gem.png"))

        gems.append(Item(416, 256, 28, 28, "gems", "gem.png"))
        gems.append(Item(320, 256, 28, 28, "gems", "gem.png"))

        gems.append(Item(192, 470, 28, 28, "gems", "gem.png"))
        gems.append(Item(288, 470, 28, 28, "gems", "gem.png"))

        obstacles.append(Obstacle(40, 350, 64, 32, "greenaligo0.png", "movingenemy", "aligo"))

        layouts = [None] * 5
        chestlayout = [None] * 5
        gemlayout = [None] * 5
        enemies = [None] * 5
        for i in range(len(layouts)):
            layouts[i] = []
            enemies[i] = []
            gemlayout[i] = []

        chestlayout[0] = Item(192, -32, 32, 32, "smallTreasure", "yellow.png")
        gemlayout[0].append(Item(288, 0, 28, 28, "gems", "gem.png"))
        gemlayout[0].append(Item(352, 0, 28, 28, "gems", "gem.png"))
        gemlayout[0].append(Item(64, 0, 28, 28, "gems", "gem.png"))
        gemlayout[0].append(Item(128, 0, 28, 28, "gems", "gem.png"))
        gemlayout[0].append(Item(300, 192, 28, 28, "gems", "gem.png"))
        layouts[0].append(Obstacle(192, 0, 32, 32, "wall.png", "still", "wall"))
        layouts[0].append(Obstacle(192, 32, 32, 32, "wall.png", "still", "wall"))
        layouts[0].append(Obstacle(224, 0, 32, 32, "wall.png", "still", "wall"))
        layouts[0].append(Obstacle(224, 32, 32, 32, "wall.png", "still", "wall"))

        enemies[0].append(Obstacle(150, 30, 64, 32, "turtle0.png", "movingenemy", "turtle"))
        enemies[0].append(Obstacle(200, 192, 32, 32, "urchin.png", "still", "urchon"))
        enemies[0].append(Obstacle(300, 30, 64, 32, "turtle0.png", "movingenemy", "turtle"))
        enemies[0].append(Obstacle(200, 256, 64, 32, "greenaligo0.png", "movingenemy", "aligo"))

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
        gemlayout[1].append(Item(32, 0, 28, 28, "gems", "gem.png"))
        gemlayout[1].append(Item(128, 0, 28, 28, "gems", "gem.png"))
        gemlayout[1].append(Item(448, 0, 28, 28, "gems", "gem.png"))
        gemlayout[1].append(Item(352, 0, 28, 28, "gems", "gem.png"))
        layouts[1].append(Obstacle(0, 192, 32, 32, "wall.png", "still", "wall"))
        layouts[1].append(Obstacle(0, 224, 32, 32, "wall.png", "still", "wall"))
        layouts[1].append(Obstacle(0, 256, 32, 32, "wall.png", "still", "wall"))
        layouts[1].append(Obstacle(32, 192, 32, 32, "wall.png", "still", "wall"))
        layouts[1].append(Obstacle(32, 224, 32, 32, "wall.png", "still", "wall"))
        layouts[1].append(Obstacle(32, 256, 32, 32, "wall.png", "still", "wall"))

        enemies[1].append(Obstacle(400, 185, 64, 32, "greenaligo0.png", "movingenemy", "aligo"))
        enemies[1].append(Obstacle(200, 50, 64, 32, "turtle0.png", "movingenemy", "turtle"))
        enemies[1].append(Obstacle(20, -64, 64, 32, "greenaligo0.png", "movingenemy", "aligo"))
        enemies[1].append(Obstacle(240, 0, 32, 32, "urchin.png", "still", "urchon"))

        layouts[1].append(Obstacle(480, 192, 32, 32, "wall.png", "still", "wall"))
        layouts[1].append(Obstacle(480, 224, 32, 32, "wall.png", "still", "wall"))
        layouts[1].append(Obstacle(480, 256, 32, 32, "wall.png", "still", "wall"))
        layouts[1].append(Obstacle(448, 192, 32, 32, "wall.png", "still", "wall"))
        layouts[1].append(Obstacle(448, 224, 32, 32, "wall.png", "still", "wall"))
        layouts[1].append(Obstacle(448, 256, 32, 32, "wall.png", "still", "wall"))

        chestlayout[2] = Item(256, 128, 32, 32, "smallTreasure", "yellow.png")
        gemlayout[2].append(Item(352, 160, 28, 28, "gems", "gem.png"))
        gemlayout[2].append(Item(416, 160, 28, 28, "gems", "gem.png"))
        gemlayout[2].append(Item(96, 176, 28, 28, "gems", "gem.png"))
        gemlayout[2].append(Item(192, 176, 28, 28, "gems", "gem.png"))
        layouts[2].append(Obstacle(0, 192, 32, 32, "wall.png", "still", "wall"))
        layouts[2].append(Obstacle(0, 224, 32, 32, "wall.png", "still", "wall"))
        layouts[2].append(Obstacle(0, 256, 32, 32, "wall.png", "still", "wall"))
        layouts[2].append(Obstacle(480, 192, 32, 32, "wall.png", "still", "wall"))
        layouts[2].append(Obstacle(480, 224, 32, 32, "wall.png", "still", "wall"))
        layouts[2].append(Obstacle(480, 256, 32, 32, "wall.png", "still", "wall"))

        enemies[2].append(Obstacle(200, 248, 64, 32, "greenaligo0.png", "movingenemy", "aligo"))
        enemies[2].append(Obstacle(200, 0, 64, 32, "turtle0.png", "movingenemy", "turtle"))
        enemies[2].append(Obstacle(384, 224, 32, 32, "urchin.png", "still", "urchon"))

        layouts[2].append(Obstacle(256, 160, 32, 32, "wall.png", "still", "wall"))
        layouts[2].append(Obstacle(256, 192, 32, 32, "wall.png", "still", "wall"))
        layouts[2].append(Obstacle(256, 224, 32, 32, "wall.png", "still", "wall"))
        layouts[2].append(Obstacle(288, 160, 32, 32, "wall.png", "still", "wall"))
        layouts[2].append(Obstacle(288, 192, 32, 32, "wall.png", "still", "wall"))
        layouts[2].append(Obstacle(288, 224, 32, 32, "wall.png", "still", "wall"))

        chestlayout[3] = Item(128, 192, 32, 32, "smallTreasure", "yellow.png")
        gemlayout[3].append(Item(64, 128, 28, 28, "gems", "gem.png"))
        gemlayout[3].append(Item(114, 128, 28, 28, "gems", "gem.png"))
        gemlayout[3].append(Item(320, 128, 28, 28, "gems", "gem.png"))
        gemlayout[3].append(Item(384, 128, 28, 28, "gems", "gem.png"))
        layouts[3].append(Obstacle(256, 32, 32, 32, "wall.png", "still", "wall"))
        layouts[3].append(Obstacle(256, 0, 32, 32, "wall.png", "still", "wall"))
        layouts[3].append(Obstacle(224, 32, 32, 32, "wall.png", "still", "wall"))
        layouts[3].append(Obstacle(224, 0, 32, 32, "wall.png", "still", "wall")) 

        enemies[3].append(Obstacle(210, 0, 64, 32, "greenaligo0.png", "movingenemy", "aligo"))
        enemies[3].append(Obstacle(310, 0, 64, 32, "greenaligo0.png", "movingenemy", "aligo"))
        enemies[3].append(Obstacle(128, 64, 32, 32, "urchin.png", "still", "urchon"))
        enemies[3].append(Obstacle(352, 64, 32, 32, "urchin.png", "still", "urchon"))
        enemies[3].append(Obstacle(256, 256, 32, 32, "urchin.png", "still", "urchon"))

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
        layouts[4].append(Obstacle(64, 0, 32, 32, "wall.png", "still", "wall")) 
        layouts[4].append(Obstacle(0, 32, 32, 32, "wall.png", "still", "wall")) 
        layouts[4].append(Obstacle(32, 32, 32, 32, "wall.png", "still", "wall")) 
        layouts[4].append(Obstacle(64, 32, 32, 32, "wall.png", "still", "wall")) 
        chestlayout[4] = Item(32, -32, 32, 32, "smallTreasure", "yellow.png")

        gemlayout[4].append(Item(32, 100, 28, 28, "gems", "gem.png"))
        gemlayout[4].append(Item(128, 100, 28, 28, "gems", "gem.png"))
        gemlayout[4].append(Item(448, 100, 28, 28, "gems", "gem.png"))
        gemlayout[4].append(Item(352, 100, 28, 28, "gems", "gem.png"))

        enemies[4].append(Obstacle(210, 0, 64, 32, "greenaligo0,png", "movingenemy", "aligo"))
        enemies[4].append(Obstacle(400, 185, 64, 32, "greenaligo0.png", "movingenemy", "aligo"))
        enemies[4].append(Obstacle(300, 50, 64, 32, "turtle0.png", "movingenemy", "turtle"))
        enemies[4].append(Obstacle(240, 250, 32, 32, "urchin.png", "still", "urchon"))

        number = -1 
        prev = -1 
        for j in range(0, 7):
            number = random.randint(0, 4)
            treasures.append(Item(chestlayout[number].x, chestlayout[number].y + 448 * j + 640, chestlayout[number].width, chestlayout[number].height, "smallTreasure", "yellow.png")) 
            for i in layouts[number]:
                obstacles.append(Obstacle(i.x, i.y + 448 * j + 640, i.width, i.height, "wall.png", "still", "wall")) 
            for i in enemies[number]:
                obstacles.append(Obstacle(i.x, i.y + 448 * j + 640, i.width, i.height, i.src, i.movetype, i.type))
            for i in gemlayout[number]:
                gems.append(Item(i.x, i.y + 448 * j + 640, i.width, i.height, "gems", "gem.png"))

        treasures.append(Item(128, background.height - 416, 32, 32, "smallTreasure", "yellow.png")) 
        obstacles.append(Obstacle(384, (background.height - 192), 32, 32, "wall.png", "still", "wall")) 
        obstacles.append(Obstacle(384, (background.height - 224), 32, 32, "wall.png", "still", "wall")) 
        obstacles.append(Obstacle(384, (background.height - 256), 32, 32, "wall.png", "still", "wall")) 
        obstacles.append(Obstacle(352, (background.height - 192), 32, 32, "wall.png", "still", "wall")) 
        obstacles.append(Obstacle(352, (background.height - 224), 32, 32, "wall.png", "still", "wall")) 
        obstacles.append(Obstacle(352, (background.height - 256), 32, 32, "wall.png", "still", "wall")) 

        obstacles.append(Obstacle(352, (background.height - 64), 32, 32, "urchin.png", "still", "urchon")) 
        obstacles.append(Obstacle(128, (background.height - 64), 32, 32, "urchin.png", "still", "urchon")) 

        obstacles.append(Obstacle(96, (background.height - 320), 32, 32, "wall.png", "still", "wall")) 
        obstacles.append(Obstacle(96, (background.height - 352), 32, 32, "wall.png", "still", "wall")) 
        obstacles.append(Obstacle(96, (background.height - 384), 32, 32, "wall.png", "still", "wall")) 
        obstacles.append(Obstacle(128, (background.height - 320), 32, 32, "wall.png", "still", "wall")) 
        obstacles.append(Obstacle(128, (background.height - 352), 32, 32, "wall.png", "still", "wall")) 
        obstacles.append(Obstacle(128, (background.height - 384), 32, 32, "wall.png", "still", "wall")) 

        obstacles.append(Obstacle(210, (background.height-200), 64, 32, "greenaligo0.png", "movingenemy", "aligo")) 
        obstacles.append(Obstacle(210, (background.height-350), 64, 32, "turtle0.png", "movingenemy", "turtle")) 

        for i in range(0, 16):
            obstacles.append(Obstacle(i * 32, (background.height - 32), 32, 32, "wall.png", "still", "wall")) 
        treasures.append(Item(224, (background.height - 96), 64, 64, "bigTreasure", "yellow.png"))
