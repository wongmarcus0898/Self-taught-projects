from graphics import *
from threading import Timer
import keyboard, random, time

# configurations
width = 400
gridHeight = width
height = 470
timer = False
game = True
score = 0
bonus = 0
x = 70
y = 30
radius = 10
length = radius * 2
playerLength = 3
poisonLength = playerLength
i = 0
k = 0
pointRadius = 5
points = False
cherryPoints = False
key = "Right"
countDown = 0

# set coordinations
cX = 90
cY = 30
coordX = [10]
coordY = [10]
while coordX[len(coordX)-1] != width-10:
    cX+=20
    coordX.append(cX)
while coordY[len(coordY)-1] != 390:
    cY+=20
    coordY.append(cY)
randomX = random.choice(coordX)
randomY = random.choice(coordY)
cherryRandomX = random.choice(coordX)
cherryRandomY = random.choice(coordY)
poisonRandomX = random.choice(coordX)
poisonRandomY = random.choice(coordY)

# window set up
win = GraphWin("SNAKE", width, height, autoflush = False)
win.setBackground(color_rgb(15,15,15))

# grid
lineX = 20
while lineX < width:
    gridX = Line(Point(lineX,0),Point(lineX,gridHeight))
    gridX.setOutline(color_rgb(25,25,25))
    gridX.draw(win)
    lineX += 20
lineY = 20
while lineY <= gridHeight:
    gridX = Line(Point(0,lineY),Point(width,lineY))
    gridX.setOutline(color_rgb(25,25,25))
    gridX.draw(win)
    lineY += 20

# snake banner
UI = Rectangle(Point(0,400),Point(width,height))
UI.setFill(color_rgb(102,51,0))
UI.setOutline(color_rgb(102,51,0))
UI.draw(win)
snakeTitle = Text(Point(width/2,420),"SNAKE")
snakeTitle.setTextColor("green")
snakeTitle.setSize(20)
snakeTitle.draw(win)
scoreTitle = Text(Point(320,424),"SCORE")
scoreTitle.setTextColor("white")
scoreTitle.setSize(10)
scoreTitle.draw(win)
scoreUI = Text(Point(320,435),score)
scoreUI.setTextColor("white")
scoreUI.setSize(10)
scoreUI.draw(win)

# make player
player = {}
player[0] = Rectangle(Point(x-20-radius,y-radius), Point(x-20+radius, y+radius))
player[1] = Rectangle(Point(x-40-radius,y-radius), Point(x-40+radius, y+radius))
player[2] = Rectangle(Point(x-60-radius,y-radius), Point(x-60+radius, y+radius))

# make poison
poison = {}

