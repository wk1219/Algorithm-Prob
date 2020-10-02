n, m, k = map(int, input().split())
x = list(map(int, input().split()))

x.sort()
first = x[n-1]
second = x[n-2]
res = 0
cnt = 0
while True:
    for i in range(0, k):
        if cnt == m:
            break
        res += first
        cnt += 1
    if cnt == m:
        break
    res += second
    cnt += 1

print(res)