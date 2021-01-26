n = int(input())

cnt = 1
room = 6
res = 1
while cnt < n:
    res += 1
    cnt += room
    room += 6
print(res)
