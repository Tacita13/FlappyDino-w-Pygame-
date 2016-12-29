
'''
Isamar López Rodríguez
14/12/15

Flappy Dino game
'''

import pygame
from random import randint
 
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 250, 0)
RED = (250, 0, 0)
LIGHTRED =(200, 0, 0)
LIGHTGREEN =(0, 200, 0)
LIGHTBLUE = (0, 0, 250)
BLUE = (121, 151, 247)
PURPLE =(181, 34, 230)
LIGHTPURPLE =(218, 167, 235)
BLUEBACKGROUND = (94, 196, 230)
YELLOW = (250, 242, 22)
LIGHTYELLOW = (250, 246, 122)
GREENOBSTACLE = (103, 235, 59)
DARKGREENOBSTACLE = (101, 168, 79)
VERYDARKGREENOBSTACLE = (50, 94, 57)

pygame.init()

# Load all images used in the game(background and player)
dinoImg = pygame.image.load('FlappyDinoFinish2.png')
dinoImg.set_colorkey(WHITE)
backgroundImage = pygame.image.load("jungle-background-vector.jpg")
backgroundImage2 = pygame.image.load("background2.jpg")
backgroundImage3 = pygame.image.load("background3.jpg")
backgroundPosition = [0, 0]

size = (700, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Flappy Dino")

# Inital set of variables
done = False
scorePoints = 0
x = 350
y = 250
ySpeed = 2
xSpeed = 0
xPos =700
yPos = 0
xSize = 70
ySize = randint(0, 350)
space = 200
obSpeed = 2.5
ground = 460
gOver=False
scoreList=[]
pause=False


clock = pygame.time.Clock()

#-------------------FUNCTIONS---------------------------

# draws the dino in x,y coordinates
def dino(x,y):
    screen.blit(dinoImg, (x,y))
    
# function to facilitate writing text
def printText(msg, x, y, size):
    font = pygame.font.SysFont(None, size)
    text = font.render (msg, True, BLACK)
    screen.blit(text, [x, y])
    
# Displays Game Over and final score
def gameOver():
    printText("GAME OVER", 180, 100, 75)
    printText("Your score: "+str(scorePoints), 230, 150, 50)
    
# Draws obstacles at the given 3 levels of difficulty    
def obstacle(xPos, yPos, xSize, ySize):

    if scorePoints > 4 and scorePoints < 10:
        pygame.draw.rect(screen, DARKGREENOBSTACLE, [xPos, yPos, xSize, ySize])
        pygame.draw.rect (screen, DARKGREENOBSTACLE, [xPos, int(yPos+ySize+space), xSize, int(ySize+500)])
        
    elif scorePoints > 9:
        pygame.draw.rect(screen, VERYDARKGREENOBSTACLE, [xPos, yPos, xSize, ySize])
        pygame.draw.rect (screen, VERYDARKGREENOBSTACLE, [xPos, int(yPos+ySize+space), xSize, int(ySize+500)])

    else:        
        pygame.draw.rect(screen, GREENOBSTACLE, [xPos, yPos, xSize, ySize])
        pygame.draw.rect (screen, GREENOBSTACLE, [xPos, int(yPos+ySize+space), xSize, int(ySize+500)])


# Shows permanent score
def Score(scorePoints):
    printText("Score: "+str(scorePoints), 0, 0, 30)
    
# Excluisivly used in the button function for standard text presentation
def textObjects(text, font):
    textSurface = font.render(text, True, BLACK)
    return textSurface, textSurface.get_rect()
    pygame.display.update()
    time.sleep(2)
    gameLoop()

# Create standard button for any action    
def button(msg, x, y, w, h, iColor, aColor, action =None, prev = None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    
# mouse position and click sensor for the buttons, plus color change (active/inactive Colors)    
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(screen, iColor,(x,y,w,h))
        if click[0] == 1 and action != None:
             if not prev:
                 action()
             else:
                 action(prev)
    else:
        pygame.draw.rect(screen, aColor,(x,y,w,h))
      
    smallText = pygame.font.SysFont(None, 20)       
    smallText = pygame.font.Font('freesansbold.ttf',20)
    textSurf, textRect = textObjects(msg, smallText)
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    screen.blit(textSurf, textRect)

# Main menu screen
def gameIntro():
        
    listScr=False
    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
        screen.fill(BLUEBACKGROUND)
        printText("Flappy Dino", 210, 100, 75)
        
#Displayed buttons
        button("START",210,200,300,40, GREEN, LIGHTGREEN, gameLoop)
        button("INSTRUCTIONS", 210, 250, 300, 40, LIGHTPURPLE, PURPLE, instrScreen, "intro")        
        button("HIGH SCORES", 210, 300, 300, 40, BLUE, LIGHTBLUE, listScreen)
        button("CREDITS", 210, 350, 300, 40, LIGHTYELLOW, YELLOW, creditsScreen, "intro")
        button("QUIT",210,400,300,40, RED, LIGHTRED, gameQuit)
        
        pygame.display.update()
        clock.tick(15)

# Pause menu screen        
def gamePause():
    global pause
    listScr=False
    pause=True
    while pause:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        screen.fill(BLUEBACKGROUND)
        printText("PAUSED", 260, 100, 75)

        button("START",210,200,300,40, GREEN, LIGHTGREEN, gameLoop)
        button("INSTRUCTIONS", 210, 250, 300, 40, LIGHTPURPLE, PURPLE, instrScreen, "pause")        
        button("CREDITS", 210, 300, 300, 40, LIGHTYELLOW, YELLOW, creditsScreen, "pause")
        button("QUIT",210,350,300,40, RED, LIGHTRED, gameQuit)
        pygame.display.update()
        clock.tick(15)

# Instructions Screen        
def instrScreen(sourceScreen):

    listScr=False
    global instr
    instr=True
    while instr:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        screen.fill(BLUEBACKGROUND)
        printText("INSTRUCTIONS", 140, 100, 75)
        printText("1. Press the UP arrow key to fly up.", 100, 200, 30)
        printText("2. Do not hit the ground nor crash against the obstacles.", 100, 250, 30)
        printText("3. Press the ESC key to pause the game.", 100, 300, 30)
   
# For those screens with back button, parameter sourceScreen shows where to go back to
        if sourceScreen == "pause":
            button("BACK",0,0,100,50, GREEN, LIGHTGREEN, gamePause)
        else:
            button("BACK",0,0,100,50, GREEN, LIGHTGREEN, gameIntro)

        pygame.display.update()
        clock.tick(15)

# Best Scores Screen
def listScreen():
    global scorePoints
    global listScr
    listScr=True
    while listScr:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        screen.fill(BLUEBACKGROUND)
        printText("BEST SCORES", 200, 100, 75)

# Display Top ten list in order
        y=0
        if gOver == True:
            if len(scoreList) > 10:
                for i in range(10):
                    printText("%s.............................  %s"%(i+1,scoreList[i]), 250, 180+y, 30)
                    y+=25
            else:   
                for i in range(len(scoreList)):
                    printText("%s.............................  %s"%(i+1,scoreList[i]), 250, 180+y, 30)
                    y+=25

        button("BACK",0,0,100,50, GREEN, LIGHTGREEN, gameIntro)
        scorePoints=0

        pygame.display.update()
        clock.tick(15)

# Create and manage top ten scores list
def scoreTopTen(scorePoints):
    if scorePoints != 0:
        scoreList.append(int(scorePoints))
        scoreList.sort()
        scoreList.reverse()
        return scoreList
    else:
        return scoreList
    
# Credits Screen
def creditsScreen(sourceScreen):

    global credits
    credits=True
    while credits:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        screen.fill(BLUEBACKGROUND)
        printText("CREDITS", 220, 100, 75)
        printText("UNIVERSIDAD DE PUERTO RICO: RÍO PIEDRAS", 120, 180, 30)
        printText("DEPARTAMENTO DE CIENCIAS DE CÓMPUTOS", 120, 210, 30)
        printText("Isamar López Rodríguez", 190, 250, 40)
        printText("Iván René Ruiz Torres", 200, 290, 40)
        printText("Youmble S.r.l. - Flappy Dino img. - iTunes ", 160, 360, 30)
        printText("Xooplate - Background img. -Freepik ", 170, 390, 30)

        if sourceScreen == "pause":
            button("BACK",0,0,100,50, GREEN, LIGHTGREEN, gamePause)
        else:
            button("BACK",0,0,100,50, GREEN, LIGHTGREEN, gameIntro)

        pygame.display.update()
        clock.tick(15)

# To quit the game
def gameQuit ():
    intro=False
    pygame.quit()
    quit()

# Runs the actual game   
def gameLoop():

    global scorePoints, x, y, ySpeed, xSpeed, xPos, yPos, xSize, ySize, space, obSpeed, ground, done, gOver, pause, listScr, instr, credits
    pause == False
    listScr = False
    instr = False
    credits = False
    if gOver:
        pause=False
# Reset variables to restart the game        
    gOver = False
    if done == True:
        done=False
        scorePoints = 0
        x = 350
        y = 250
        ySpeed = 2
        xSpeed = 0
        xPos =700
        yPos = 0
        xSize = 70
        ySize = randint(0, 350)
        space = 200
        obSpeed = 2.5
        
# -------------- GAME LOGIC --------------------------
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
                pause=False
            if not gOver:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        ySpeed = -10
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_UP:
                        ySpeed = 5

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE and not gOver:
                         pause=True
                         gamePause()

# Background change on difficulty levels                    
        if scorePoints > 4 and scorePoints < 10:
            screen.blit(backgroundImage2, backgroundPosition)
        elif scorePoints > 9:
            screen.blit(backgroundImage3, backgroundPosition)
        else:
            screen.blit(backgroundImage, backgroundPosition)

# Call the draw/write functions        
        dino(x,y)
        obstacle(xPos, yPos, xSize, ySize)
        Score(scorePoints)
        
        y+= ySpeed
        xPos -= obSpeed

# Game over, random, and score logic
        if y > ground or x < 0:
            ySpeed=0
            obSpeed = 0
            gameOver()
            gOver = True

        if x+57 > xPos and y-5 < ySize and x-15 < xSize+xPos:
            gameOver()
            obSpeed = 0
            ySpeed = 0
            gOver = True

        if x+57 > xPos and y+42 > ySize+space and x-15 < xSize+xPos:
            gameOver()
            obSpeed = 0
            ySpeed = 0
            gOver = True

        if xPos < -80:
            xPos = 700
            ySize = randint(0, 350)

        if x > xPos and x < xPos+3 and not gOver:
            scorePoints +=1

        
        pygame.display.flip()
        clock.tick(60)
        
    if gOver:
        scoreTopTen(scorePoints)
        
# --------- MAIN PROGRAM LOOP ------------------------------        
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    
    pygame.display.flip()
    clock.tick(60)
    gameIntro()
pygame.quit()

    
