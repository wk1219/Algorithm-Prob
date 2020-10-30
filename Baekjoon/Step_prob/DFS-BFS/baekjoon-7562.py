dx = [1, 2, -1, -2, -2, -1, 1, 2]
dy = [2, 1, 2, 1, -1, -2, -2, -1]


def bfs(matrix, x, y, ex, ey):
    queue = [[x, y]]
    matrix[x][y] = 1
    while queue:
        x, y = queue.pop(0)
        if x == ex and y == ey:
            print(matrix[ex][ey] - 1)
            return
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < I and 0 <= ny < I and matrix[nx][ny] == 0:
                queue.append([nx, ny])
                matrix[nx][ny] = matrix[x][y] + 1


n = int(input())
mat = []
for i in range(n):
    I = int(input())
    mat = [[0] * I for i in range(I)]
    sx, sy = list(map(int, input().split()))
    ex, ey = list(map(int, input().split()))
    bfs(mat, sx, sy, ex, ey)