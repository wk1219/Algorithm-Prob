n, m = map(int, input().split())

res = 0
for i in range(0, n):
    s = list(map(int, input().split()))
    min_card = min(s)
    res = max(res, min_card)

print(res)