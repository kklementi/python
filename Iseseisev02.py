#Karel Klementi

#Iseseisev töö 2

import turtle
turtle.pensize(2)
turtle.lt(90)
for i in range (5):
    turtle.fd(50)
    for i in range (3):
        turtle.rt(90)
        turtle.fd(100)
    turtle.rt(90)
    turtle.fd(50)
    turtle.rt(72)
turtle.done()