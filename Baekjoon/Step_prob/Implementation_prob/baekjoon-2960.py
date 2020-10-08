n, k = map(int, input().split())
s = [0 for _ in range(1001)]
cnt = 0

for i in range(2, n+1):
    for j in range(i, n+1, i):
        if s[j] != 1:
            s[j] = 1
            cnt += 1
            if cnt == k:
                print(j)
                break
