upimages = []
downimages = []
leftimages = []
rightimages = []
transparent = loadImage("transparent.png")


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
    currentimage = ""

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
        if self.type == "character":
            global transparent
            upimages.append(loadImage("toraup1.png"))
            upimages.append(loadImage("toraup2.png"))
            upimages.append(loadImage("toraupattack1.png"))
            upimages.append(loadImage("toraupattack2.png"))
            upimages.append(loadImage("upattack.png"))

            downimages.append(loadImage("toradown1.png"))
            downimages.append(loadImage("toradown2.png"))
            downimages.append(loadImage("toradownattack1.png"))
            downimages.append(loadImage("toradownattack2.png"))
            downimages.append(loadImage("downattack.png"))

            leftimages.append(loadImage("toraleft1.png"))
            leftimages.append(loadImage("toraleft2.png"))
            leftimages.append(loadImage("toraleftattack1.png"))
            leftimages.append(loadImage("toraleftattack2.png"))
            leftimages.append(loadImage("leftattack.png"))

            rightimages.append(loadImage("toraright1.png"))
            rightimages.append(loadImage("toraright2.png"))
            rightimages.append(loadImage("torarightattack1.png"))
            rightimages.append(loadImage("torarightattack2.png"))
            rightimages.append(loadImage("rightattack.png"))

            transparent = loadImage("transparent.png")
        self.currentimage = loadImage(self.src)

    def move(self, framewidth, frameheight):
        if (self.x - 2 >= 0 and self.speedX < 0) or (self.x + self.width + 2 <= 512 and self.speedX > 0):
            if (self.left is True and self.xdir == "left") or (self.right is True and self.xdir == "right"):
                self.x += self.speedX
        if (self.y - 2 >= 0 and self.speedY < 0) or (self.y + self.height + 2 <= frameheight and self.speedY > 0):
            if (self.up is True and self.ydir == "up") or (self.down is True and self.ydir == "down"):
                self.y += self.speedY

    def animate(self, animationcounter, weapon):
        if (self.type == "character"):
            if (self.invincible % 10 > 5):
                self.currentimage = transparent
            elif (weapon.attack is True):
                if (self.attackDir == "up"):
                    if (animationcounter <= 10):
                        self.currentimage = upimages[2]
                    elif (animationcounter <= 20):
                        self.currentimage = upimages[3]

                elif (self.attackDir == "down"):
                    if (animationcounter <= 10):
                        self.currentimage = downimages[2]
                    elif (animationcounter <= 20):
                        self.currentimage = downimages[3]

                elif (self.attackDir == "left"):
                    if (animationcounter <= 10):
                        self.currentimage = leftimages[2]
                    elif (animationcounter <= 20):
                        self.currentimage = leftimages[3]

                elif (self.attackDir == "right"):
                    if (animationcounter <= 10):
                        self.currentimage = rightimages[2]
                    elif (animationcounter <= 20):
                        self.currentimage = rightimages[3]

            elif (len(self.directionqueue) > 0):
                if (self.directionqueue[0] == "up"):
                    if (animationcounter <= 10):
                        self.currentimage = upimages[0]
                    elif (animationcounter <= 20):
                        self.currentimage = upimages[1]

                elif (self.directionqueue[0] == "down"):
                    if (animationcounter <= 10):
                        self.currentimage = downimages[0]
                    elif (animationcounter <= 20):
                        self.currentimage = downimages[1]

                elif (self.directionqueue[0] == "left"):
                    if (animationcounter <= 10):
                        self.currentimage = leftimages[0]
                    elif (animationcounter <= 20):
                        self.currentimage = leftimages[1]

                elif (self.directionqueue[0] == "right"):
                    if (animationcounter <= 10):
                        self.currentimage = rightimages[0]
                    elif (animationcounter <= 20):
                        self.currentimage = rightimages[1]

            else:
                if (self.lastDir == "up"):
                    if (animationcounter <= 10):
                        self.currentimage = upimages[0]
                    elif (animationcounter <= 20):
                        self.currentimage = upimages[1]

                elif (self.lastDir == "down"):
                    if (animationcounter <= 10):
                        self.currentimage = downimages[0]
                    elif (animationcounter <= 20):
                        self.currentimage = downimages[1]

                elif (self.lastDir == "left"):
                    if (animationcounter <= 10):
                        self.currentimage = leftimages[0]
                    elif (animationcounter <= 20):
                        self.currentimage = leftimages[1]

                elif (self.lastDir == "right"):
                    if (animationcounter <= 10):
                        self.currentimage = rightimages[0]
                    elif (animationcounter <= 20):
                        self.currentimage = rightimages[1]

    def loseHealth(self, healthAmount, invincibleAmount):
        if (self.invincible == 0):
            self.health -= healthAmount
            self.invincible += invincibleAmount
            return

    def update(self, frameheight, framewidth, animationcounter, weapon):
        if (self.invincible > 0):
            self.invincible -= 1
        if (weapon.attack is True):
            self.attackcounter += self.attackposition
            if (self.attackcounter == 15):
                self.attackposition = -1

            if (self.attackDir == "up"):
                weapon.y = self.y - self.attackcounter * 10
                weapon.x = self.x + self.width / 2 - weapon.width / 2

            if (self.attackDir == "down"):
                weapon.y = self.y + self.attackcounter * 10
                weapon.x = self.x + self.width / 2 - weapon.width / 2

            if (self.attackDir == "left"):
                weapon.x = self.x - self.attackcounter * 10
                weapon.y = self.y + self.height / 2 - weapon.height / 2

            if (self.attackDir == "right"):
                weapon.x = self.x + self.attackcounter * 10
                weapon.y = self.y + self.height / 2 - weapon.height / 2

            if ((self.attackDir == "up" or self.attackDir == "down") and weapon.y == self.y) or ((self.attackDir == "left" or self.attackDir == "right") and weapon.x == self.x):
                weapon.attack = False
                self.attackcounter = 0
                self.attackposition = 1
                weapon.currentimage = transparent
        else:
            weapon.y = self.y
            weapon.x = self.x

        if (self.y + self.height > frameheight):
            self.y = frameheight - self.height
        if (self.y < 0 and self.moving is True):
            self.y = 0

        if (len(self.horizontalqueue) == 0 or self.moving is False):
            self.speedX = 0
        elif (self.horizontalqueue[0] == "left"):
            self.speedX = -3
        elif (self.horizontalqueue[0] == "right"):
            self.speedX = 3

        if (len(self.verticalqueue) == 0 or self.moving is False):
            self.speedY = 0
        elif (self.verticalqueue[0] == "up"):
            self.speedY = -3
        elif (self.verticalqueue[0] == "down"):
            self.speedY = 3

        self.animate(animationcounter, weapon)

        if ((self.speedX == 0 and self.speedY == 0) or (self.counter == 22)):
            self.counter = 0
        else:
            self.counter += 1

    def paint(self):
        image(self.currentimage, self.x, self.y, self.width, self.height)

    def keyReleased(self):
        if (key == 'a'):
            try:
                self.xkey = False
                self.directionqueue.remove("left")
                self.horizontalqueue.remove("left")
                self.leftpressed = False
                self.lastDir = "left"
            except:
                pass

        if (key == 'd'):
            try:
                self.xkey = False
                self.directionqueue.remove("right")
                self.horizontalqueue.remove("right")
                self.rightpressed = False
                self.lastDir = "right"
            except:
                pass

        if (key == 'w'):
            try:
                self.ykey = False
                self.directionqueue.remove("up")
                self.verticalqueue.remove("up")
                self.uppressed = False
                self.lastDir = "up"
            except:
                pass

        if (key == 's'):
            try:
                self.ykey = False
                self.directionqueue.remove("down")
                self.verticalqueue.remove("down")
                self.downpressed = False
                self.lastDir = "down"
            except:
                pass

    def keyPressed(self, camera, weapon):
        if (self.moving is True):
            if (key == 'a' and self.left is True and self.leftpressed is False):
                self.directionqueue.insert(0, "left")
                self.horizontalqueue.insert(0, "left")
                self.xkey = True
                self.xdir = "left"
                self.leftpressed = True

            if (key == 'd' and self.right is True and self.rightpressed is False):
                self.directionqueue.insert(0, "right")
                self.horizontalqueue.insert(0, "right")
                self.xkey = True
                self.xdir = "right"
                self.rightpressed = True

            if (key == 'w' and self.up is True and self.uppressed is False):
                self.directionqueue.insert(0, "up")
                self.verticalqueue.insert(0, "up")
                self.ykey = True
                self.ydir = "up"
                self.uppressed = True

            if (key == 's' and self.down is True and self.downpressed is False):
                self.directionqueue.insert(0, "down")
                self.verticalqueue.insert(0, "down")
                self.ykey = True
                self.ydir = "down"
                self.downpressed = True

            if (camera.movement == "down" and key == ' ' and weapon.attack is False):
                weapon.attack = True
                if (len(self.directionqueue) > 0):
                    self.attackDir = self.directionqueue[0]
                else:
                    self.attackDir = self.lastDir
                if(self.attackDir == "up"):
                    weapon.currentimage = upimages[4]
                elif(self.attackDir == "down"):
                    weapon.currentimage = downimages[4]
                elif(self.attackDir == "left"):
                    weapon.currentimage = leftimages[4]
                elif(self.attackDir == "right"):
                    weapon.currentimage = rightimages[4]
