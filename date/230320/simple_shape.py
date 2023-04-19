import turtle
turtle.pensize(3)

turtle.penup()
turtle.goto(-150, 50)
turtle.pendown()
turtle.circle(40, steps=3)

turtle.penup()
turtle.goto(-50, 50)
turtle.pendown()
turtle.circle(40, steps=4)

turtle.penup()
turtle.goto(50, 50)
turtle.pendown()
turtle.circle(40, steps=5)

turtle.penup()
turtle.goto(150, 50)
turtle.pendown()
turtle.circle(40, steps=6)

turtle.penup()
turtle.goto(250, 50)
turtle.pendown()
turtle.circle(40)

turtle.done()
