n = int(input())

cnt = 0

for i in range(n+1):
    for j in range(60):
        for k in range(60):
            t = '%02d%02d%02d' % (i, j, k)
            if t.find('5') != -1:
                cnt += 1
print(cnt)

