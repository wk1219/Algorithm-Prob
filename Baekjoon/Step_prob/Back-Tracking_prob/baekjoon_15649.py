import sys

n, t = map(int, sys.stdin.readline().split())
chk = [False] * (n+1)
answer = [0] * t

def recursive(idx, n, t):
    if idx == t:
        for i in range(t):
            print(answer[i], end=' ')
        print()
        return

    for i in range(1, n+1):
        if chk[i]:
            continue
        chk[i] = True
        answer[idx] = i
        recursive(idx+1, n, t)
        chk[i] = False

recursive(0, n, t)
