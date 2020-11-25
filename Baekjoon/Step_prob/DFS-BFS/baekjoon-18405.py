from collections import deque

n, k = map(int, input().split())
matrix = []
virus = []
for i in range(n):
    matrix.append(list(map(int, input().split())))
s, x, y = map(int, input().split())

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def bfs():
    while queue:
        v, t, x, y = queue.popleft()
        if s == t:
            break
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and matrix[nx][ny] == 0:
                matrix[nx][ny] = matrix[x][y]
                queue.append([v, t + 1, nx, ny])


for i in range(n):
    for j in range(n):
        if matrix[i][j] > 0:
            virus.append([matrix[i][j], 0, i, j])

virus.sort()
queue = deque(virus)
bfs()
print(matrix[x - 1][y - 1])