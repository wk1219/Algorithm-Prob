N = int(input())
matrix = [list(map(int, input())) for _ in range(N)]

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
visited = [[0] * N for _ in range(N)]


visited[0][0] = 0
cnt = []
c = 0


def bfs(matrix, cnt, x, y):
    matrix[x][y] = 0
    queue = []
    queue.append([x, y])
    while queue:
        x, y = queue.pop(0)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                if matrix[nx][ny] == 1 and visited[nx][ny] == 0:
                    matrix[nx][ny] = 0
                    queue.append([nx, ny])
                    cnt += 1
    return cnt


for i in range(N):
    for j in range(N):
        if matrix[i][j] == 1:
            cnt.append(bfs(matrix, c + 1, i, j))


print(len(cnt))
cnt.sort()
for i in range(len(cnt)):
    print(cnt[i])