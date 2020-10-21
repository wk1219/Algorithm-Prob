import sys
import heapq
input = sys.stdin.readline
MAX = 100001
N, K = map(int, input().split())
distance = [-1] * MAX


def dijkstra(start):
    q = []
    distance[start] = 0
    heapq.heappush(q, (0, start))
    while q:
        dist, now = heapq.heappop(q)
        for x in [2 * now, now + 1, now - 1]:
            if 0 <= x < MAX and distance[x] == -1:
                if x == 2 * now:
                    heapq.heappush(q, (dist, x))
                    distance[x] = dist
                else:
                    heapq.heappush(q, (dist + 1, x))
                    distance[x] = dist + 1


dijkstra(N)
print(distance[K])