import sys
input = sys.stdin.readline
T = int(input())
for i in range(T):
    N = int(input())
    s = [0 for k in range(N + 1)]
    cnt = 0
    for j in range(N):
        a, b = map(int, input().split())
        s[a] = b
    min_val = s[1]
    for k in range(2, N + 1):
        if s[k] > min_val:
            cnt += 1
        else:
            min_val = s[k]
    print(N - cnt)