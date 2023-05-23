import random

total_money = 0
keep_rolling = True

while keep_rolling:
    num = random.randint(1, 6)
    money = num * 100
    total_money += money

    print(f"주사위 숫자: {num}, 현재 총 상금 : {total_money}")

    choice = input("한번 더 ? (y/n): ")
    if choice.lower() == "y":
        keep_rolling = True

    elif choice.lower() == "n":
        keep_rolling = False


print(f"최종 총 상금은 {total_money}원 입니다.")

