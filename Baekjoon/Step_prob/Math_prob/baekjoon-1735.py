def gcd(a, b):
    while b != 0:
        temp = a % b
        a = b
        b = temp
    return a


u1, d1 = map(int, input().split())
u2, d2 = map(int, input().split())

u = u1 * d2 + u2 * d1
d = d1 * d2

g = gcd(d1, d2)
d = d // g
u = u // g

gg = gcd(u, d)
print(u // gg, d // gg)