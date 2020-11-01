n = int(input())
M = 1000001
p = [False, False] + [True] * (M - 2)


def prime(n):
    for i in range(2, int(M ** 0.5) + 1):
        if p[i]:
            for j in range(i + i, M, i):
                if p[j]:
                    p[j] = False

    res = 0
    for i in range(n, M):
        if i == 1:
            continue
        if str(i)[::-1] == str(i):
            if p[i]:
                res = i
                break
    if res == 0:
        res = 1003001
    return res

print(prime(n))