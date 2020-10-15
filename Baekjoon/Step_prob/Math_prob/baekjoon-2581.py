m = int(input())
n = int(input())

s = [x for x in range(m, n + 1)]
res = []


def prime(num):
    if num < 2:
        return False

    for i in range(2, num):
        if num % i == 0:
            return False
    return True


for i in range(n - m + 1):
    if prime(s[i]):
        res.append(s[i])

if len(res) == 0:
    print(-1)
else:
    print(sum(res))
    print(min(res))