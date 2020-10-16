n = int(input())
m = list(map(int, input().split()))

m.sort()
res = m[0] * m[len(m) - 1]
print(res)