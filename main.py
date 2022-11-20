from cmu_112_graphics import *

import math, copy, random
from tkinter import font

class SpaceShip:
    def __init__(self, x, y):
        self.x = x
        self.y = y 
        self.r = 10
        
    def drawSpaceShip(self, canvas):
        canvas.create_rectangle(self.x-self.r, self.y-self.r, self.x+self.r, self.y+self.r, width = 3)
        
    def moveSpaceShip(self, direction, app):
        if direction == 'Right' and self.x <= app.width-50:
            self.x+=20
            print(self.x)
        elif direction == 'Left' and self.x >= 50:
            self.x-=20
    
class Laser:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.r = 10
        
    def drawLaser(self, canvas):
        canvas.create_oval(self.x - self.r, self.y - self.r, self.x + self.r, self.y + self.r)
        

class SpaceShipLaser(Laser):
    def __init__(self, x, y):
        super().__init__(x,y)
        
    def moveLaser(self):
        self.y -= 5
        
    def checkHitAlien(self, alien):
        if (self.x >= alien.x-alien.r and self.x <= alien.x+alien.r 
            and self.y >= alien.y-alien.r and self.y <= alien.y+alien.r):
            return True
        else:
            return False

class AlienLaser(Laser):
    def __init__(self, x, y):
        super().__init__(x, y)
        
    def moveLaser(self):
        self.y += 5
    
    def checkHitSpaceShip(self, SpaceShip):
        if (self.x >= SpaceShip.x-SpaceShip.r and self.x <= SpaceShip.x+SpaceShip.r 
            and self.y >= SpaceShip.y-SpaceShip.r and self.y <= SpaceShip.y+SpaceShip.r):
            return True
        else:
            return False
    
class Alien:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.r = 15
        self.dir = "l"
    
    def drawAlien(self, canvas):
        canvas.create_oval(self.x-self.r, self.y-self.r, self.x+self.r, self.y+self.r)
        
    def moveAlienLeftandRight(self):
        if self.dir == "l":
            self.x -= 5
        elif self.dir == "r":
            self.x += 5

    def moveAlienDown(self):
        self.y += 50
            
    def checkSide(self, app):
        if self.x <= 40:
            return "l"
        elif self.x >= app.width - 40:
            return "r"
        return "m"
        
# class GroupOfAliens:
#     def __init__(self, listOfAliens):
#         self.listOfAliens = listOfAliens
        
#     def 
        
def gameDimensions():
    pass

def appStarted(app):
    app.mode = 'startScreenMode'
    app.SpaceShip = SpaceShip(app.width//2, 780)
    app.SpaceShipLasers = []
    app.timerDelay = 30
    app.groupOfAliens = []
    app.alienLasers = []
    app.totalTime = 0
    app.gameOver = False
    for i in range(8):
        for j in range(3):
            app.groupOfAliens.append(Alien(50+100*i, 50+100*j))
    
    
# def keyPressed(app, event):
#     pass
        
##########################################
# StartScreen Mode
##########################################

def startScreenMode_redrawAll(app, canvas):
    drawStartScreen(app, canvas)
    drawThreeButtons(app, canvas)


def drawStartScreen(app, canvas):
    fontDirections = font.Font(family = 'Small Fonts', size = 20, weight = 'bold')
    canvas.create_text(app.width//2, 50, text = "SPACE INVADERS!", font = fontDirections)

def drawThreeButtons(app, canvas):
    fontDirections = font.Font(family = 'Small Fonts', size = 25, weight = 'bold')

    # Start Button
    canvas.create_rectangle(app.width//2-app.width*(1/4), app.height//4-app.height*(1/10), 
                           app.width//2+app.width*(1/4), app.height//4+app.height*(1/10), outline = "black", width=3)
    canvas.create_text(app.width//2, app.height//4, text = "START", font = fontDirections)
    
    # Instructions Button
    canvas.create_rectangle(app.width//2-app.width*(1/4), app.height//2-app.height*(1/10), 
                           app.width//2+app.width*(1/4), app.height//2+app.height*(1/10), outline = "black", width=3)
    canvas.create_text(app.width//2, app.height//2, text = "INSTRUCTIONS", font = fontDirections)

    # LeaderBoard Button
    canvas.create_rectangle(app.width//2-app.width*(1/4), app.height*(3/4)-app.height*(1/10), 
                           app.width//2+app.width*(1/4), app.height*(3/4)+app.height*(1/10), outline = "black", width=3)
    canvas.create_text(app.width//2, app.height*(3/4), text = "LEADERBOARD", font = fontDirections)
    
def startScreenMode_timerFired(app):
    # print("startScreen!")
    pass

def startScreenMode_mousePressed(app, event):
    pass

def startScreenMode_keyPressed(app, event):
    if (event.key == 'g'):
        app.mode = 'gameMode'
    elif (event.key == 'v'):
        app.makeAnMVCViolation = True

##########################################
# Game Mode
##########################################


def drawLasers(app, canvas):
    for laser in app.SpaceShipLasers:
        laser.drawLaser(canvas)
    
    for laser in app.alienLasers:
        laser.drawLaser(canvas)
        
def drawAliens(app, canvas):
    for alien in app.groupOfAliens:
        alien.drawAlien(canvas)

def gameMode_redrawAll(app, canvas):
    canvas.create_text(20, 20, text = "YOO")
    app.SpaceShip.drawSpaceShip(canvas)
    drawLasers(app, canvas)
    drawAliens(app, canvas)
    

def gameMode_timerFired(app):
    # print("gameMode!")
    if app.gameOver == False:
        app.totalTime+=app.timerDelay
        print(app.totalTime)
        for alien in app.groupOfAliens:
            alien.moveAlienLeftandRight()
            if alien.checkSide(app) == "l":
                alien.dir = "r"
                alien.moveAlienDown()
            elif alien.checkSide(app) == "r":
                alien.dir = "l"
                alien.moveAlienDown()
                
        for laser in app.SpaceShipLasers:
            laser.moveLaser()
            for alien in app.groupOfAliens:
                if laser.checkHitAlien(alien):
                    app.groupOfAliens.remove(alien)
                    app.SpaceShipLasers.remove(laser)
        for laser in app.alienLasers:
            laser.moveLaser()
            if laser.checkHitSpaceShip(app.SpaceShip):
                print("loss")
                app.gameOver = True
                    
        if app.totalTime%1000==0:
            randomAlien = random.randint(0, 10)
            i=0
            for alien in app.groupOfAliens:
                if i == randomAlien:
                    app.alienLasers.append(AlienLaser(alien.x, alien.y))
                i+=1
        
def gameMode_mousePressed(app, event):
    pass

def gameMode_keyPressed(app, event):
    if (event.key == 'h'):
        app.mode = 'startScreenMode'
    if (event.key == 'Right' or event.key == 'Left'):
        print(event.key)
        print(app.SpaceShip.x)
        app.SpaceShip.moveSpaceShip(event.key, app)
    if (event.key == 'Space'):
        app.SpaceShipLasers.append(SpaceShipLaser(app.SpaceShip.x, app.SpaceShip.y))
    


def playSpaceInvaders():
    width=800
    height=800
    runApp(width=width, height=height)


def main():
    playSpaceInvaders()

if __name__ == '__main__':
    main()
