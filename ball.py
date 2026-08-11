from turtle import Turtle
from random import randint,choice

class Ball(Turtle):

    def __init__(self,color:str="#0DAB76"):
        super().__init__()
        self.color(color)
        self.shape("circle")
        self.penup()
        self.xMove=10
        self.yMove=10
        self.chooseBallOrientation()


    def chooseBallOrientation(self,interval:tuple=(0,360)):
        """Choose randomly an angle between 0 and 360 to move the ball."""
        listAngles=[45,135,225,315]
        #angle=randint(*interval)
        angle=choice(listAngles)
        if angle == 0 or angle== 90 or angle == 180 or angle ==270:
            angle=45
        self.setheading(angle)

    def bounceY(self):
        """Makes the ball bounce in the Y direction"""
        self.yMove*= -1


    def bounceX(self):
        """Makes the ball bounce in the X direction"""
    
        self.xMove*= -1


    #self.xMove*= -1

        """heading=self.heading()
        if collisionPaddle:
             angle=heading+180
        else:     
            angle=-heading

        self.setheading(angle)"""

    def moveBall(self):
        """Move the ball forward"""
        newX=self.xcor()+self.xMove
        newY=self.ycor()+self.yMove
        self.goto(newX,newY)

        #self.forward(10)
        #print(self.heading())


    def resetBall(self):
        """Reset the ball to the initial position (0,0)"""

        self.home()