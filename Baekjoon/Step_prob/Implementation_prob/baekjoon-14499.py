import sys
input = sys.stdin.readline


def move_dice(cmd):
    if cmd == 1:
        dice[1], dice[3], dice[4], dice[6] = dice[3], dice[6], dice[1], dice[4]
    elif cmd == 2:
        dice[1], dice[3], dice[4], dice[6] = dice[4], dice[1], dice[6], dice[3]
    elif cmd == 3:
        dice[1], dice[2], dice[5], dice[6] = dice[2], dice[6], dice[1], dice[5]
    elif cmd == 4:
        dice[1], dice[2], dice[5], dice[6] = dice[5], dice[1], dice[6], dice[2]


def direction(cmd):
    if cmd == 1:
        return [0, 1]
    elif cmd == 2:
        return [0, -1]
    elif cmd == 3:
        return [-1, 0]
    elif cmd == 4:
        return [1, 0]


N, M, x, y, K = map(int, input().split())
maps = []
for i in range(N):
    maps.append(list(map(int, input().split())))
cmds = list(map(int, input().split()))
dice = [0, 0, 0, 0, 0, 0, 0]


for cmd in cmds:
    dx, dy = direction(cmd)
    if 0 <= x + dx < N and 0 <= y + dy < M:
        x += dx
        y += dy
        move_dice(cmd)
        if maps[x][y] != 0:
            dice[1] = maps[x][y]
            maps[x][y] = 0
        else:
            maps[x][y] = dice[1]
    else:
        continue
    print(dice[6])