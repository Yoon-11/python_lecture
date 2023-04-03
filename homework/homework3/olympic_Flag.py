import turtle

r = int(input("반지름 값을 입력하세요 > "))
turtle.pensize(3)
turtle.penup()
turtle.goto(-100, 50)   # 시작점

# 위쪽 원
turtle.pendown()
turtle.color("blue")
turtle.circle(r)

turtle.penup()
turtle.goto(-80 + (2*r), 50)
turtle.pendown()
turtle.color("black")
turtle.circle(r)

turtle.penup()
turtle.goto(-60 + (4*r), 50)
turtle.pendown()
turtle.color("red")
turtle.circle(r)


# 아래쪽 원
turtle.penup()
turtle.goto((-180 + (2*r)) / 2, 40 - r)
turtle.pendown()
turtle.color("yellow")
turtle.circle(r)

turtle.penup()
turtle.goto((-140 + (6*r)) / 2, 40 - r)
turtle.pendown()
turtle.color("green")
turtle.circle(r)

turtle.done()

