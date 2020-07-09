str = input().lower()
wlist = list(set(str))
cnt = list()

for i in wlist:
    count = str.count(i)
    cnt.append(count)

if cnt.count(max(cnt)) >= 2:
    print('?')
else:
    print(wlist[(cnt.index(max(cnt)))].upper())