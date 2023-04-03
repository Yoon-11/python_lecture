import turtle
x, y = eval(input("x, y 값을 입력하세요 :"))
radius = eval(input("반지름 값을 입력하세요 :"))

area = radius * radius * 3.14

turtle.penup()
turtle.goto(x, y)
turtle.down()
turtle.circle(radius)
turtle.write(area)
turtle.done()
