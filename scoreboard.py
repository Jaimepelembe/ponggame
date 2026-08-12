from turtle import Turtle

class ScoreBoard(Turtle):

    def __init__(self,xPosition:int,yPosition:int,font:tuple=('Arial',14,'bold'),color:str="white",text:str="0"):
        super().__init__()
        self.score=0
        self.color(color)
        self.penup()
        self.hideturtle()
        self.setx(xPosition)
        self.sety(yPosition)
        self.font:tuple=font
        self.writeText(argument=text)
  

    def writeText(self,argument:str="",move:bool=False,align:str="center"):
        """Write the text into the score board"""
        self.write(argument,move,align,self.font)

    def increaseScore(self):
        """Increase the game score in one point."""
        self.score+=1
        self.clear()
        self.writeText(argument=f"{self.score}")



    def resetScore(self):
        """Reset the game score to 0"""
        self.score=0
        self.clear()
        self.color("white")
        self.writeText("0")
        #self.createScoreBoard()

    def gameOver(self,position:str,color:str="#FBAF00"):
        """Write game over on the screen"""
        self.goto(0,0)
        self.clear()
        self.font=('Arial',18,'bold')
        self.color(color)
        self.writeText(argument=f"Game Over.\nThe winner is the {position} player")



"""
screen=Screen()

score=ScoreBoard(600)

#screen.bgcolor("black")
screen.mainloop()
"""