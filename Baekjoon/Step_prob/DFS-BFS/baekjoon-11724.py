import sys
from collections import deque
input = sys.stdin.readline
N, M = map(int, input().split())

graph = [[]for i in range(N+1)]
visited = [0] * (N + 1)
for i in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)


def bfs(start):
    queue = deque([start])
    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if visited[i] == 0:
                queue.append(i)
                visited[i] = 1


cnt = 0
for i in range(1, N + 1):
    if visited[i] == 0:
        bfs(i)
        cnt += 1

print(cnt)