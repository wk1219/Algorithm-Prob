import sys
from itertools import combinations
input = sys.stdin.readline

N = int(input())
status = []
for i in range(N):
    status.append(list(map(int, input().split())))

team = list(combinations(range(0, N), N // 2))
res = []
for x in team:
    start = set(x)
    link = list(set(range(N)) - start)
    start = list(start)

    start_status = 0
    link_status = 0

    for i in range(N // 2 - 1):
        for j in range(i + 1, N // 2):
            start_status += status[start[i]][start[j]] + status[start[j]][start[i]]
            link_status += status[link[i]][link[j]] + status[link[j]][link[i]]
    res.append(abs(start_status - link_status))


print(min(res))