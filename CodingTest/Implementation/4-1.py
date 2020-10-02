N = int(input())
M = [[(x+1, y+1) for y in range(N)] for x in range(N)]
direct = list(input().split())

cnt = 0
cur = M[cnt][cnt]

while cnt != len(direct):
    if direct[cnt] == 'R':
        if cur[1] == len(M):
            cnt += 1
            continue
        else:
            cur = (cur[0], cur[1] + 1)
            cnt += 1
    elif direct[cnt] == 'L':
        if cur[1] == 1:
            cnt += 1
            continue
        else:
            cur = (cur[0], cur[1] - 1)
            cnt += 1
    elif direct[cnt] == 'U':
        if cur[0] == 1:
            cnt += 1
            continue
        else:
            cur = (cur[0] - 1, cur[1])
            cnt += 1
    elif direct[cnt] == 'D':
        if cur[0] == len(M):
            cnt += 1
        else:
            cur = (cur[0] + 1, cur[1])
            cnt += 1

print(cur[0], cur[1])