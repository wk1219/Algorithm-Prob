import sys
from collections import deque
input = sys.stdin.readline

M, N = map(int, input().split())
matrix = []
queue = deque()
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

for i in range(N):
    r = list(map(int, input().split()))
    for j in range(M):
        if r[j] == 1:
            queue.append([i, j])
    matrix.append(r)


def bfs(matrix):
    cnt = -1
    while queue:
        cnt += 1
        for _ in range(len(queue)):
            x, y = queue.popleft()

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < N and 0 <= ny < M and matrix[nx][ny] == 0:
                    matrix[nx][ny] = matrix[x][y] + 1
                    queue.append([nx, ny])
    for k in matrix:
        if 0 in k:
            return -1
    return cnt


print(bfs(matrix))
