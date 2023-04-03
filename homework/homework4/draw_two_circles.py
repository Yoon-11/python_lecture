import turtle
import math

r1 = eval(input("첫번째 원의 반지름 값 입력 >> "))
center1_x, center1_y = eval(input("첫번째 원의 중심 값 x, y값 입력 >> "))

r2 = eval(input("두번째 원의 반지름 값 입력 >> "))
center2_x, center2_y = eval(input("두번째 원의 중심 값 x, y값 입력 >> "))

# 두 원의 중심 좌표 거리
distance = math.sqrt((center1_x - center2_x) ** 2 + (center1_y - center2_y) ** 2)

turtle.penup()
turtle.goto(center1_x, center1_y)
turtle.pendown()
turtle.circle(r1)

turtle.penup()
turtle.goto(center2_x, center2_y)
turtle.pendown()
turtle.circle(r2)

if abs(r1 - r2) < distance < abs(r1 + r2):
    turtle.write("두 원은 두 점에서 만남")
elif abs(r1+r2) == distance:
    turtle.write("외접함")
elif abs(r1-r2) == distance:
    turtle.write("내접함")
elif abs(r1-r2) > distance or distance == 0:
    turtle.write("원 안에 다른 원이 있음")
elif abs(r1+r2) < distance:
    turtle.write("두 원은 만나지 않는다")

turtle.done()
