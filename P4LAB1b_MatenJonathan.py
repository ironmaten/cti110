 # Jonathan Maten
 # 20 October 2024
 # P4LAB1
 # This program controls a turtle and makes it draw shapes

import turtle

turtle.shape("turtle")
turtle.color("blue")
turtle.pencolor("green")
turtle.pensize(3)

#Create the J

turtle.right(90)
turtle.forward(50)
turtle.right(45)
turtle.forward(15)
turtle.right(45)
turtle.forward(15)
turtle.right(45)
turtle.forward(25)
turtle.left(225)

#Lift the turtle, reset, and place in position for M

turtle.penup()
turtle.goto(0, 0)
turtle.forward(10)
turtle.right(90)
turtle.forward(60)
turtle.right(180)
turtle.pendown()

#Create the M

turtle.forward(60)
turtle.right(135)
turtle.forward(30)
turtle.left(90)
turtle.forward(30)
turtle.right(135)
turtle.forward(60)
