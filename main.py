from turtle import Screen
from sideSeparator import SideSeparator

from paddle import Paddle
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





screen=Screen()
screenWidth=800
screenHeight=600
configureScreen(screenWidth,screenHeight,screen)




separator=SideSeparator(screenHeight)
separator.drawSeparator()

paddleLeft = Paddle()
paddleLeft.createPaddle("left",screenWidth)
paddleRight = Paddle()
paddleRight.createPaddle("right",screenWidth)

def moveRightPaddleUp():
    """Move the Right Paddle Up in 20 units. Until it touches the upper line"""
    index=len(paddleRight.listSegments)-1
    maxHeight=(screenHeight/2)-20
    ycor=paddleRight.listSegments[index].ycor()
    if ycor<=maxHeight:
        paddleRight.movePaddle("up")


def moveRightPaddleDown():
    """Move the Right Paddle Down in 20 units. Until it touches the bottom line"""

    maxHeight= -(screenHeight/2)+20
    ycor=paddleRight.listSegments[0].ycor()
    if ycor >= maxHeight:
        paddleRight.movePaddle("down")



def moveLeftPaddleUp():
    """Move the Left Paddle Up in 20 units. Until it touches the upper line"""
    index=len(paddleLeft.listSegments)-1
    maxHeight=(screenHeight/2)-20
    ycor=paddleLeft.listSegments[index].ycor()
    if ycor<=maxHeight:
        paddleLeft.movePaddle("up")


def moveLeftPaddleDown():
    """Move the Left Paddle Down in 20 units. Until it touches the bottom line"""

    maxHeight= -(screenHeight/2)+20
    ycor=paddleLeft.listSegments[0].ycor()
    if ycor >= maxHeight:
        paddleLeft.movePaddle("down")


#Event listener
screen.listen()
screen.onkey(closeWindow,"Escape")
screen.onkeypress(moveRightPaddleUp,"Up")
screen.onkeypress(moveRightPaddleDown,"Down")
screen.onkeypress(moveLeftPaddleUp,"w")
screen.onkeypress(moveLeftPaddleDown,"s")
#screen.onkeypress()
#screen.onkey(turnRight,"Right")
#screen.onkey(turnUp,"Up")
#screen.onkey(turnDown,"Down")

playGame=True

while playGame:
    while True:
        time.sleep(0) #0.075
        screen.update()






#closeWindow() # Close the screen
screen.mainloop()