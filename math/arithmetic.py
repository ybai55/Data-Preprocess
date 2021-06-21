

def summation(num):
    res = 0
    for i in range(1, num + 1):
        res += i
    print(res)


def average_list(li):
    return sum(li) / len(li)

d = [53, 28, 54, 84, 65, 60, 22, 93, 62, 27, 16, 25, 74, 42, 4, 42,
15, 96, 11, 70, 83, 97, 75]

print(average_list(d))

# summation(1000)
