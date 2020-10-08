import sys
n, m = map(int, sys.stdin.readline().split())
v = list(map(int, sys.stdin.readline().split()))
start = 0
end = max(v)
res = 0

while start <= end:
    tot = 0
    mid = (start + end) // 2
    for i in v:
        if i > mid:
            tot += i - mid
    if tot < m:
        end = mid - 1
    else:
        res = mid
        start = mid + 1

print(res)