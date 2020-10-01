pan = [[0 for i in range(19)] for j in range(19)]
n = int(input())
x = []
y = []

for i in range(0, n):
    a, b = map(int, input().split())
    x.append(a)
    y.append(b)

for i in range(0, 19):
    for j in range(0, 19):
        for k in range(0, n):
            if x[k] == i+1 and y[k] == j+1:
                pan[i][j] = 1
        print("%d" % pan[i][j], end=' ')
    print()