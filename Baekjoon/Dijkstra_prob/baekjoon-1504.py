import heapq
import sys
input = sys.stdin.readline

INF = int(1e9)
n, e = map(int, input().split())
graph = [[] for _ in range(n + 1)]


for i in range(e):
    a, b, c = map(int, input().split())
    graph[a].append([b, c])
    graph[b].append([a, c])

v1, v2 = map(int, input().split())


def dijkstra(start):
    q = []
    heapq.heappush(q, [0, start])
    distance = [INF] * (n + 1)
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for node, cost in graph[now]:
            cost += dist
            if cost < distance[node]:
                distance[node] = cost
                heapq.heappush(q, [cost, node])
    return distance


res = dijkstra(1)
path_v1 = dijkstra(v1)
path_v2 = dijkstra(v2)
cnt = min(res[v1] + path_v1[v2] + path_v2[n], res[v2] + path_v2[v1] + path_v1[n])
if cnt < INF:
    print(cnt)
else:
    print(-1)

