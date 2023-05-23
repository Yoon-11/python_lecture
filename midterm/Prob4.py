def water(num_people, bottles_per_person):
    total_bottles = num_people * bottles_per_person
    total_cost = (total_bottles // 15) * 10000 + (total_bottles % 15) * 900
    return total_cost

def pizza(num_people):
    total_pizza = (num_people + 3) // 4
    total_cost = total_pizza * 12000
    return total_cost


num_people = int(input("인원수를 입력하세요: "))
bottles_per_person = int(input("한 사람당 마실 생수의 개수를 입력하세요: "))



water_cost = water(num_people, bottles_per_person)


pizza_cost = pizza(num_people)


total_cost = water_cost + pizza_cost


print(f"필요한 생수 개수 {num_people * bottles_per_person}개")
print(f"생수 팩 구매량 {num_people * bottles_per_person // 15}개 = {num_people * bottles_per_person // 15 * 10000}원")
print(f"생수 낱개 구매량 {num_people * bottles_per_person % 15}개 = {num_people * bottles_per_person % 15 * 900}원")
print(f"생수 총 구매 비용 = {water_cost}원")
print(f"주문 피자 개수 {(num_people + 3) // 4}판")
print(f"총 피자 가격: {pizza_cost}원")

print(f"총 지출액 = {total_cost}원")
