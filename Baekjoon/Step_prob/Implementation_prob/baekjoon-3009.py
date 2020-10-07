t = []
for i in range(3):
    x, y = map(int, input().split())
    t.append((x, y))
xlist = [t[0][0], t[1][0], t[2][0]]
ylist = [t[0][1], t[1][1], t[2][1]]

for i in xlist:
    if xlist.count(i) == 1:
        x = i
for i in ylist:
    if ylist.count(i) == 1:
        y = i
print(x, y)