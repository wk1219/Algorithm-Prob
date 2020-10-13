n, k = map(int, input().split())
p = 1000000007


def power(a, b, m):
    res = 1
    while b > 0:
        if b % 2 != 0:
            res = (res * a) % m
        b //= 2
        a = (a * a) % m
    return res


a = 1
b = 1
for i in range(1, n+1):
    a *= i
    a %= p
for i in range(1, k+1):
    b *= i
    b %= p
for i in range(1, n-k+1):
    b *= i
    b %= p


res = power(b, (p-2), p)
print((a * res) % p)
