n = int(input())
conn = int(input())
com = [[0] * n for i in range(n)]
visited = [0] * n
for i in range(conn):
    x, y = map(int, input().split())
    com[x - 1][y - 1] = com[y - 1][x - 1] = 1


def dfs(v):
    visited[v] = 1
    for i in range(n):
        if visited[i] == 0 and com[v][i] == 1:
            dfs(i)


dfs(0)
cnt = 0
for i in range(1, n):
    if visited[i] == 1:
        cnt += 1
print(cnt)


