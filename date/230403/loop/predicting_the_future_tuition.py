price = 10000
price2 = price * 2

year = 0

while price < price2:
    price *= 1.07
    year += 1

print(f"{year}년 후에 등록금이 2배")
