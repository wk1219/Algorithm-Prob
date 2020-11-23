from itertools import product

n, m = map(int, input().split())
s = product(range(1, n + 1), repeat=m)

for i in s:
    print(*i)


