from turtle import Turtle #,Screen
class SideSeparator(Turtle):

    def __init__(self,screenHeight,color:str="white"):
        super().__init__()
        self.screenHeight=screenHeight
        self.pencolor(color)

    def drawSeparator(self):
        """Draws the side separator"""
        position=-(self.screenHeight/2)
        self.hideturtle()
        self.setheading(90)
        self.penup()
        self.goto(0,position)
        self.pendown()
        self.pensize(5)
        steps=20
        #self.speed("fastest")

        while position <self.screenHeight/2:
            self.forward(steps)
            self.penup()
            self.forward(steps)
            self.pendown()
            position+=2*steps
            self.goto(0,position)

"""
screen=Screen()
screen.bgcolor("black")
screen.setup(800,600)

side=SideSeparator(600)
side.drawSeparator()

screen.mainloop()"""