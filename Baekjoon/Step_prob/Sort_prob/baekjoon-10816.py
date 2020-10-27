import sys
from collections import Counter
input = sys.stdin.readline

n = int(input())
x = list(map(int, input().split()))
m = int(input())
z = list(map(int, input().split()))

cnt = Counter(x)
for i in z:
    if i in cnt:
        print(cnt[i], end=' ')
    else:
        print(0, end=' ')
