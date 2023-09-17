from turtle import *
print("hello Mr.Keshelava")


#the walls of the house
color("grey")
width(7)
forward(200) 
left(90)
forward(200)
left(90)
forward(200)
left(90)
forward(200)
left(90)
forward(70)

#the door of the house
color("red")
begin_fill()
left(90)
forward(100)
right(90)
forward(50)
right(90)
forward(100)
end_fill()

penup()
goto(200, 200)
pendown()

#the roof of the house
color("blue")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()

penup()
goto(150, 150)
pendown()

#the first window of the house
color("purple")
begin_fill()
left(30)
forward(30)
left(90)
forward(30)
left(90)
forward(30)
left(90)
forward(30)
end_fill()

penup()
goto(50, 150)
pendown()

#the second window of the house
color("purple")
begin_fill()
forward(30)
left(90)
forward(30)
left(90)
forward(30)
left(90)
forward(30)
end_fill()

exitonclick()