import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

N, M, X = map(int, input().split())
graph = [[] for i in range(N)]
ans = [0] * N
for i in range(M):
    u, v, t = map(int, input().split())
    graph[u - 1].append((v - 1, t))


def dijkstra(start):
    distance = [INF] * N
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

    return distance


for i in range(N):
    ret = dijkstra(i)

    if i == X - 1:
        for idx, r in enumerate(ret):
            ans[idx] += r
    else:
        ans[i] += ret[X - 1]


print(max(ans))