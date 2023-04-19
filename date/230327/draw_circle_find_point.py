import turtle
import math

r = eval(input("반지름 값 입력 >> "))
center_x, center_y = eval(input("원의 중심 값 x, y값 입력 >> "))
point_x, point_y = eval(input("한점 값 x, y값 입력 >> "))
distance = math.sqrt((center_x-point_x) * (center_x-point_x) + (center_y-point_y) * (center_y-point_y))

turtle.penup()
turtle.goto(center_x, center_y)
turtle.pendown()
turtle.circle(r)

if r == distance:
    turtle.write("원 위에 있음")
elif r > distance:
    turtle.write("원 안에 있음")
else:
    turtle.write("원 밖에 있음")

turtle.done()
