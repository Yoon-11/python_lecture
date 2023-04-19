from func import gcd

n1 = eval(input("첫번째 정수 입력 >> "))
n2 = eval(input("두번째 정수 입력 >> "))

print(f"{n1}과 {n2}의 최대 공약수는 {gcd(n1, n2)}")