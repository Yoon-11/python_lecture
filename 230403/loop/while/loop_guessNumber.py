import random
import time

correctCount = 0
count = 0
NUMBER_OF_QUESTION = 5

start_time = time.time()

while count < NUMBER_OF_QUESTION:
    num_1 = random.randint(0, 9)
    num_2 = random.randint(0, 9)

    if num_1 > num_2:
        num_1, num_2 = num_2, num_1

    question = eval(input(f"{num_2} - {num_1}의 결과값은?"))

    if question == num_2 - num_1:
        print("정답입니다")
        break
    else:
        print("틀렸습니다")

    if count > NUMBER_OF_QUESTION:
        print("기회 끝남")
        exit()
        
    count += 1

end_time = time.time()

print(f"정답을 맞추기까지 {end_time - start_time} 걸렸습니다")
