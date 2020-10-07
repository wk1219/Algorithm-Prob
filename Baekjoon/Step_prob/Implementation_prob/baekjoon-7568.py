n = int(input())
a = []

for i in range(n):
    x, y = map(int, input().split())
    a.append((x, y))

for j in a:
    rank = 1

    for k in a:
        if j[0] != k[0] and j[1] != k[1]:
            if j[0] < k[0] and j[1] < k[1]:
                rank += 1
    print(rank, end=' ')