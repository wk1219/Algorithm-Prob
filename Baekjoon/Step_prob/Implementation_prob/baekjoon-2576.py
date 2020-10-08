s = []
for i in range(7):
    s.append(int(input()))
d = []
r = 0
for i in s:
    if i % 2 == 1:
        d.append(i)
    else:
        r = -1

if len(d) == 0:
    print(r)
else:
    print(sum(d))
    print(min(d))