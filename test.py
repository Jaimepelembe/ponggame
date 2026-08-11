from turtle import Turtle, Screen

screen = Screen()

t1=Turtle()
t1.shape("square")
t1.goto(60,0)


t2=Turtle()
t2.shape("square")

print(f"Distancia entre t1 e t2: {t1.distance(t2)}")

t1.shapesize(stretch_wid=1,stretch_len=4)
t2.goto(120,0)
print(f"Nova Distancia entre t1 e t2: {t1.distance(t2)}")
if t1.distance(t2)==60:
    print("Menor que 20")
screen.mainloop()