def gcd(a, b):
    while b != 0:
        temp = a % b
        a = b
        b = temp
    return a


def lcm(a, b):
    return (a * b) // gcd(a, b)


n = int(input())
d = []
for i in range(n):
    x, y = map(int, input().split())
    d.append((x, y))

for i in range(n):
    print(lcm(d[i][0], d[i][1]))