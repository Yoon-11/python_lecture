import turtle
import random

x = int(input("중심좌표 x를 입력하세요: "))
y = int(input("중심좌표 y를 입력하세요: "))
r = int(input("반지름을 입력하세요: "))


turtle.penup()
turtle.goto(x, y - r)
turtle.pendown()


turtle.circle(r)


count = 0
for i in range(10):

    x = random.randint(-200, 200)
    y = random.randint(-200, 200)
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.dot(5)


    if (x - turtle.xcor()) ** 2 + (y - turtle.ycor()) ** 2 <= r ** 2:
        count += 1


turtle.penup()
turtle.goto(-150, -250)
turtle.write("원 안에 있는 점의 개수: {}".format(count), font=("Arial", 16, "normal"))
turtle.done()
