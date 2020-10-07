a = []
for i in range(4):
    a.append(list(map(int, input().split())))

m = 0
res = []
result = []
for i in range(4):
    res.append(a[i][1] - a[i][0])
    m += res[i]
    result.append(m)
print(max(result))



