from turtle import Screen
from sideSeparator import SideSeparator
from ball import Ball
from paddle import Paddle
from scoreboard import ScoreBoard
import time



def closeWindow():
    """Close the screen"""
    screen.bye()


def configureScreen(screenWidth:int,screenHeight:int,screen:Screen,color:str="black",title:str="Pong Game"):
    """Configure the screen"""
    screen.setup(width=screenWidth,height=screenHeight)

    # Make the screen not resizable
    canvas=screen.getcanvas()
    root=canvas.winfo_toplevel()
    root.resizable(False,False)

    screen.bgcolor(color)
    screen.title(title)

    screen.tracer(0) # Turn off the animation


def checkCollisionWithWalls(screenHeight:int,ball:Ball):
    """Check if the ball collided with the top or bottom wall"""

    if ball.ycor() >= (screenHeight/2) -20 or ball.ycor() <= -(screenHeight/2) +20: # We put -20 and +20 because the ball is 20x20
        ball.bounceY()


def checkCollisionWithPaddle(ball:Ball,paddleLeft:Paddle,paddleRight:Paddle):
    """Check if the ball collided with the paddle"""
    limite=screenWidth/2 -65 # 335
    if (ball.distance(paddleRight) < 80 and ball.xcor() >limite and ball.xcor() < limite +10) or (ball.distance(paddleLeft)<80 and ball.xcor() < -limite and ball.xcor() > -limite -10):
        ball.bounceX()
        ball.increaseBallSpeed()
        print(ball.ballSpeed)
    
        

def checkPlayerScore(ball:Ball,scoreBoardRight:ScoreBoard,scoreBoardLeft:ScoreBoard):
    """Check if one of the player has scored one point"""

    limite = (screenWidth/2)
    if ball.xcor() > limite: #The Right player has scored a point
        scoreBoardLeft.increaseScore()
        ball.resetBall()

    elif ball.xcor() < -limite:      #The Left player has scored a point
        scoreBoardRight.increaseScore()
        ball.resetBall()

screen=Screen()
screenWidth=800
screenHeight=600
configureScreen(screenWidth,screenHeight,screen)




separator=SideSeparator(screenHeight)
separator.drawSeparator()

paddleLeft = Paddle(screenWidth,screenHeight)
paddleLeft.createPaddle("left")
paddleRight = Paddle(screenWidth,screenHeight)
paddleRight.createPaddle("right")

ball= Ball()
scoreHeight=screenHeight/2 -80
font=("verdana",32,"bold")
scoreBoardLeft=ScoreBoard(-80,scoreHeight,font)
scoreBoardRight=ScoreBoard(80,scoreHeight,font)

#Event listener
screen.listen()
screen.onkey(closeWindow,"Escape")
screen.onkeypress(paddleRight.moveUP,"Up")
screen.onkeypress(paddleRight.moveDown,"Down")
screen.onkeypress(paddleLeft.moveUP,"w")
screen.onkeypress(paddleLeft.moveDown,"s")


playGame=True

while playGame:
    while True:
        time.sleep(ball.ballSpeed) # Make a pause after each movement of the ball
        screen.update()
        checkCollisionWithWalls(screenHeight,ball)
        checkCollisionWithPaddle(ball,paddleLeft,paddleRight)
        checkPlayerScore(ball,scoreBoardLeft,scoreBoardRight)
        ball.moveBall()






#closeWindow() # Close the screen
screen.mainloop()