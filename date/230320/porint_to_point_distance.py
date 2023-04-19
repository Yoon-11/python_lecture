import math

x1, y1 = eval(input("x1,y1 값을 입력하시오"))
x2, y2 = eval(input("x2,y2 값을 입력하시오"))
x3, y3 = eval(input("x3,y3 값을 입력하시오"))

distance_a = math.sqrt((x1-x2)*(x1-x2) + (y1-y2)*(y1-y2))
distance_b = math.sqrt((x1-x3)*(x1-x3) + (y1-y3)*(y1-y3))
distance_c = math.sqrt((x3-x2)*(x3-x2) + (y3-y2)*(y3-y2))

angle_a = math.degrees(math.acos(distance_a * distance_a - distance_b * distance_b - distance_c * distance_c)/(-2 * distance_b * distance_c))

print(angle_a)