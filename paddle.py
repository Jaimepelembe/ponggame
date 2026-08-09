from turtle import Turtle

class Paddle(Turtle):

    def __init__(self,screenWidth:int,screenHeight:int):
        super().__init__()  
        self.screenWidth=screenWidth 
        self.screenHeight=screenHeight


    def createPaddle(self,side:str,color:str="white"):
        """Create a new paddle. On the left or right side"""
        yPosition=0
        xPosition=(self.screenWidth/2) -40
        if side =="left":
            xPosition*=-1
        else:
            pass

         
        self.color(color)
        self.penup()
        self.shape("square")
        self.shapesize(stretch_wid=5,stretch_len=1)
        self.goto(xPosition,yPosition)
        
     

    def moveUP(self):
        """Move the paddle Up or Down in 20 units."""
      
        ycor=self.ycor()
        maxHeight=(self.screenHeight/2)-80
        if ycor < maxHeight:   
            newYcor=ycor+20
            self.sety(newYcor)
        

    def moveDown(self):
        """Move the paddle Down in 20 units."""

        ycor=self.ycor()
        maxHeight= -(self.screenHeight/2)+80
        if ycor > maxHeight:   
            newYcor=ycor-20
            self.sety(newYcor)
  