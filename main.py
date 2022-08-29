# sum of natural numbers
def fn(n):
    return n * (n + 1) / 2


res = fn(5)
print(res)


def fn2(n):
    sum = 0
    for i in range(1, n + 1):
        sum = sum + i
    return sum


res2 = fn2(5)
print(res2)


def fn3(n):
    sum = 0
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            sum = sum + 1
    return sum


res3 = fn3(5)
print(res3)
