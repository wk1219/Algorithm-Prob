import sys
import collections

num = int(sys.stdin.readline())
q = collections.deque([i for i in range(num)])

while len(q) > 1:
    q.popleft()
    q.append(q[0])
    q.popleft()

print(q[0] + 1)
