from cmu_112_graphics import *

import math, copy, random
from tkinter import font
import time
from classes import *

def gameDimensions():
    pass

def appStarted(app):
    app.mode = 'startScreenMode'
    app.name = "dan"
    app.SpaceShip = SpaceShip(app.width//2, app.height-50)
    app.SpaceShipLasers = []
    app.timerDelay = 10
    app.groupOfAliens = []
    app.alienLasers = []
    app.items = []
    app.itemActive = False
    app.activeItem = None
    app.totalTime = 0
    app.leaderBoardtext = open("leaderboard.txt", "r").read() #https://www.w3schools.com/python/python_file_open.asp //opening files
    app.score = 0
    app.countDown = 3
    app.gameOver = False
    app.stage = 1
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
    fontDirections = font.Font(family = 'Small Fonts', size = 40, weight = 'bold')
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
        app.name = app.getUserInput("What is your name?: ")
        app.mode = 'gameMode'
    
    elif (event.x >= app.width//2-app.width*(1/4) and event.x <=app.width//2+app.width*(1/4) 
        and event.y >= app.height//2-app.height*(1/10) and event.y <= app.height//2+app.height*(1/10)):
        app.mode = 'instructionMode'
        
    elif (event.x >= app.width//2-app.width*(1/4) and event.x <=app.width//2+app.width*(1/4) 
        and event.y >= app.height*(3/4)-app.height*(1/10) and event.y <= app.height*(3/4)+app.height*(1/10)):
        app.mode = 'leaderboardMode'

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

def createLeaderBoard(app, canvas):
    fontDirections = font.Font(family = 'Small Fonts', size = 15, weight = 'bold')
    newLeaderBoard = []
    for pair in app.leaderBoardtext.split('\n'):
        pairOfData = []
        for data in pair.split(","):
            pairOfData.append(data)
        newLeaderBoard.append(pairOfData)
    # print("HERE", newLeaderBoard)
    for i in range(0, 10):
        if len(newLeaderBoard) > i:
            canvas.create_text(app.width//2-app.width*(1/5), app.height-app.height*(77/100)+i*app.height*(2/33), 
                               text = f"{i+1}.{newLeaderBoard[i][0]}: {newLeaderBoard[i][1]}", font = fontDirections, 
                               fill = "blue", anchor = 'sw')  
        else:
            canvas.create_text(app.width//2-app.width*(1/5), app.height-app.height*(77/100)+i*app.height*(2/33), text = f"{i+1}.",
                               font = fontDirections, fill = "blue", anchor = 'sw')  


def leaderboardMode_redrawAll(app, canvas):
    canvas.create_image(app.width//2, app.height//2, image=ImageTk.PhotoImage(app.backGround))
    drawleaderBoard(app, canvas)
    createLeaderBoard(app, canvas)

def leaderboardMode_timerFired(app):
    pass

def leaderboardMode_mousePressed(app, event):
    if (event.x >= app.width//10-30 and event.x <= app.width//10+30 
        and event.y >= app.height*(19/20)-10 and event.y <= app.height*(19/20)+10):
        app.mode = 'startScreenMode'
    
##########################################
# GameOver Mode
##########################################

def drawgameOverScreen(app, canvas):
    fontDirectionsBackButton = font.Font(family = 'Small Fonts', size = 13, weight = 'bold')
    fontDirectionsTitle = font.Font(family = 'Small Fonts', size = 25, weight = 'bold')
    canvas.create_text(app.width//2, app.height//2, text = f"GAME OVER! \nYour Score: {app.score}", font = fontDirectionsTitle, fill = "blue")
    
    # Back Button (bottom left corner)
    canvas.create_rectangle(app.width//10-30, app.height*(19/20)-10, app.width//10+30, app.height*(19/20)+10, outline = "blue")
    canvas.create_text(app.width//10, app.height*(19/20), text = "EXIT", font = fontDirectionsBackButton, fill = "blue")


def gameOverMode_redrawAll(app, canvas):
    canvas.create_image(app.width//2, app.height//2, image=ImageTk.PhotoImage(app.backGround))
    drawgameOverScreen(app, canvas)
    
    
def gameOverMode_timerFired(app):
    pass

def updateLeaderBoard(app):
    f1 = open('leaderboard.txt', 'r')
    leaderboard = f1.read()
    f = open('leaderboardtmp.txt', 'w')
    i=0
    leaderList = []
    for line in leaderboard.split("\n"):
        newList = []
        for data in line.split(","):
            newList.append(data)
        leaderList.append(newList)
    # print(leaderList)
    l=len(leaderList)
    while app.score < int(leaderList[i][1]):
        f.write(f"{leaderList[i][0]},{leaderList[i][1]}\n")
        i+=1
    f.write(f"{app.name},{app.score}\n")
    for j in range(i, l-1):
        f.write(f"{leaderList[j][0]},{leaderList[j][1]}\n")
    f.write(f"{leaderList[l-1][0]},{leaderList[l-1][1]}")   
    
    f1.close()
    f.close()
    
    #https://www.geeksforgeeks.org/python-copy-contents-of-one-file-to-another-file/
    with open("leaderboardtmp.txt", "r") as f, open("leaderboard.txt", 'w') as f1: 
        for line in f:
            f1.write(line)
    
    f.close()
    f1.close()
   


def gameOverMode_mousePressed(app, event):
    if (event.x >= app.width//10-30 and event.x <= app.width//10+30 
        and event.y >= app.height*(19/20)-10 and event.y <= app.height*(19/20)+10):
        updateLeaderBoard(app)
        appStarted(app)
        app.mode = 'startScreenMode'
    
##########################################
# StageScreen Mode
##########################################

def drawstageScreen(app, canvas):
    fontDirectionsBackButton = font.Font(family = 'Small Fonts', size = 13, weight = 'bold')

    # Back Button (bottom left corner)
    canvas.create_rectangle(app.width//10-30, app.height*(19/20)-10, app.width//10+30, app.height*(19/20)+10, outline = "blue")
    canvas.create_text(app.width//10, app.height*(19/20), text = "EXIT", font = fontDirectionsBackButton, fill = "blue")
    

def stageScreenMode_redrawAll(app, canvas):
    canvas.create_image(app.width//2, app.height//2, image=ImageTk.PhotoImage(app.backGround))
    drawstageScreen(app, canvas)

    fontDirectionsTitle = font.Font(family = 'Small Fonts', size = 25, weight = 'bold')
    canvas.create_text(app.width//2, app.height//2, 
                       text = f"Next Stage: {app.stage} \n Starting in {app.countDown}... \n Current Score: {app.score}", 
                       font = fontDirectionsTitle, fill = "blue")

    
def stageScreenMode_timerFired(app):
    app.countDown-=1
    time.sleep(1)
    if app.countDown == 0:
        tmpStage = app.stage
        tmpScore = app.score
        tmpName = app.name
        appStarted(app)
        app.stage = tmpStage
        app.score = tmpScore
        app.name = tmpName
        app.mode = "gameMode"


def stageScreenMode_mousePressed(app, event):
    if (event.x >= app.width//10-30 and event.x <= app.width//10+30 
        and event.y >= app.height*(19/20)-10 and event.y <= app.height*(19/20)+10):
        app.mode = 'startScreenMode'
        tmpStage = app.stage
        appStarted(app)
        app.stage = tmpStage
        

##########################################
# Game Mode
##########################################

def drawTimer(app, canvas):
    fontDirections = font.Font(family = 'Small Fonts', size = 20, weight = 'bold')

    totalTime = app.totalTime*4.34782//1000
    # totalTime *= 4.34
    # print(totalTime)
    canvas.create_text(app.width*(2/20), app.height*(1/30), text = f'Time: {totalTime}s', font = fontDirections, fill = 'blue')
    
def drawScore(app, canvas):
    fontDirections = font.Font(family = 'Small Fonts', size = 20, weight = 'bold')
    canvas.create_text(app.width*(18/20), app.height*(1/30), text = f"Score: {app.score}", font = fontDirections, fill = 'blue')

def drawStage(app, canvas):
    fontDirections = font.Font(family = 'Small Fonts', size = 20, weight = 'bold')
    canvas.create_text(app.width//2, app.height*(1/30), text = f"Stage {app.stage}", font = fontDirections, fill = 'blue')


def drawLasers(app, canvas):
    for laser in app.SpaceShipLasers:
        laser.drawLaser(canvas)
    
    for laser in app.alienLasers:
        laser.drawLaser(canvas)
        
def drawAliens(app, canvas):
    for alien in app.groupOfAliens:
        alien.drawAlien(canvas)
        
def drawItems(app, canvas):
    for item in app.items:
        item.drawItem(canvas)
        

def gameMode_redrawAll(app, canvas):
    canvas.create_image(app.width//2, app.height//2, image=ImageTk.PhotoImage(app.backGround))
    app.SpaceShip.drawSpaceShip(canvas)
    drawLasers(app, canvas)
    drawAliens(app, canvas)
    
    drawItems(app, canvas)
    
    # Back Button (bottom left corner)
    fontDirectionsBackButton = font.Font(family = 'Small Fonts', size = 13, weight = 'bold')
    canvas.create_rectangle(app.width//10-30, app.height*(19/20)-10, app.width//10+30, app.height*(19/20)+10, outline = "blue")
    canvas.create_text(app.width//10, app.height*(19/20), text = "EXIT", font = fontDirectionsBackButton, fill = "blue")
    
    drawStage(app, canvas)
    drawTimer(app, canvas)
    drawScore(app, canvas)
    
def moveAliensAround(app):
    for alien in app.groupOfAliens:
        alien.moveAlienLeftandRight()
        if alien.checkSide(app) == "l":
            alien.dir = "r"
            alien.moveAlienDown()
        elif alien.checkSide(app) == "r":
            alien.dir = "l"
            alien.moveAlienDown()

def moveItemsDown(app):
    for item in app.items:
        item.moveItemDown()

def moveAndCheckSpaceShipLaser(app):
    for laser in app.SpaceShipLasers:
        # print(laser.laserSpeed)
        laser.moveLaser()
        for alien in app.groupOfAliens:
            if laser.checkHitAlien(alien):
                app.groupOfAliens.remove(alien)
                app.SpaceShipLasers.remove(laser)
                app.score += 10*app.stage
                
                if True:
                    newItem = chooseRandItem(alien.x, alien.y)
                    app.items.append(newItem)
                    # print(app.items)
                
def chooseRandItem(x, y):
    typesOfItems = [bulletSpeedDecrease, bulletSpeedIncrease]
    itemIndex = random.randint(0, len(typesOfItems)-1)
    return typesOfItems[itemIndex](x, y, )

def removeCollidingLasers(app):
    for laser in app.SpaceShipLasers:
        for alienLaser in app.alienLasers:
            if laser.checkHitAlienLaser(alienLaser):
                app.SpaceShipLasers.remove(laser)
                app.alienLasers.remove(alienLaser)

def removeCollidingItems(app):
    for item in app.items:
        # item.deactivatePower(app)
        if item.checkHitSpaceShip(app.SpaceShip):
            app.items.remove(item)
            app.activeItem = item
            app.itemActive = True
            
def checkItemActive(app):
    if app.itemActive == True:
        app.activeItem.activatePower(app)

def checkGameOverorNextStage(app):
    for laser in app.alienLasers:
        laser.moveLaser()
        if laser.checkHitSpaceShip(app.SpaceShip):
            # print("loss")
            app.gameOver = True
        
    if len(app.groupOfAliens) == 22:
        app.stage += 1
        app.mode = "stageScreenMode"
        
def randomAlienShootLaser(app):
    randomAlien = random.randint(0, len(app.groupOfAliens)-1)
    i=0
    for alien in app.groupOfAliens:
        if i == randomAlien:
            app.alienLasers.append(AlienLaser(alien.x, alien.y))
        i+=1
    
def gameMode_timerFired(app):
    # print("gameMode!")
    if app.gameOver == False:
        app.totalTime+=app.timerDelay
    
        
        app.SpaceShip.moveSpaceShip(app)
        
        moveAliensAround(app)
        
        moveAndCheckSpaceShipLaser(app)
        
        moveItemsDown(app)
        
        removeCollidingLasers(app)
        
        removeCollidingItems(app)
            
        checkItemActive(app)
        
        checkGameOverorNextStage(app)
                        
        if app.totalTime%200==0:
            randomAlienShootLaser(app)
    
    elif app.gameOver == True:
        app.mode = "gameOverMode"
        
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