from camera import *
from character import *
from item import *
from map import *
from obstacle import *
frameheight = 480
obstacles = []
animationcounter = 0
framewidth = 512 + 240
frameheight = 480
background = character(0, 0, 512, 4192, "background.png", "blank")
tora = character(100, 30, 32, 32, "tora1.png", "character")
weapon = character(0, 0, 10, 10, "", "weapon")
ui = character(512, 0, 240, 480, "red.png", "blank")
collectedTreasure = []
bigChest = character(600, 200, 64, 64, "", "blank")
maptype = ''
collectedTreasures = 0
gameStatus = "playing"

treasures = []

sounds = []
#Clip bgm
camx = 0
camy = 0
Camera = camera(0, 0)

def move():
    tora.move(framewidth, frameheight)
    #for i in obstacles:
    #    i.move()
    
def update():
    background.update(frameheight, framewidth)
    #if Camera.movement != "stop":
    #    for i in obstacles: 
    #        obstacles.get(i).update()
    #        
    #for i in treasures:
    #    treasures.get(i).update()
    tora.update(frameheight, framewidth)
    
def paint():
    translate(0, 0)
    translate(-Camera.x, -Camera.y)
    background.paint()
    #for i in obstacles:
    #    i.paint()
    #for i in treasures:
    #    i.paint()
    translate(Camera.x, Camera.y)
    tora.paint()
    ui.paint()
    #for i in collectedTreasure:
    #    i.paint()
    #bigChest.paint()
    fill(255,255,255)
    rect(600, 50, tora.health*10,10)
    fill(0,0,0)
    rect(600+tora.health*10,50,(10-tora.health)*10,10)
    #print("kk")
    
def setup():
    tora.setup()
    background.setup()
    ui.setup()
    size(framewidth,frameheight)
    #size(900,900)
    
def main(): 
    finalwidth = framewidth
    finalheight = frameheight
    maptype = "default"
    Map.createMap(Map(),obstacles,treasures,background)
main()
    
def draw():
    clear()
    if gameStatus == "playing":
        move()
        tora.up = True
        tora.down = True
        tora.left = True
        tora.right = True
        update()
        Camera.update()
        paint()
def keyPressed():
    character.keyPressed(tora)
def keyReleased():
    character.keyReleased(tora)
