n = int(input())

arr = (list(map(int, input().split())))
arr = sorted(arr)
r = []
res = 0
p = 0
for i in arr:
    p += i
    r.append(p)
    res += p

print(res)