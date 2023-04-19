def m(i):
    pi_value = 0
    for i in range(1, i+1):
        pi_value += 4 * (-1) ** (i + 1) / (2 * i - 1)
    print("{:<10} {:.4f}".format(i,pi_value))


for i in range(1, 902, 100):
    m(i)







