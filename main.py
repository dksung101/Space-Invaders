from cmu_112_graphics import *

import math, copy, random

class SpaceShip:
    def __init__(self, x, y):
        self.x = x
        self.y = y 
        
    def drawSpaceShip(self, canvas):
        canvas.create_rectangle(self.x-10, self.y-10, self.x+10, self.y+10, width = 3)
        
    def moveSpaceShip(self, direction):
        if direction == 'Right':
            self.x+=5
            print(self.x)
        elif direction == 'Left':
            self.x-=5
    

class Laser:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.r = 10
    
    def drawLaser(self, canvas):
        canvas.create_oval(self.x - self.r, self.y - self.r, self.x + self.r, self.y + self.r)
        
    def moveLaser(self):
        self.y -= 5
    
class Alien:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.r = 15
    
    def drawAlien(self, canvas):
        canvas.create_oval(self.x-self.r, self.y-self.r, self.x+self.r, self.y+self.r)
        
# class GroupOfAliens:
#     def __init__(self, listOfAliens):
#         self.listOfAliens = listOfAliens
        
#     def 
        
def gameDimensions():
    pass

def appStarted(app):
    app.mode = 'startScreenMode'
    app.SpaceShip = SpaceShip(400, 780)
    app.Lasers = []
    app.timerDelay = 10
    app.groupOfAliens = []
    for i in range(8):
        for j in range(3):
            app.groupOfAliens.append(Alien(50+100*i, 50+100*j))
    
    
# def keyPressed(app, event):
#     pass
        
##########################################
# StartScreen Mode
##########################################

def startScreenMode_redrawAll(app, canvas):
    pass

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
    for laser in app.Lasers:
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
    for laser in app.Lasers:
        laser.moveLaser()
        
        
def gameMode_mousePressed(app, event):
    pass

def gameMode_keyPressed(app, event):
    if (event.key == 'h'):
        app.mode = 'startScreenMode'
    if (event.key == 'Right' or event.key == 'Left'):
        print(event.key)
        print(app.SpaceShip.x)
        app.SpaceShip.moveSpaceShip(event.key)
    if (event.key == 'Space'):
        app.Lasers.append(Laser(app.SpaceShip.x, app.SpaceShip.y))
    


def playSpaceInvaders():
    width=800
    height=800
    runApp(width=width, height=height)


def main():
    playSpaceInvaders()

if __name__ == '__main__':
    main()
