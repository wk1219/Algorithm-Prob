from collections import deque
import sys
input = sys.stdin.readline

n, m, k, x = map(int, input().split())
matrix = [[] for _ in range(n + 1)]
INF = int(1e9)
dis = [INF] * (n + 1)
dis[x] = 0
for i in range(m):
    a, b = map(int, input().split())
    matrix[a].append(b)


def bfs(start):
    queue = deque([start])
    while queue:
        now = queue.popleft()
        for next in matrix[now]:
            if dis[next] == INF:
                dis[next] = dis[now] + 1
                queue.append(next)


bfs(x)
chk = False
for i in range(1, n + 1):
    if dis[i] == k:
        print(i)
        chk = True

if not chk:
    print(-1)