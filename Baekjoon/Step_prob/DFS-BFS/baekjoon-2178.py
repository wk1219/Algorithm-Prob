n, m = map(int, input().split())
g = []
for i in range(n):
    g.append(list(map(int, input())))

visited =[[0] * m for _ in range(n)]
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

queue = [[0, 0]]            # start
visited[0][0] = 1           # position : start


while queue:
    x, y = queue.pop(0)
    for i in range(4):      # direction : up, down, left, right
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            if visited[nx][ny] == 0 and g[nx][ny] == 1:
                visited[nx][ny] = visited[x][y] + 1
                queue.append([nx, ny])


print(visited[n - 1][m - 1])