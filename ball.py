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
        self.ballSpeed=0.07


    def chooseBallOrientation(self,interval:tuple=(0,360)):
        """Choose randomly an orientation."""
        listAngles=[45,135,225,315]
        angle=choice(listAngles)
        self.setheading(angle)

    def bounceY(self):
        """Makes the ball bounce in the Y direction"""
        self.yMove*= -1


    def bounceX(self):
        """Makes the ball bounce in the X direction"""   
        self.xMove*= -1

    def moveBall(self):
        """Move the ball forward"""
        newX=self.xcor()+self.xMove
        newY=self.ycor()+self.yMove
        self.goto(newX,newY)


    def resetBall(self):
        """Reset the ball to the initial position (0,0)"""
        self.home()
        self.bounceX()
        self.ballSpeed=0.07

    def increaseBallSpeed(self):
        """Increases the speed of the ball"""
        if self.ballSpeed > 0:
            self.ballSpeed-= 0.005125#625