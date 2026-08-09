from turtle import Turtle

class Paddle:

    def __init__(self,color:str="white"):
        #super().__init__()   
        #self.color(color)
        self.listSegments:list[Turtle]=[]



    def createPaddle(self,side:str,screenWidth:int,color:str="white"):
        """Create a new paddle. On the left or right side"""
        yPosition=-20
        xPosition=(screenWidth/2) -40
        if side =="left":
            xPosition*=-1
        else:
            pass


        for i in range(5):
            segment=Turtle()
            segment.color(color)
            segment.penup()
            segment.shape("square")
            segment.goto(xPosition,yPosition)
            yPosition+=20
            self.listSegments.append(segment)
            

    def movePaddle(self,direction:str):
        """Move the paddle Up or Down in 20 units."""
        angle=0
        if direction.lower() =="up":
            angle=90
            startPoint=0
            endPoint=len(self.listSegments)-1
            step=1
            #rangeTuple=(0,len(self.listSegments)-1,1)
            

        else:
            angle=270
            startPoint=len(self.listSegments)-1
            endPoint=0
            step=-1
            #rangeTuple=(len(self.listSegments)-1,0,-1)




        for index in range(startPoint,endPoint,step):
            newX=self.listSegments[index+step].xcor()
            newY=self.listSegments[index+step].ycor()
            #self.listSegments[index].setheading(angle)
            self.listSegments[index].speed(10)
            print(f"Index:{index} \n newX:{newX}  newY:{newY}")
            self.listSegments[index].goto(newX,newY)

        self.listSegments[endPoint].setheading(angle)
        self.listSegments[endPoint].forward(20)
        print("------------------")