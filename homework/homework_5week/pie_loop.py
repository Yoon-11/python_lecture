
for i in range(1, 100001):
    pie_value = 4 * ((-1) ** (i + 1) / (2*i - 1))
    if i % 10000 == 0:
        print(f"i={i}일때 파이값 = {pie_value}")
