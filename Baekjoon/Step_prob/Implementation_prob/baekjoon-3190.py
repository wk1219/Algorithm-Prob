from collections import deque


def directions(dir):
    if dir == 'D':
        if move == [0, 1]:
            return [1, 0]
        elif move == [1, 0]:
            return [0, -1]
        elif move == [-1, 0]:
            return [0, 1]
        elif move == [0, -1]:
            return [-1, 0]
    elif dir == 'L':
        if move == [0, 1]:
            return [-1, 0]
        elif move == [1, 0]:
            return [0, 1]
        elif move == [0, -1]:
            return [1, 0]
        elif move == [-1, 0]:
            return[0, -1]


n = int(input())
k = int(input())
maps = [[0] * n for i in range(n)]
for i in range(k):
    x, y = map(int, input().split())
    maps[x - 1][y - 1] = 1
snake_dirs = int(input())
snake_info = deque()
for i in range(snake_dirs):
    k, c = map(str, input().split())
    snake_info.append([int(k), c])

move = [0, 1]
queue = deque()
queue.append([0, 0])
cnt = 0

while True:
    x, y = queue[-1][0], queue[-1][1]   # Snake tail
    nx = x + move[0]
    ny = y + move[1]
    if 0 <= nx < n and 0 <= ny < n:
        if [nx, ny] in queue:       # Self snake check
            break
        queue.append([nx, ny])
        if maps[nx][ny] == 1:
            maps[nx][ny] = 0
        else:
            queue.popleft()
    else:
        break
    cnt += 1
    if snake_info and cnt == snake_info[0][0]:
        move = directions(snake_info[0][1])
        snake_info.popleft()

print(cnt + 1)