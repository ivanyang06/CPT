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
weapon = character(0, 0, 10, 10, "transparent.png", "weapon")
ui = character(512, 0, 240, 480, "red.png", "blank")
collectedTreasure = []
bigChest = character(600, 200, 64, 64, "", "blank")
maptype = ''
collectedTreasures = 0
gameStatus = "start"

treasures = []

sounds = []
#Clip bgm
camx = 0
camy = 0
Camera = camera(0, 0)




button1 = False
button2 = False


def move():
    tora.move(framewidth, frameheight)
    for i in obstacles:
        i.move()
    
def update():
    background.update(frameheight, framewidth, animationcounter, weapon)
    if Camera.movement != "stop":
        for i in obstacles: 
            i.update(tora,Camera, obstacles, weapon)
            
    for i in treasures:
        i.update(tora,Camera,treasures, collectedTreasure, collectedTreasures, bigChest)
    tora.update(frameheight, framewidth, animationcounter, weapon)
    
def paint():
    translate(0, 0)
    translate(-Camera.x, -Camera.y)
    background.paint()
    for i in obstacles:
        i.paint()
    for i in treasures:
        i.paint()
    translate(Camera.x, Camera.y)
    tora.paint()
    weapon.paint()
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
    frameRate(30);
    tora.setup()
    weapon.setup()
    background.setup()
    ui.setup()
    for i in obstacles:
        i.setup()
    for i in treasures:
        i.setup()
    size(framewidth,frameheight)
    noSmooth()
    #size(900,900)
    
def main(): 
    finalwidth = framewidth
    finalheight = frameheight
    maptype = "default"
    Map.createMap(Map(),obstacles,treasures,background)
main()
    
def draw():
    global button1
    global button2
    global animationcounter
    x = 300
    y = 300 
    w = 120
    h = 60
    a = 300
    b = 350
    c = 120
    d = 60
    global gameStatus
    clear()
    if gameStatus == "start":
        if button1 and gameStatus == "start":
            gameStatus = "playing"
        elif button2 and gameStatus == "start":
            gameStatus = "playing"
        else:
            textSize(100)
            fill(204,0,0)
            text("Diving", 120, 100)
            fill(153,255,0)
            text("Game!", 300, 215)
            textSize(24)
            fill(255)
            text('Normal', 320, 340)
            fill(255)
            text('Easy', 320, 400)
            fill(255)
            text('Credit  1', 10,470)
            if mousePressed and mouseButton == LEFT:
                if mouseX > x and mouseX < x+w and mouseY > y and mouseY < y+h:
                    button1 = True
                    print("button1")
    
            if mousePressed and mouseButton == LEFT:
                if mouseX > a and mouseX < a+c and mouseY > b and mouseY < b+d:
                    button2 = True
                    print("button2")
        
    if gameStatus == "playing" or gameStatus == "done":
        animationcounter += 1
        if animationcounter == 20:
            animationcounter = 0
        move()
        tora.up = True
        tora.down = True
        tora.left = True
        tora.right = True
        update()
        gameStatus = Camera.update(background, frameheight, tora,gameStatus)
        paint()
    if gameStatus == "won":
        score1 = 100000
        score2 = 121020
        textSize(100)
        fill(204,0,0)
        text("STAGE", 30, 100)
        fill(153,255,0)
        text("CLEAR", 400, 100)
    
        textSize(24)
   
        fill(255,255,255)
        text("Score : " + str(score1), 340,200) 
        fill(255,255,255)
        text("Coins : " + str(score2), 340,240) 
        fill(255,255,255)
        text("Treasure Complete", 250,290) 
    if gameStatus == "lost":
        score1 = 100000
        score2 = 121020
        textSize(100)
        fill(204,0,0)
        text("GAME", 30, 100)
        fill(153,255,0)
        text("OVER", 400, 100)
    
        textSize(24)
   
        fill(255,255,255)
        text("Score : " + str(score1), 340,200) 
        fill(255,255,255)
        text("Coins : " + str(score2), 340,240) 
        fill(255,255,255)
        text("Treasure Complete", 250,290) 

def keyPressed():
    character.keyPressed(tora, Camera, weapon)
def keyReleased():
    character.keyReleased(tora)