def main():
    global timer, scoreUI, score, bonus, playerLength, poisonLength, x, y, points, cherryPoints, randomX, randomY, cherryRandomX, cherryRandomY, poisonRandomX, poisonRandomY, key, countDown, k, game

    while(game==True):
        # score update
        scoreUI.undraw()
        scoreUI = Text(Point(320,435),score)
        scoreUI.setTextColor("white")
        scoreUI.setSize(10)
        scoreUI.draw(win)

        # generating new body blocks
        if len(player) < playerLength:
            i+=1
            player[i] = player[i-1].clone()

        # body following player
        player[0].undraw()
        for i in range(1,len(player)):
            player[len(player)-i].undraw()
            player[len(player)-i] = player[len(player)-i-1].clone()
            player[len(player)-i].draw(win)

        # update player's head coordinate
        player[0] = Rectangle(Point(x-radius,y-radius), Point(x+radius,y+radius))
        player[0].setFill("green")
        player[0].setWidth(2)
        player[0].draw(win)

        # player movement
        if keyboard.is_pressed("Up") and key != "Down":
            key = "Up"
        elif keyboard.is_pressed("Left") and key != "Right":
            key = "Left"
        elif keyboard.is_pressed("Down") and key != "Up":
            key = "Down"
        elif keyboard.is_pressed("Right") and key != "Left":
            key = "Right"
        if key == "Up":
            y -= length
        elif key == "Left":
            x -= length
        elif key == "Down":
            y += length
        elif key == "Right":
            x += length

        # point
        if points == False: # generates new point when eaten
            point = Rectangle(Point(randomX-pointRadius,randomY-pointRadius),Point(randomX+pointRadius,randomY+pointRadius))
            point.setFill("white")
            point.setWidth(2)
            point.draw(win)
            points = True
        if player[0].getCenter().getX() == point.getCenter().getX() and player[0].getCenter().getY() == point.getCenter().getY(): # when player eats the point
            point.undraw()
            playerLength += 1
            poisonLength += 1
            score += 200+bonus
            randomX = random.choice(coordX)
            randomY = random.choice(coordY)
            for i in range(len(player)):
                if (point.getCenter().getX() == player[i].getCenter().getX() and point.getCenter().getY() == player[i].getCenter().getY()) or (cherryPoints == True and cherryPoint.getCenter().getX() == point.getCenter().getX() and cherryPoint.getCenter().getY() == point.getCenter().getY()): # regenerate x and y coordinate if they share the same coordinate as player and cherry
                    randomX = random.choice(coordX)
                    randomY = random.choice(coordY)
            for i in range(len(poison)): # regenerate x and y coordinate if point shares the same coordinate to other array of poisons
                if point.getCenter().getX() == poison[i].getCenter().getX() and point.getCenter().getY() == poison[i].getCenter().getY():
                    cherryRandomX = random.choice(coordX)
                    cherryRandomY = random.choice(coordY)
            points = False

        # cherry
        if countDown == 150:
            countDown = 0
            if cherryPoints == False: # generates new cherry from countdown
                cherryPoint = Rectangle(Point(cherryRandomX-pointRadius,cherryRandomY-pointRadius),Point(cherryRandomX+pointRadius,cherryRandomY+pointRadius))
                cherryPoint.setFill(color_rgb(213,0,50))
                cherryPoint.setWidth(2)
                cherryPoint.draw(win)
                cherryPoints = True
        if cherryPoints == True:
            for i in range(2, 6): # cherry blinks between countdown 40 to 100
                if countDown == 20*i:
                    cherryPoint.undraw()
                elif countDown == 10+(20*i):
                    cherryPoint.draw(win)
            if countDown >= 100: # when countdown becomes 100, remove cherry and reset count down
                cherryPoints = False
                countDown = 0
                cherryRandomX = random.choice(coordX)
                cherryRandomY = random.choice(coordY)
        if cherryPoints==True and player[0].getCenter().getX() == cherryPoint.getCenter().getX() and player[0].getCenter().getY() == cherryPoint.getCenter().getY(): # when player eats the cherry
            cherryPoint.undraw()
            score += 500
            cherryRandomX = random.choice(coordX)
            cherryRandomY = random.choice(coordY)
            for i in range(len(player)):
                if (cherryPoint.getCenter().getX() == player[i].getCenter().getX() and cherryPoint.getCenter().getY() == player[i].getCenter().getY()) or (cherryPoint.getCenter().getX() == point.getCenter().getX() and cherryPoint.getCenter().getY() == point.getCenter().getY()): # regenerate x and y coordinate if they share the same coordinate as player and point
                    cherryRandomX = random.choice(coordX)
                    cherryRandomY = random.choice(coordY)
            for i in range(len(poison)): # regenerate x and y coordinate if cherry shares the same coordinate to other array of poisons
                if cherryPoint.getCenter().getX() == poison[i].getCenter().getX() and cherryPoint.getCenter().getY() == poison[i].getCenter().getY():
                    cherryRandomX = random.choice(coordX)
                    cherryRandomY = random.choice(coordY)
            cherryPoints = False

        # poison
        if poisonLength % 5 == 0: # generates a poison block each time the player size reaches the multiple of 5
            poison[k] = Rectangle(Point(poisonRandomX-pointRadius,poisonRandomY-pointRadius),Point(poisonRandomX+pointRadius,poisonRandomY+pointRadius))
            poison[k].setFill("green")
            poison[k].setWidth(2)
            poison[k].draw(win)
            poisonRandomX = random.choice(coordX)
            poisonRandomY = random.choice(coordY)
            for i in range(len(player)):
                if (poison[k].getCenter().getX() == player[i].getCenter().getX() and poison[k].getCenter().getY() == player[i].getCenter().getY()) or (poison[k].getCenter().getX() == point.getCenter().getX() and poison[k].getCenter().getY() == point.getCenter().getY()) or (cherryPoints==True and poison[k].getCenter().getX() == cherryPoint.getCenter().getX() and poison[k].getCenter().getY() == cherryPoint.getCenter().getY()): # regenerate x and y coordinate if they share the same coordinate as player and point and cherry
                    poisonRandomX = random.choice(coordX)
                    poisonRandomY = random.choice(coordY)
            for i in range(len(poison)):
                if poison[k].getCenter().getX() == poison[i].getCenter().getX() and poison[k].getCenter().getY() == poison[i].getCenter().getY(): # regenerate x and y coordinate if new poison shares the same coordinate to other array of poisons
                    poisonRandomX = random.choice(coordX)
                    poisonRandomY = random.choice(coordY)
            bonus+=50
            k+=1
            poisonLength+=1

        # game over requirements
        for i in range(len(poison)): # if player touches poison
            if player[0].getCenter().getX() == poison[i].getCenter().getX() and player[0].getCenter().getY() == poison[i].getCenter().getY():
                game = False
        for i in range(2, len(player)): # if player touches its own body or reach out of window
            if (player[0].getCenter().getX() == player[i].getCenter().getX() and player[0].getCenter().getY() == player[i].getCenter().getY()) or x < 0 or x > width or y < 0 or y > gridHeight:
                game = False

        # FPS
        update(10)
        countDown += 1


    # GAME OVER
    gameOver = Text(Point(width/2,200), "GAME OVER")
    gameOver.setTextColor("red")
    gameOver.setSize(30)
    gameOver.draw(win)
    update()
    time.sleep(2)
    win.close()

main()