n = int(input())
matrix = []
for i in range(n):
    matrix.append(list(input()))

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
visited = [[0] * n for _ in range(n)]
cnt = 0
vcnt = 0


def bfs(x, y, z, ar):
    ar[x][y] = 0
    queue = [[x, y]]
    while queue:
        x, y = queue.pop(0)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and ar[nx][ny] == z:
                ar[nx][ny] = 0
                queue.append([nx, ny])


for i in range(n):
    for j in range(n):
        if matrix[i][j] == 'R' or matrix[i][j] == 'G':
            visited[i][j] = 1
        else:
            visited[i][j] = 2

for i in range(n):
    for j in range(n):
        if matrix[i][j] != 0:
            bfs(i, j, matrix[i][j], matrix)
            cnt += 1
        if visited[i][j] != 0:
            bfs(i, j, visited[i][j], visited)
            vcnt += 1

print(cnt, vcnt)