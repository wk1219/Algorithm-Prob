m = int(input())
n = int(input())

res = []
s = 0

for i in range(0, n):
    if n >= pow(i, 2) >= m:
        res.append(pow(i, 2))
        s += pow(i, 2)

if len(res) != 0:
    print(s)
    print(min(res))
else:
    print(-1)