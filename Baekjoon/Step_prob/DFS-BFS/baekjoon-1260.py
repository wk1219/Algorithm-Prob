from collections import deque

n, m, v = map(int, input().split())
matrix = [[0] * (n+1) for i in range(n+1)]
for i in range(m):
    x, y = list(map(int, input().split()))
    matrix[x][y] = matrix[y][x] = 1     # 대칭 표현

visited = [False] * (n+1)


def dfs(v):
    visited[v] = True
    print(v, end=' ')
    for i in range(1, n+1):
        if not visited[i] and matrix[v][i]:
            dfs(i)


def bfs(start):
    queue = deque([start])
    visited[start] = False
    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for i in range(1, n+1):
            if visited[i] and matrix[v][i]:
                queue.append(i)
                visited[i] = False


dfs(v)
print()
bfs(v)
