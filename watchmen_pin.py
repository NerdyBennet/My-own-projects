from turtle import *
import turtle
#the result should look something like this:
"""⬜⬜⬜⬜⬜⬜⬜🟨🟨🟨🟨🟨🟨🟨🟨🟨⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬜🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨⬜⬜⬜⬜⬜
⬜⬜⬜⬜🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨⬜⬜⬜⬜
⬜⬜⬜🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨⬜⬜⬜
⬜⬜🟨🟥🟥🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨⬜⬜
⬜🟨🟨🟥🟥🟥🟨⬛🟨🟨🟨🟨🟨🟨🟨⬛🟨🟨🟨🟨🟨🟨⬜
⬜🟨🟨🟥🟥🟥🟥🟥⬛🟨🟨🟨🟨🟨⬛⬛🟨🟨🟨🟨🟨🟨⬜
⬜🟨🟨🟨🟥🟥🟥⬛⬛🟨🟨🟨🟨🟨⬛⬛🟨🟨🟨🟨🟨🟨⬜
🟨🟨🟨🟨🟨🟥🟥🟥⬛🟨🟨🟨🟨🟨⬛⬛🟨🟨🟨🟨🟨🟨🟨
🟨🟨🟨🟨🟨🟥🟨⬛🟥🟨🟨🟨🟨🟨⬛⬛🟨🟨🟨🟨🟨🟨🟨
🟨🟨🟨🟨🟨🟨🟨⬛🟥🟨🟨🟨🟨🟨🟨⬛🟨🟨🟨🟨🟨🟨🟨
🟨🟨🟨🟨🟨🟨🟨🟨🟨🟥🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨
🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟥🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨
🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨
🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨
⬜🟨🟨🟨🟨⬛🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨⬛🟨🟨🟨🟨⬜
⬜🟨🟨🟨⬛⬛🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨⬛⬛🟨🟨🟨⬜
⬜🟨🟨🟨🟨🟨⬛🟨🟨🟨🟨🟨🟨🟨🟨🟨⬛🟨🟨🟨🟨🟨⬜
⬜⬜🟨🟨🟨🟨🟨⬛⬛⬛🟨🟨🟨⬛⬛⬛🟨🟨🟨🟨🟨⬜⬜
⬜⬜⬜🟨🟨🟨🟨🟨🟨🟨⬛⬛⬛🟨🟨🟨🟨🟨🟨🟨⬜⬜⬜
⬜⬜⬜🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨⬜⬜⬜
⬜⬜⬜⬜⬜🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬜🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨⬜⬜⬜⬜⬜⬜
⬜⬜⬜⬜⬜⬜⬜⬜🟨🟨🟨🟨🟨🟨🟨⬜⬜⬜⬜⬜⬜⬜⬜
"""
#smiley face/background
bgcolor("white")
penup()
goto(-20,-130)
pendown()
turtle.color("#dfc612")
turtle.begin_fill()
circle(180)
turtle.end_fill()

#eyes of the pin
color("black")
penup()
right(90)
goto(35,155) #right eye of  the pin
width(20)
pendown()
forward(90)
penup()
goto(-70,155) #left eye of the pin
pendown()
forward(90)

#blood
penup()
color("red")
left(45)
goto(-143,140)
pendown()
turtle.color("#c22319")
turtle.begin_fill()
circle(20)
turtle.end_fill()
penup()
width(15)
goto(-150,162)#longest blood line
pendown()
forward(200)
penup()
goto(-150,162)#2nd longest blood line
width(12)
right(15)
pendown()
forward(75) 
goto(-150,162)#3rd blood line
right(15)
width(10)
forward(60)
goto(-140,162)#4th blood line
left(90)
right(45)
width(9)
forward(60)
penup()

#mouth
goto(-95, -20)
pendown()
color("black")
right(20)
circle(100, 100)
print(pos()) #58.21,-20.00
right(90)
forward(10)
right(180)
forward(20)
penup()
goto(-95, -20)
pendown()
right(90)
forward(10)
right(180)
forward(20)
#:)
exitonclick()
