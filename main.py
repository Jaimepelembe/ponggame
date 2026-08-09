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

paddleLeft = Paddle(screenWidth,screenHeight)
paddleLeft.createPaddle("left")
paddleRight = Paddle(screenWidth,screenHeight)
paddleRight.createPaddle("right")




#Event listener
screen.listen()
screen.onkey(closeWindow,"Escape")
screen.onkeypress(paddleRight.moveUP,"Up")
screen.onkeypress(paddleRight.moveDown,"Down")
screen.onkeypress(paddleLeft.moveUP,"w")
screen.onkeypress(paddleLeft.moveDown,"s")
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