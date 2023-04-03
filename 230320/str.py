# print("\uD658 \uC601") 아스키 코드 입력해도 나옴

money = int(input("돈 입력하시오 > "))
man_5 = money//50000
man_1 = (money//50000) // 5
man = money//10000
cheon = (money//1000) % 10
baek = (money//100) % 10
won = money % 100

print(man, "만", cheon, "천", baek, "백", won, "원")
print("5만원", man_5, "개 \n", "만원", man_1, "개\n", "천원", cheon, "개\n", "백원", baek, "개")



