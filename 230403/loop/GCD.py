n1 = eval(input("첫번째 숫자 입력 >> "))
n2 = eval(input("두번째 숫자 입력 >> "))

god = 1
k = 2

while k <= n1 and k <= n2:
    if n1 % k == 0 and n2 % k == 0:
        god = k
    k += 1

print(f"최대공약수는 {god}")

