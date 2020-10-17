import sys


n = int(sys.stdin.readline())
res = n
for i in range(2, int(n ** 0.5) + 1):   # shorten time (root)
    if n % i == 0:
        while n % i == 0:
            n //= i
        res *= 1 - (1 / i)

if n > 1:
    res *= 1 - (1 / n)
print(int(res))


