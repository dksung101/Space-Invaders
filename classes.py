class SpaceShip:
    def __init__(self, x, y):
        self.x = x
        self.y = y 
        self.r = 10
        self.movingRight = False
        self.movingLeft = False
        self.movingUp = False
        self.movingDown = False
        
    def drawSpaceShip(self, canvas):
        canvas.create_rectangle(self.x-self.r, self.y-self.r, self.x+self.r, self.y+self.r, width = 3, fill = 'orange')
        
    def moveSpaceShip(self, app):
        if self.movingRight == True and self.x <= app.width-50:
            self.x+=5

        if self.movingLeft == True and self.x >= 50:
            self.x-=5
            
        if self.movingUp == True and self.y >= 50:
            self.y-=5
                
        if self.movingDown == True and self.y <= app.height-50:
            self.y+=5

class Laser:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.r = 10
        # self.laserSpeed = laserSpeed

class SpaceShipLaser(Laser):
    def __init__(self, x, y):
        super().__init__(x,y)
        self.laserSpeed = 10
        
    def moveLaser(self):
        # print(self.laserSpeed)
        self.y -= self.laserSpeed
    
    
    def checkHitAlien(self, alien):
        if (self.x-alien.x)**2+(self.y-alien.y)**2 < (self.r+alien.r)**2:
            return True
        return False
        # if (self.x >= alien.x-alien.r and self.x <= alien.x+alien.r 
        #     and self.y >= alien.y-alien.r and self.y <= alien.y+alien.r):
        #     return True
        # else:
        #     return False
    
    def checkHitAlienLaser(self, alienLaser):
        if (self.x-alienLaser.x)**2+(self.y-alienLaser.y)**2 < (self.r+alienLaser.r)**2:
            return True
        # if (self.x >= alienLaser.x-alienLaser.r and self.x <= alienLaser.x+alienLaser.r 
        #     and self.y >= alienLaser.y-alienLaser.r and self.y <= alienLaser.y+alienLaser.r):
        #     return True
        return False
        
    def drawLaser(self, canvas):
        canvas.create_oval(self.x - self.r, self.y - self.r, self.x + self.r, self.y + self.r, fill = 'blue')

class Item:
    def __init__(self, xPos, yPos):
        self.xPos = xPos
        self.yPos = yPos
        self.r = 10
        # self.typeOfItem = typeOfItem
        
    def moveItemDown(self):
        self.yPos += 5
        
    def checkHitSpaceShip(self, SpaceShip):
        if (self.xPos - SpaceShip.x)**2 + (self.yPos - SpaceShip.y)**2 < (self.r + SpaceShip.r)**2:
        # if (self.xPos >= SpaceShip.x-SpaceShip.r and self.xPos <= SpaceShip.x+SpaceShip.r 
        #     and self.yPos >= SpaceShip.y-SpaceShip.r and self.yPos <= SpaceShip.y+SpaceShip.r):
        #     return True
            return True
        return False
    
class bulletSpeedIncrease(Item):
    def __init__(self, xPos, yPos):
        super().__init__(xPos, yPos)
    
    def drawItem(self, canvas):
        canvas.create_oval(self.xPos-self.r, self.yPos-self.r, self.xPos+self.r, self.yPos+self.r, fill = "purple")

    def activatePower(self, app):
        # print("YUHs")
        for laser in app.SpaceShipLasers:
            laser.laserSpeed = 20
            
    def deactivatePower(self, app):
        for laser in app.SpaceShipLasers:
            laser.laserSpeed = 10
    
class bulletSpeedDecrease(Item):
    def __init__(self, xPos, yPos):
        super().__init__(xPos, yPos)
        
    def drawItem(self, canvas):
        canvas.create_oval(self.xPos-self.r, self.yPos-self.r, self.xPos+self.r, self.yPos+self.r, fill = "cyan")

    def activatePower(self, app):
        for laser in app.SpaceShipLasers:
            laser.laserSpeed = 5
            
    def deactivatePower(self, app):
        for laser in app.SpaceShipLasers:
            laser.laserSpeed = 10

class AlienLaser(Laser):
    def __init__(self, x, y):
        super().__init__(x, y)
        
    def moveLaser(self):
        self.y += 10
    
    def checkHitSpaceShip(self, SpaceShip):
        # if (SpaceShip.x - self.x)**2 + (SpaceShip.y - self.y)**2 < (SpaceShip.r + self.r)**2:
        #     return True
        if (self.x >= SpaceShip.x-SpaceShip.r and self.x <= SpaceShip.x+SpaceShip.r 
            and self.y >= SpaceShip.y-SpaceShip.r and self.y <= SpaceShip.y+SpaceShip.r):
            return True
        return False
        
    def drawLaser(self, canvas):
        canvas.create_oval(self.x - self.r, self.y - self.r, self.x + self.r, self.y + self.r, fill = 'red')
        
    
class Alien:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.r = 15
        self.dir = "l"
    
    def drawAlien(self, canvas):
        canvas.create_oval(self.x-self.r, self.y-self.r, self.x+self.r, self.y+self.r, fill = 'green')
        
    def moveAlienLeftandRight(self):
        if self.dir == "l":
            self.x -= 3
        elif self.dir == "r":
            self.x += 3

    def moveAlienDown(self):
        self.y += 50
            
    def checkSide(self, app):
        if self.x <= 40:
            return "l"
        elif self.x >= app.width - 40:
            return "r"
        return "m"