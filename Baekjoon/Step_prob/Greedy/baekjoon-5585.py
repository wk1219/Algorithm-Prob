import sys
input = sys.stdin.readline

n = int(input())
s = 1000 - n
money = [500, 100, 50, 10, 5, 1]
cnt = 0
for i in money:
    cnt += s // i
    s %= i
print(cnt)