from turtle import *
import turtle

penup()
bgcolor("black")
pencolor("red")
goto(0,0)
left(45)
width(19)
pendown()
forward(140)
left(90)
forward(70)
penup()
goto(0,0)
pendown()
forward(140)
right(90)
forward(70)
penup()

# middle part of the brand of sacrifice + lower half
goto(0,0)
left(45)
pendown()
width(17)
forward(180)
print(pos())
penup()
goto(0,150)
width(15)
pendown()
left(35)
forward(30)
penup()
goto(0,150)
pendown()
right(70)
forward(30)
penup()
goto(0,0)
turtle.setheading(0) # resets the pointers position
right(90)
pendown()
forward(185)
goto(0,0)
right(45)
forward(140)
left(90)
forward(140)
left(90)
forward(140)
left(90)
forward(140)
penup()
goto(100,1000)

exitonclick()