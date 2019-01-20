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
ui = character(512, 0, 240, 480, "ui.png", "blank")
collectedTreasure = []
bigChest = character(580, 170, 64, 64, "transparent.png", "blank")
maptype = ''
collectedTreasures = 0
totaltreasures = 0
gameStatus = "start"
treasures = []
enemiesHit = []
collectedGem = []
gems = []
collectedGems = 0

camx = 0
camy = 0
Camera = camera(0, 0)

button1 = False


def move():
    tora.move(framewidth, frameheight)
    for i in obstacles:
        i.move()


def update():
    global totaltreasures
    background.update(frameheight, framewidth, animationcounter, weapon)
    if Camera.movement != "stop":
        for i in obstacles:
            i.update(tora, Camera, obstacles, weapon, animationcounter, enemiesHit)

    for i in treasures:
        totaltreasures = i.update(tora, Camera, treasures, collectedTreasure, collectedTreasures, bigChest)
    tora.update(frameheight, framewidth, animationcounter, weapon)

    for i in gems:
        i.update(tora, Camera, gems, collectedGem, collectedGems, bigChest)


def paint():
    translate(0, 0)
    translate(-Camera.x, -Camera.y)
    background.paint()
    for i in obstacles:
        i.paint()
    for i in treasures:
        i.paint()
    for i in gems:
        i.paint()
    translate(Camera.x, Camera.y)
    tora.paint()
    weapon.paint()
    ui.paint()
    for i in collectedTreasure:
        i.paint()
    bigChest.paint()
    noStroke()
    fill(10, 225, 255)
    if tora.health >= 0:
        rect(540, 122, tora.health*19, 23)
    text('Score:', 520, 70)
    text(len(collectedGem*100)+len(enemiesHit)*50, 520, 100)


def setup():
    frameRate(30)
    tora.setup()
    weapon.setup()
    background.setup()
    ui.setup()
    bigChest.setup()
    for i in obstacles:
        i.setup()
    for i in treasures:
        i.setup()
    for i in gems:
        i.setup()
    size(framewidth, frameheight)
    noSmooth()


def main():
    finalwidth = framewidth
    finalheight = frameheight
    maptype = "default"
    Map.createMap(Map(), obstacles, treasures, gems, background)
main()


def draw():
    global totaltreasures
    global button1
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
    if gameStatus == "start":
        if button1 and gameStatus == "start":
            gameStatus = "starting"
        else:
            textSize(100)
            fill(0)
            rect(0, 0, 752, 480)
            fill(204, 0, 0)
            text("Diving", 120, 100)
            fill(153, 255, 0)
            text("Game!", 300, 215)
            textSize(24)
            fill(255)
            text('Play', 320, 340)
            text('Credit  1', 10, 470)
            if mousePressed and mouseButton == LEFT:
                if mouseX > x and mouseX < x+w and mouseY > y and mouseY < y+h:
                    button1 = True
                    print("button1")

    if gameStatus == "starting" or gameStatus == "playing" or gameStatus == "done":
        animationcounter += 1
        if animationcounter == 20:
            animationcounter = 0
        move()
        tora.up = True
        tora.down = True
        tora.left = True
        tora.right = True
        update()
        gameStatus = Camera.update(background, frameheight, tora, gameStatus)
        paint()
    if gameStatus == "won":
        fill(0)
        rect(0, 0, 752, 480)
        textSize(100)
        fill(204, 0, 0)
        text("STAGE", 30, 100)
        fill(153, 255, 0)
        text("CLEAR", 400, 100)

        textSize(24)

        fill(255, 255, 255)
        text("Score : " + str(len(collectedGem)*100+len(enemiesHit)*50), 340, 200)
        text(str(totaltreasures) + "/8 extra treasures", 250, 290)
    if gameStatus == "lost":
        textSize(100)
        fill(0)
        rect(0, 0, 752, 480)
        fill(204, 0, 0)
        text("GAME", 30, 100)
        fill(153, 255, 0)
        text("OVER", 400, 100)
        textSize(24)
        fill(255, 255, 255)
        text("Score : " + str(len(collectedGem)*100+len(enemiesHit)*50), 340, 200)
        text(str(totaltreasures) + "/8 treasures", 250, 290)


def keyPressed():
    character.keyPressed(tora, Camera, weapon)


def keyReleased():
    character.keyReleased(tora)
