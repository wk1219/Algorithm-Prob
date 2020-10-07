n, m = map(int, input().split())
h = list(map(int, input().split()))

start = 0
end = max(h)
res = 0

while start <= end:
    total = 0
    mid = (start + end) // 2
    for x in h:
        if x > mid:
            total += x - mid
    if total < m:
        end = mid - 1
    else:
        res = mid
        start = mid + 1
print(res)
