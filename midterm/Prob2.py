n = int(input("숫자를 입력하세요: "))

# 1부터 n까지 증가하며 출력
for i in range(1, n+1):
    for j in range(1, i+1):
        print(j, end='')
    print()

# n-1부터 1까지 감소하며 출력
for i in range(n-1, 0, -1):
    for j in range(1, i+1):
        print(j, end='')
    print()
