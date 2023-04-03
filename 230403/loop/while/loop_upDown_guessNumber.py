import random

number = random.randint(1, 100)

print("0~100까지 중에 숫자를 맞혀보세요")

guess = -1

while guess != number:

    input_value = eval(input("숫자 입력 >> "))

    if input_value == number:
        print("정답입니다")
        break
    elif input_value > number:
        print("DOWN")
    else:
        print("UP")
