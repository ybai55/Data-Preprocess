
def average(a, b):
    return (a + b) / 2.0


def square_root(num, low, high):
    for i in range(20):
        guess = average(low, high)
        if guess ** 2 == num:
            print(guess)
        if guess ** 2 < num:
            low = guess
        if guess ** 2 > num:
            high = guess
    print(guess)

square_root(60, 7, 8)


