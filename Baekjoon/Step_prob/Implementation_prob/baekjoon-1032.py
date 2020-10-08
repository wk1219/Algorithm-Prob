n = int(input())
d = []
for i in range(n):
    d.append(input())
c = list(d[0])

for i in range(n):
    for j in range(len(c)):
        if c[j] == d[i][j]:
            continue
        else:
            c[j] = '?'
print(''.join(c))