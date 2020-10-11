n = input().split('-')
res = 0

for i in n[0].split('+'):
    res += int(i)

for i in n[1:]:
    for j in i.split('+'):
        res -= int(j)
        print(j)
print(res)