from math import sqrt


def equation(a, b, c, d):
    """
    for formula like ax + b = cx + d
    then x = (d-b) / (a-c)
    """
    return (d - b) / (a - c)


def quad(a, b, c):
    """
    a * x^2 + b*x + c = 0
    x = (-b +- (b^2-4ac)^1/2) / 2a
    """
    x1 = (-b + sqrt(b**2 - 4*a*c)) / (2*a)
    x2 = (-b - sqrt(b**2 - 4*a*c)) / (2*a)
    return x1, x2


x1, x2 = quad(2, 7, -15)
print(x1, x2)

