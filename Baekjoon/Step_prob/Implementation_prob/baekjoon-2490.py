a = []
for i in range(3):
    a.append(list(map(int, input().split())))

for i in range(len(a)):
    cnt = 0
    for j in a[i]:
        if j == 0:
            cnt += 1
    if cnt == 1:
        print('A')
    elif cnt == 2:
        print('B')
    elif cnt == 3:
        print('C')
    elif cnt == 4:
        print('D')
    else:
        print('E')