import sys

n = []
while True:
    r = int(sys.stdin.readline())
    if r == 0:
        break
    n.append(r)


for i in range(0, len(n)):
    res = n[i]
    for j in range(2, int(n[i] ** 0.5) + 1):
        if n[i] % j == 0:
            while n[i] % j == 0:
                n[i] //= j
            res *= 1 - (1 / j)

    if n[i] > 1:
        res *= 1 - (1 / n[i])
    print(int(res))

