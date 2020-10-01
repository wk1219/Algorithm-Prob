n, k = map(int, input().split())
wons = []
cnt = 0

for i in range(0, n):
    x = int(input())
    wons.append(x)

a = wons.reverse()
res = 0
for won in wons:
    cnt += k
    s = int(k / won)
    res += s
    k %= won

print(res)