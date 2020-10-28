import sys
input = sys.stdin.readline


dx = [-1, 1, 0, 0, 1, -1, 1, -1]
dy = [0, 0, -1, 1, -1, -1, 1, 1]


def bfs(x, y):
    matrix[x][y] = 0
    queue = [[x, y]]
    while queue:
        x, y = queue.pop(0)
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < h and 0 <= ny < w and matrix[nx][ny] == 1:
                matrix[nx][ny] = 0
                queue.append([nx, ny])


while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break
    cnt = 0
    matrix = []
    for i in range(h):
        matrix.append(list(map(int, input().split())))
    for i in range(h):
        for j in range(w):
            if matrix[i][j] == 1:
                bfs(i, j)
                cnt += 1
    print(cnt)