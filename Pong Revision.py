from graphics import *
import random
import keyboard
import time

# configuration
width = 550
height = 400
movement = 0.3
scoreWin = 2

win = GraphWin("PONG REVISION", width, height)

#score
playerScore = 0
enemyScore = 0

def main():
    global playerScore, enemyScore
    game = True

    # backgrounds
    background = {}
    background[0] = Rectangle(Point(0,0), Point(width/2,height))
    background[1] = Rectangle(Point(width/2,0), Point(width,height))
    background[0].setFill(color_rgb(25,25,25))
    background[0].setOutline(color_rgb(25,25,25))
    background[1].setFill(color_rgb(35,35,35))
    background[1].setOutline(color_rgb(35,35,35))
    for i in range(len(background)):
        background[i].draw(win)

    # player platform
    player = Rectangle(Point(10,(height/2)-30), Point(20,(height/2)+30))
    player.setFill(color_rgb(245,245,245))
    player.setOutline(color_rgb(245,245,245))
    player.draw(win)

    # enemy player
    enemy = Rectangle(Point(width-20,(height/2)-30), Point(width-10,(height/2)+30))
    enemy.setFill(color_rgb(245,245,245))
    enemy.setOutline(color_rgb(245,245,245))
    enemyY = random.uniform(0,(enemy.p2.getY() - enemy.p1.getY()))
    enemy.draw(win)

    # midde lines
    line = {}
    lineHeight = 0
    i = 0
    while lineHeight < 400:
        line[i] = Line(Point(width/2,0+lineHeight), Point(width/2,5+lineHeight))
        line[i].setOutline(color_rgb(245,245,245))
        lineHeight += 10
        i += 1
    for i in range(len(line)):
        line[i].draw(win)

    # pong
    pong = Rectangle(Point((width/2)-7.5,(height/2)-7.5), Point((width/2)+7.5,(height/2)+7.5))
    pong.setFill("white")
    pong.setOutline("white")
    pong.draw(win)

    # pong speed
    posneg = [-1, 1]
    directionx = random.choice(posneg)
    directiony = random.choice(posneg)
    speed = 0.2
    projy = (random.uniform(0, 0.1488))*directiony
    projx = (speed**2) - (projy**2)
    projx = (projx**0.5)*directionx

    score = {}
    score[0] = Text(Point((width/2)-30,30), playerScore)
    score[1] = Text(Point((width/2)+30,30), enemyScore)
    for i in range(len(score)):
        score[i].setSize(30)
        score[i].setTextColor("white")
        score[i].draw(win)

    time.sleep(1)

    while(game==True): # things that move

        # player control
        if keyboard.is_pressed("w") and player.p1.getY() > 0 and (player.p1.getX() < pong.p2.getX() and pong.p1.getX() < player.p2.getX() and player.p1.getY() < pong.p2.getY() < player.p2.getY())==False:
            player.move(0,-movement)
        elif keyboard.is_pressed("s") and player.p2.getY() < height and (player.p1.getX() < pong.p2.getX() and pong.p1.getX() < player.p2.getX() and player.p1.getY() < pong.p1.getY() < player.p2.getY())==False:
            player.move(0,movement)

        # enemy movement
        if pong.p1.getX() > width/2 and pong.p2.getX() > width/2 and enemy.getP2().getY()-enemyY > pong.getCenter().getY() and enemy.p1.getY() > 0:
            enemy.move(0,-movement)
        elif pong.p1.getX() > width/2 and pong.p2.getX() > width/2 and enemy.getP2().getY()-enemyY < pong.getCenter().getY() and enemy.p2.getY() < height:
            enemy.move(0,movement)

        # ball movement
        pong.move(projx, projy)
        if (player.p1.getY() < pong.p2.getY() and pong.p1.getY() < player.p2.getY() and player.p1.getX() < pong.p1.getX() < player.p2.getX()+1): # bounce off player x axis
            display = pong.getCenter().getY()+7.5 - player.p1.getY()
            if 18.75 < display < 56.25:
                speed = 0.3
            else:
                speed = 0.4
            if display > 37.5:
                display = -display/2
            else:
                display = 37.5-display
            if display < 37.5:
                projy *= -1
            projy = display * 0.005
            projy *= -1
            projx = (((speed**2) - (projy**2))**0.5)

        elif (enemy.p1.getY() < pong.p2.getY() and pong.p1.getY() < enemy.p2.getY() and enemy.p1.getX() < pong.p2.getX() < enemy.p2.getX()): # bounce off enemy x axis
            enemyY = random.uniform(0,(enemy.p2.getY() - enemy.p1.getY()))
            display = pong.getCenter().getY()+7.5 - enemy.p1.getY()
            if 18.75 < display < 56.25:
                speed = 0.3
            else:
                speed = 0.4
            if display >= 37.5:
                display = -display/2
            else:
                display = 37.5-display
            projy = display * 0.005
            if display < 37.5:
                projy *= -1
            projx = (((speed**2) - (projy**2))**0.5)
            projx *= -1

        elif player.getCenter().getY == pong.getCenter().getY() or enemy.getCenter().getY() == pong.getCenter().getY(): # hitting center platform
            projy = 0
            projx = 0.4

        elif pong.p1.getY() <= 0 or pong.p2.getY() >= height: # bounce off wall y axis
            projy = projy * -1

        elif pong.p1.getX() > width: # scoring
            playerScore += 1
            game = False
        elif pong.p2.getX() < 0:
            enemyScore += 1
            game = False

    # win or lose
    if playerScore != scoreWin and enemyScore != scoreWin:
        for i in range(len(background)):
            background[i].undraw()
        for i in range(len(line)):
            line[i].undraw()
        player.undraw()
        enemy.undraw()
        pong.undraw()
        for i in range(len(score)):
            score[i].undraw()
        main()
    else:
        pong.undraw()
        for i in range(len(score)):
            score[i].undraw()
        score[0] = Text(Point((width/2)-30,30), playerScore)
        score[1] = Text(Point((width/2)+30,30), enemyScore)
        for i in range(len(score)):
            score[i].setSize(30)
            score[i].setTextColor("white")
            score[i].draw(win)
        if playerScore == scoreWin: # win message
            playerWin = Text(Point(width/2,height/2), "YOU WON")
            playerWin.setSize(30)
            playerWin.setTextColor("white")
            playerWin.draw(win)
        elif enemyScore == scoreWin:
            enemyWin = Text(Point(width/2,height/2), "GAME OVER") # lose message
            enemyWin.setSize(30)
            enemyWin.setTextColor(color_rgb(245,245,245))
            enemyWin.draw(win)
        time.sleep(2)
        win.close()

main()