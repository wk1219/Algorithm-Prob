N, M = map(int, input().split())
A = []
for i in range(N):
    A.append(list(map(int, input().split())))

M, K = map(int, input().split())
B = []
for i in range(M):
    B.append(list(map(int, input().split())))

C = [[0] * K for _ in range(N)]

for i in range(N):
    for j in range(K):
        for k in range(M):
            C[i][j] += A[i][k] * B[k][j]

for i in C:
    for j in i:
        print(j, end=' ')
    print()