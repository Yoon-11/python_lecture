import random
#
number1 = random.randint(0, 9)
number2 = random.randint(0, 9)

# 덧셈
# answer = eval(input(f"What is {number1} + {number2} ?"))
#
# print(f"{number1} + {number2} = {answer} is {number1+number2 == answer}")

# 뺄셈
if number1 < number2:
    number1, number2 = number2, number1

answer = eval(input(f"What is {number1} - {number2} = ? "))

print(f"{number1} - {number2} = {answer} is {number1 - number2 == answer}")

