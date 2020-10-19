N = 123456 * 2 + 1
a = [1] * N

for i in range(2, int(N ** 0.5) + 1):
    if a[i]:
        for j in range(2 * i, N, i):
            a[j] = 0


def prime(n):
    cnt = 0
    for i in range(n + 1, 2 * n + 1):
        if a[i]:
            cnt += 1
    print(cnt)


while True:
    n = int(input())
    if n == 0:
        break
    prime(n)



