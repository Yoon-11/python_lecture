def binaryToDecimal(binaryString):
    decimal = 0
    power = len(binaryString) - 1
    for digit in binaryString:
        decimal += int(digit) * (2 ** power)
        power -= 1
    return decimal

binaryString = input("이진수를 입력하세요: ")

decimal = binaryToDecimal(binaryString)
print("10진수 값은:", decimal)
