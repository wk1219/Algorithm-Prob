a, b, c = map(int, input().split())


def power(a, b, m):
    res = 1
    while b > 0:
        if b % 2 != 0:
            res = (res * a) % m
        b //= 2
        a = (a * a) % m
    return res


print(power(a, b, c))