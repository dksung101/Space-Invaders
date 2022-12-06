import random

class SpaceShip:
    def __init__(self, x, y):
        self.x = x
        self.y = y 
        self.r = 15
        self.movingRight = False
        self.movingLeft = False
        self.movingUp = False
        self.movingDown = False
        self.Xvelocity = 5
        self.Yvelocity = 5
        self.planetX = 2
        self.planetY = 2
        
    def drawSpaceShip(self, canvas):
        canvas.create_oval(self.x-self.r, self.y-self.r, self.x+self.r, self.y+self.r, width = 3, fill = 'orange')
        
    def moveSpaceShip(self, app):
        if self.movingRight == True and self.x <= app.width-50:
            self.x+=self.Xvelocity

        if self.movingLeft == True and self.x >= 50:
            self.x-=self.Xvelocity
        
        if self.movingUp == True and self.y >= 50:
            self.y-=self.Yvelocity
                
        if self.movingDown == True and self.y <= app.height-50:
            self.y+=self.Yvelocity
    
    def checkFriendlyFire(self, laser):
        if (self.x-laser.x)**2+(self.y-laser.y)**2 < (self.r+laser.r)**2:
            return True
        return False
    
    
    def moveTowardsPlanet(self, planet):
        if planet.x < self.x:
            self.x -= self.planetX
            
        elif planet.x > self.x:
            self.x += self.planetX
        
        if planet.y < self.y:
            self.y -= self.planetY
            
        elif planet.y > self.y:
            self.y += self.planetY 
    
    def checkHitAlien(self, alien):
        if (self.x-alien.x)**2+(self.y-alien.y)**2 < (self.r+alien.r)**2:
            return True
        return False
    
    def SpaceShipNearPlanet(self, Planet):
        if (self.x - Planet.x)**2 + (self.y - Planet.y)**2 < (self.r + Planet.r*4/3)**2:
            return True
        return False

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
        self.color = "blue"
        self.laserVel = 1
        self.laserAcc = 1.5
        
    def moveLaser(self):
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
        canvas.create_oval(self.x - self.r, self.y - self.r, self.x + self.r, self.y + self.r, fill = self.color)


class AlienLaser(Laser):
    def __init__(self, x, y):
        super().__init__(x, y)
        
    def moveLaser(self):
        self.y += 10
    
    def checkHitSpaceShip(self, SpaceShip):
        # if (SpaceShip.x - self.x)**2 + (SpaceShip.y - self.y)**2 < (SpaceShip.r + self.r)**2:
        #     return True
        if (self.x-SpaceShip.x)**2+(self.y-SpaceShip.y)**2 < (self.r+SpaceShip.r)**2:
            return True
        return False
        
    def drawLaser(self, canvas):
        canvas.create_oval(self.x - self.r, self.y - self.r, self.x + self.r, self.y + self.r, fill = 'red')
        
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
            laser.color = "purple"
            
    def deactivatePower(self, app):
        for laser in app.SpaceShipLasers:
            laser.laserSpeed = 10
            laser.color = "blue"
    
class bulletSpeedDecrease(Item):
    def __init__(self, xPos, yPos):
        super().__init__(xPos, yPos)
        
    def drawItem(self, canvas):
        canvas.create_oval(self.xPos-self.r, self.yPos-self.r, self.xPos+self.r, self.yPos+self.r, fill = "cyan")

    def activatePower(self, app):
        for laser in app.SpaceShipLasers:
            # laser.laserSpeed = 5
            laser.color = "cyan"

    def deactivatePower(self, app):
        for laser in app.SpaceShipLasers:
            laser.laserSpeed = 10
            laser.color = "blue"

class Alien:
    def __init__(self, x, y, movementX, movementY):
        self.x = x
        self.y = y
        self.r = 15
        self.dir = "l"
        self.movementX = movementX
        self.movementY = movementY
        
    def moveAlienLeftandRight(self):
        if self.dir == "l":
            self.x -= 3
        elif self.dir == "r":
            self.x += 3

    def moveAlienDown(self):
        self.y += 50
    
    def moveAlienDiagonal(self):
        self.x += self.movementX
        self.y += self.movementY/5
    
    def changeDirection(self, dir):
        if dir == "l" or dir == "r":
            self.movementX *= -1
        elif dir == "u" or dir == "d":
            self.movementY *= -1
        
    def checkSide(self, app):
        if self.x <= 40:
            return "l"
        elif self.x >= app.width - 40:
            return "r"
        return "m"

class purpleAlien(Alien):
    def __init__(self, x, y, movementX, movementY):
        super().__init__(x, y, movementX, movementY)
    
    def drawAlien(self, canvas):
        canvas.create_oval(self.x-self.r, self.y-self.r, self.x+self.r, self.y+self.r, fill = 'purple')
    

class greenAlien(Alien):
    def __init__(self, x, y, movementX, movementY):
        super().__init__(x, y, movementX, movementY)
    
    def drawAlien(self, canvas):
        canvas.create_oval(self.x-self.r, self.y-self.r, self.x+self.r, self.y+self.r, fill = 'green')
        
class Planet:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.r = random.randint(40, 60)
        
    def drawPlanet(self, canvas):
        canvas.create_oval(self.x-self.r, self.y-self.r, self.x+self.r, self.y+self.r, fill = 'red')
    
    