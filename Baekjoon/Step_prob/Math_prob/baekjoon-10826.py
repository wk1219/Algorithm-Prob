import sys


def fibo(n):
    fibo = [x for x in range(n + 1)]
    for x in range(2, n + 1):
        fibo[x] = fibo[x - 2] + fibo[x - 1]
    return fibo[n]


t = int(sys.stdin.readline())
print(fibo(t))