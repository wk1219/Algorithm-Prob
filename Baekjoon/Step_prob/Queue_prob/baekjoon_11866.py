import sys
from collections import deque

queue = deque([])

n, r = sys.stdin.readline().split()
n = int(n)
r = int(r)

for i in range(n):
    queue.append(i+1)

print('<', end='')

while queue:
    for i in range(r - 1):
        queue.append(queue[0])
        queue.popleft()
    print(queue.popleft(), end='')
    if queue:
        print(', ', end='')
print('>')
