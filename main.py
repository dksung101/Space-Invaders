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
    app.Planet = Planet(random.randint(200, 600), random.randint(650, 700))
    app.SpaceShipLasers = []
    app.timerDelay = 10
    app.groupOfAliens = []
    app.purpleAlienMovement = [random.randint(4,7), random.randint(4, 7)]
    app.greenAlienMovement = [random.randint(4, 8), random.randint(4, 8)]
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
            typeOfAlien = random.randint(0, 1)
            if typeOfAlien == 0:
                app.groupOfAliens.append(greenAlien(50+100*i, 50+100*j, app.greenAlienMovement[0], app.greenAlienMovement[1]))
            elif typeOfAlien == 1:
                app.groupOfAliens.append(purpleAlien(50+100*i, 50+100*j, app.purpleAlienMovement[0], app.purpleAlienMovement[1]))

    
    
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
    fontDirectionsTitle1 = font.Font(family = 'Small Fonts', size = 50, weight = 'bold')
    fontDirections = font.Font(family = 'Small Fonts', size = 18, weight = 'bold')
    fontDirections1 = font.Font(family = 'Small Fonts', size = 13, weight = 'bold')

    canvas.create_text(app.width/2, app.height//8, text = "How-To-Play", font = fontDirectionsTitle1, fill = "blue")
    canvas.create_rectangle(app.width//2-app.width*(1/3), app.height//2-app.height*(1/5), 
                           app.width//2+app.width*(1/3), app.height/1.95, outline = "blue", width=3)
    canvas.create_text(app.width//2, app.height//4, text = "CONTROLS", font = fontDirectionsTitle, fill = "blue")
    
    canvas.create_text(app.width/5, app.height//2, 
                       text = "1. Use Arrow Keys to move SpaceShip:\nUp, Down, Left, or Right.\n\n2. Use SPACE Key to shoot\nlasers at Alien Enemies", 
                       font = fontDirections, fill = "blue", anchor = "sw")
    
    canvas.create_text(app.width/5, app.height/1.75, 
                       text = "Goal of the Game:", 
                       font = fontDirections, fill = "blue", anchor = "sw")
    
    canvas.create_rectangle(app.width//2-app.width*(1/3), app.height/1.7,
                            app.width//2+app.width*(1/3), app.height/1.1, outline = "blue", width=3)
    canvas.create_text(app.width/2.3, app.height/1.35, 
                       text = '''
                       The Goal of the game is to survive the longest and score the 
                       highest. Each Stage you will face 24 random aliens: 
                       green or purple, which have different movement patterns. 
                       Kill all of the enemies to progress to the next stage! 
                       At later stages, the enemies will begin to shoot faster.
                       Collect Items that can speed up your bullets, but watch out 
                       for the item that slows them down and can kill you.
                       Watch out for the Red Planet that will interfere with 
                       your SpaceShip's movement! 
                        ''', 
                       font = fontDirections1, fill = "blue")
    # canvas.create_text(app.width/3.8, app.height//2, text = "Use SPACE Key to shoot\nlasers at Alien Enemies")
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
    l=len(leaderList)
    while i<l and app.score < int(leaderList[i][1]):
        f.write(f"{leaderList[i][0]},{leaderList[i][1]}\n")
        i+=1
    if i == l:
        f.write(f"{app.name},{app.score}")
    else:
        f.write(f"{app.name},{app.score}\n")
    for j in range(i, l-1):
        f.write(f"{leaderList[j][0]},{leaderList[j][1]}\n")
    
    if i != l:
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
    app.Planet.drawPlanet(canvas)

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
        alien.moveAlienDiagonal()
        if alien.checkSide(app) == "l" or alien.checkSide(app) == "r":
            alien.changeDirection("l")
        
        if app.totalTime % 100 == 0:
            if app.totalTime%1000<600:
                alien.changeDirection("u")
                # print(app.totalTime%1000)
            elif app.totalTime%1000>=600 and alien.movementY < 0:
                alien.movementY*=-1
                # print("BRUH", alien.movementY)
                
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
                # chanceOfItem = random.randint(0, 3)
                # if chanceOfItem == 0:
                if True:
                    newItem = chooseRandItem(alien.x, alien.y)
                    app.items.append(newItem)
                    # print(app.items)
                
def chooseRandItem(x, y):
    typesOfItems = [bulletSpeedDecrease, bulletSpeedIncrease]
    itemIndex = random.randint(0, len(typesOfItems)-1)
    return typesOfItems[itemIndex](x, y)

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
        if isinstance(app.activeItem, bulletSpeedIncrease):
            app.activeItem.activatePower(app)
            if app.totalTime%100 == 0:
                for laser in app.SpaceShipLasers:
                    laser.laserVel *= laser.laserAcc
                    laser.laserSpeed += laser.laserVel

        if isinstance(app.activeItem, bulletSpeedDecrease):
            app.activeItem.activatePower(app)
            if app.totalTime%100 == 0:
                for laser in app.SpaceShipLasers:
                    laser.laserVel *= laser.laserAcc
                    laser.laserSpeed += laser.laserVel*(-1)

def checkGameOverorNextStage(app):
    for laser in app.alienLasers:
        laser.moveLaser()
        if laser.checkHitSpaceShip(app.SpaceShip):
            # print("loss")
            app.gameOver = True
        
    for laser in app.SpaceShipLasers:
        if app.SpaceShip.checkFriendlyFire(laser):
            app.gameOver = True
    
    for alien in app.groupOfAliens:
        if app.SpaceShip.checkHitAlien(alien):
            app.gameOver = True
    
        if alien.y >= app.height:
            app.gameOver = True
    
    if len(app.groupOfAliens) == 20:
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
        
        if app.SpaceShip.SpaceShipNearPlanet(app.Planet):
            # if app.totalTime%100 == 0:
                
            app.SpaceShip.moveTowardsPlanet(app.Planet)
        # if app.SpaceShip.SpaceShipNearPlanet(app.Planet) == False:
            
        
        if app.totalTime%(200//app.stage)>=0 and app.totalTime%(200//app.stage)<10:
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
        app.SpaceShipLasers.append(SpaceShipLaser(app.SpaceShip.x, app.SpaceShip.y-app.SpaceShip.r-10))
        
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