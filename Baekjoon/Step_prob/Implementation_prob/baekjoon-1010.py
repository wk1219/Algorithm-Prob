n = int(input())

for i in range(n):
    x, y = map(int, input().split())
    k = y - x
    res = 1
    while y > k:
        res *= y
        y -= 1
    while x > 1:
        res = res // x
        x -= 1
    print(res)