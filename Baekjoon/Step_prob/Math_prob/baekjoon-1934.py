def gcd(a, b):
    i = min(a, b)
    while True:
        if a % i == 0 and b % i == 0:
            return i
        i -= 1


def lcm(a, b):
    return a*b // gcd(a, b)


t = int(input())

for i in range(t):
    a, b = map(int, input().split())
    res = lcm(a, b)
    print(res)
