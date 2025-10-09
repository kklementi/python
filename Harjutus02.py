#Karel Klementi 09.10.2025

import turtle

#Seaded!
turtle.speed(0)
ekraan = turtle.Screen()
ekraan.title("Olümpiarõngad - Karel")
ekraan.setup(500, 400)

#Orõngad

turtle.pensize(6)

#1

turtle.pencolor("blue")
turtle.penup()
turtle.goto(-110, 0)
turtle.pendown()
turtle.circle(50)

#2

turtle.pencolor("black")
turtle.penup()
turtle.goto(0, 0)
turtle.pendown()
turtle.circle(50)

#3

turtle.pencolor("red")
turtle.penup()
turtle.goto(110, 0)
turtle.pendown()
turtle.circle(50)

#4

turtle.pencolor("yellow")
turtle.penup()
turtle.goto(-55, -55)
turtle.pendown()
turtle.circle(50)

#5

turtle.pencolor("green")
turtle.penup()
turtle.goto(55, -55)
turtle.pendown()
turtle.circle(50)

#valmis rõngad


turtle.done()