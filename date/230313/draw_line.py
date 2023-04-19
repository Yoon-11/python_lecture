# 중간고사 1번

import turtle
x1, y1 = eval(input("Enter value x1, y1 : "))
x2, y2 = eval(input("Enter value x2, y2 : "))

distance = ((x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2)) ** 0.5

turtle.penup()
turtle.goto(x1, y1)
turtle.pendown()
turtle.goto(x2, y2)

turtle.done()