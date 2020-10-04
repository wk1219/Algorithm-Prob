from collections import deque

n, m, v = map(int, input().split())
matrix = [[0] * (n+1) for i in range(n+1)]
for i in range(m):
    x, y = list(map(int, input().split()))
    matrix[x][y] = matrix[y][x] = 1

visited = [False] * (n+1)


def dfs(matrix, v, visited):
    visited[v] = True
    print(v, end=' ')
    for i in range(1, n+1):
        if visited[i] == False and matrix[v][i] == True:
            dfs(matrix, i, visited)


def bfs(matrix, start, visited):
    queue = deque([start])
    visited[start] = False
    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for i in range(1, n+1):
            if visited[i] == True and matrix[v][i] == True:
                queue.append(i)
                visited[i] = False


dfs(matrix, v, visited)
print()
bfs(matrix, v, visited)
