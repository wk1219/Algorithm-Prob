from itertools import combinations

n, m = map(int, input().split())
s = list(combinations(range(1, n + 1), m))

for i in s:
    print(' '.join(map(str, i)))
