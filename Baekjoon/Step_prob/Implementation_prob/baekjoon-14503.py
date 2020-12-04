from collections import deque

n, m = map(int, input().split())
r, c, d = map(int, input().split())
maps = []
for i in range(n):
    maps.append(list(map(int, input().split())))

dx = [-1, 0, 1, 0]      # North, South
dy = [0, 1, 0, -1]      # East, West


def direction(dir):
    if dir == 0:
        return 3
    elif dir == 1:
        return 0
    elif dir == 2:
        return 1
    elif dir == 3:
        return 2


def back(x):
    if x == 0:
        return 2
    elif x == 1:
        return 3
    elif x == 2:
        return 0
    elif x == 3:
        return 1


def bfs(x, y, d):
    cnt = 1
    maps[x][y] = 2
    queue = deque([[x, y, d]])
    while queue:
        x, y, d = queue.popleft()
        direct = d
        for i in range(4):
            direct = direction(direct)
            nx = x + dx[direct]
            ny = y + dy[direct]
            if 0 <= nx < n and 0 <= ny < m and maps[nx][ny] == 0:
                cnt += 1
                maps[nx][ny] = 2                # Clean Place
                queue.append([nx, ny, direct])
                break
            elif i == 3:                        # All Direction Clean
                nx = x + dx[back(d)]
                ny = y + dy[back(d)]
                queue.append([nx, ny, d])
                if maps[nx][ny] == 1:           # All Direction Clean & Back Wall
                    return cnt


print(bfs(r, c, d))