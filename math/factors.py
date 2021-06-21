

def factor(num):
    factor_list = []
    for i in range(1, num + 1):
        if num % i == 0:
            factor_list.append(i)
    return factor_list


def gcf(num1, num2):
    fact1 = factor(num1)
    fact2 = factor(num2)
    gf = 1
    for i in fact1:
        if i in fact2 and i > gf:
           gf = i

    return gf


print(gcf(150, 138))
