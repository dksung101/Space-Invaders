from cmu_112_graphics import *

import math, copy, random
from tkinter import font

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
            self.x+=7

        if self.movingLeft == True and self.x >= 50:
            self.x-=7
            
        if self.movingUp == True and self.y >= 50:
            self.y-=7
                
        if self.movingDown == True and self.y <= app.height-50:
            self.y+=7
    
class Laser:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.r = 10

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
    
    def checkHitAlienLaser(self, alienLaser):
        if (self.x >= alienLaser.x-alienLaser.r and self.x <= alienLaser.x+alienLaser.r 
            and self.y >= alienLaser.y-alienLaser.r and self.y <= alienLaser.y+alienLaser.r):
            return True
        else:
            return False
        
    def drawLaser(self, canvas):
        canvas.create_oval(self.x - self.r, self.y - self.r, self.x + self.r, self.y + self.r, fill = 'blue')
        

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
    app.SpaceShip = SpaceShip(app.width//2, app.height-50)
    app.SpaceShipLasers = []
    app.timerDelay = 30
    app.groupOfAliens = []
    app.alienLasers = []
    app.totalTime = 0
    app.gameOver = False
    app.image1 = app.loadImage('Images and Sprites/SpaceInvadersBG.jpg')
    # Background image from: https://www.google.com/url?
    # sa=i&url=http%3A%2F%2Fwww.csun.edu%2F~asn71882%2Fc
    # hallenge09%2F&psig=AOvVaw33CnmOUxRPUhQIq1GM0w4s&ust
    # =1669023233501000&source=images&cd=vfe&ved=0CA8QjRx
    # qFwoTCIjW8Zi6vPsCFQAAAAAdAAAAABAJ
    app.backGround = app.scaleImage(app.image1, 1)
    for i in range(8):
        for j in range(3):
            app.groupOfAliens.append(Alien(50+100*i, 50+100*j))
    
    
# def keyPressed(app, event):
#     pass
        
##########################################
# StartScreen Mode
##########################################

def startScreenMode_redrawAll(app, canvas):
    canvas.create_image(app.width//2, app.height//2, image=ImageTk.PhotoImage(app.backGround))
    drawStartScreen(app, canvas)
    drawThreeButtons(app, canvas)


def drawStartScreen(app, canvas):
    fontDirections = font.Font(family = 'Small Fonts', size = 20, weight = 'bold')
    canvas.create_text(app.width//2, 50, text = "SPACE INVADERS!", font = fontDirections, fill = 'blue')

def drawThreeButtons(app, canvas):
    fontDirections = font.Font(family = 'Small Fonts', size = 25, weight = 'bold')

    # Start Button
    canvas.create_rectangle(app.width//2-app.width*(1/4), app.height//4-app.height*(1/10), 
                           app.width//2+app.width*(1/4), app.height//4+app.height*(1/10), outline = "blue", width=3)
    canvas.create_text(app.width//2, app.height//4, text = "START", font = fontDirections, fill = 'blue')
    
    # Instructions Button
    canvas.create_rectangle(app.width//2-app.width*(1/4), app.height//2-app.height*(1/10), 
                           app.width//2+app.width*(1/4), app.height//2+app.height*(1/10), outline = "blue", width=3)
    canvas.create_text(app.width//2, app.height//2, text = "INSTRUCTIONS", font = fontDirections, fill = 'blue')

    # LeaderBoard Button
    canvas.create_rectangle(app.width//2-app.width*(1/4), app.height*(3/4)-app.height*(1/10), 
                           app.width//2+app.width*(1/4), app.height*(3/4)+app.height*(1/10), outline = "blue", width=3)
    canvas.create_text(app.width//2, app.height*(3/4), text = "LEADERBOARD", font = fontDirections, fill = 'blue')
    
def startScreenMode_timerFired(app):
    # print("startScreen!")
    pass

def startScreenMode_mousePressed(app, event):
    if (event.x >= app.width//2-app.width*(1/4) and event.x <=app.width//2+app.width*(1/4) 
        and event.y >= app.height//4-app.height*(1/10) and event.y <= app.height//4+app.height*(1/10)):
        app.mode = 'gameMode'
    
    elif (event.x >= app.width//2-app.width*(1/4) and event.x <=app.width//2+app.width*(1/4) 
        and event.y >= app.height//2-app.height*(1/10) and event.y <= app.height//2+app.height*(1/10)):
        app.mode = 'instructionMode'
        
    elif (event.x >= app.width//2-app.width*(1/4) and event.x <=app.width//2+app.width*(1/4) 
        and event.y >= app.height*(3/4)-app.height*(1/10) and event.y <= app.height*(3/4)+app.height*(1/10)):
        app.mode = 'leaderboardMode'

# def startScreenMode_keyPressed(app, event):
#     if (event.key == 'g'):
#     elif (event.key == 'v'):
#         app.makeAnMVCViolation = True



##########################################
# Instruction Mode
##########################################

def drawInstructionBoard(app, canvas):
    fontDirectionsBackButton = font.Font(family = 'Small Fonts', size = 13, weight = 'bold')
    fontDirectionsTitle = font.Font(family = 'Small Fonts', size = 25, weight = 'bold')

    canvas.create_rectangle(app.width//2-app.width*(1/4), app.height//2-app.height*(1/5), 
                           app.width//2+app.width*(1/4), app.height//2+app.height*(1/5), outline = "blue", width=3)
    canvas.create_text(app.width//2, app.height//2, text = "CONTROLS", font = fontDirectionsTitle, fill = "blue")
    
    # Back Button (bottom left corner)
    canvas.create_rectangle(app.width//10-30, app.height*(19/20)-10, app.width//10+30, app.height*(19/20)+10, outline = "blue")
    canvas.create_text(app.width//10, app.height*(19/20), text = "BACK", font = fontDirectionsBackButton, fill = "blue")

def instructionMode_redrawAll(app, canvas):
    canvas.create_image(app.width//2, app.height//2, image=ImageTk.PhotoImage(app.backGround))
    drawInstructionBoard(app, canvas)

def instructionMode_timerFired(app):
    pass

def instructionMode_mousePressed(app, event):
    if (event.x >= app.width//10-30 and event.x <= app.width//10+30 
        and event.y >= app.height*(19/20)-10 and event.y <= app.height*(19/20)+10):
        app.mode = 'startScreenMode'
    

def instructionMode_keyPressed(app, event):
    pass

##########################################
# Leaderboard Mode
##########################################

def drawleaderBoard(app, canvas):
    fontDirectionsBackButton = font.Font(family = 'Small Fonts', size = 13, weight = 'bold')
    fontDirectionsTitle = font.Font(family = 'Small Fonts', size = 25, weight = 'bold')
    canvas.create_rectangle(app.width//2-app.width*(1/4), app.height//2-app.height*(1/3), 
                           app.width//2+app.width*(1/4), app.height//2+app.height*(1/3), outline = "blue", width=3)
    canvas.create_text(app.width//2, app.height//2-app.height*(1.1/3), text = "LEADERBOARD", font = fontDirectionsTitle, fill = "blue")
    
    # Back Button (bottom left corner)
    canvas.create_rectangle(app.width//10-30, app.height*(19/20)-10, app.width//10+30, app.height*(19/20)+10, outline = "blue")
    canvas.create_text(app.width//10, app.height*(19/20), text = "BACK", font = fontDirectionsBackButton, fill = "blue")

def leaderboardMode_redrawAll(app, canvas):
    canvas.create_image(app.width//2, app.height//2, image=ImageTk.PhotoImage(app.backGround))
    drawleaderBoard(app, canvas)

def leaderboardMode_timerFired(app):
    pass

def leaderboardMode_mousePressed(app, event):
    if (event.x >= app.width//10-30 and event.x <= app.width//10+30 
        and event.y >= app.height*(19/20)-10 and event.y <= app.height*(19/20)+10):
        app.mode = 'startScreenMode'
    

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
    canvas.create_image(app.width//2, app.height//2, image=ImageTk.PhotoImage(app.backGround))
    app.SpaceShip.drawSpaceShip(canvas)
    drawLasers(app, canvas)
    drawAliens(app, canvas)
    
    # Back Button (bottom left corner)
    fontDirectionsBackButton = font.Font(family = 'Small Fonts', size = 13, weight = 'bold')
    canvas.create_rectangle(app.width//10-30, app.height*(19/20)-10, app.width//10+30, app.height*(19/20)+10, outline = "blue")
    canvas.create_text(app.width//10, app.height*(19/20), text = "EXIT", font = fontDirectionsBackButton, fill = "blue")

    
def moveAliensAround(app):
    for alien in app.groupOfAliens:
        alien.moveAlienLeftandRight()
        if alien.checkSide(app) == "l":
            alien.dir = "r"
            alien.moveAlienDown()
        elif alien.checkSide(app) == "r":
            alien.dir = "l"
            alien.moveAlienDown()

def moveAndCheckSpaceShipLaser(app):
    for laser in app.SpaceShipLasers:
        laser.moveLaser()
        for alien in app.groupOfAliens:
            if laser.checkHitAlien(alien):
                app.groupOfAliens.remove(alien)
                app.SpaceShipLasers.remove(laser)

def removeCollidingLasers(app):
    for laser in app.SpaceShipLasers:
        for alienLaser in app.alienLasers:
            if laser.checkHitAlienLaser(alienLaser):
                app.SpaceShipLasers.remove(laser)
                app.alienLasers.remove(alienLaser)
             
def checkGameOver(app):
    for laser in app.alienLasers:
        laser.moveLaser()
        if laser.checkHitSpaceShip(app.SpaceShip):
            # print("loss")
            app.gameOver = True
            
def randomAlienShootLaser(app):
    randomAlien = random.randint(0, len(app.groupOfAliens))
    i=0
    for alien in app.groupOfAliens:
        if i == randomAlien:
            app.alienLasers.append(AlienLaser(alien.x, alien.y))
        i+=1
    
def gameMode_timerFired(app):
    # print("gameMode!")
    if app.gameOver == False:
        app.totalTime+=app.timerDelay
        # print(app.totalTime)
        
        app.SpaceShip.moveSpaceShip(app)
        
        moveAliensAround(app)
        
        moveAndCheckSpaceShipLaser(app)
        
        removeCollidingLasers(app)
                
        checkGameOver(app)
                        
        if app.totalTime%200==0:
            randomAlienShootLaser(app)
        
def gameMode_mousePressed(app, event):
    if (event.x >= app.width//10-30 and event.x <= app.width//10+30 
    and event.y >= app.height*(19/20)-10 and event.y <= app.height*(19/20)+10):
        app.mode = 'startScreenMode'




def gameMode_keyPressed(app, event):
    if (event.key == 'Right'):
        app.SpaceShip.movingRight = True
        
    if (event.key == 'Left'):
        app.SpaceShip.movingLeft = True
        
    if (event.key == 'Up'):
        app.SpaceShip.movingUp = True
        
    if (event.key == 'Down'):
        app.SpaceShip.movingDown = True
        
    if (event.key == 'Space'):
        app.SpaceShipLasers.append(SpaceShipLaser(app.SpaceShip.x, app.SpaceShip.y))
    
def gameMode_keyReleased(app, event):
    if event.key == 'Right':
        app.SpaceShip.movingRight = False
    
    if event.key == 'Left':
        app.SpaceShip.movingLeft = False
        
    if (event.key == 'Up'):
        app.SpaceShip.movingUp = False
        
    if (event.key == 'Down'):
        app.SpaceShip.movingDown = False

def playSpaceInvaders():
    width=800
    height=800
    runApp(width=width, height=height)


def main():
    playSpaceInvaders()

if __name__ == '__main__':
    main()
