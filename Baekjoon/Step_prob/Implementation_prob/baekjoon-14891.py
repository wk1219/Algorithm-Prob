gear = []
for i in range(4):
    x = list(map(int, input()))
    gear.append(x)
k = int(input())
cmds = []
for i in range(k):
    n, direction = map(int, input().split())
    cmds.append([n, direction])


def rotate(gear, chk):
    if chk:
        return [gear[-1]] + gear[0:-1]      # Clockwise Turn
    else:
        return gear[1:] + [gear[0]]         # Counter Clockwise Turn


for cmd in cmds:
    dir = [0] * 4
    num = cmd[0] - 1
    if cmd[1] == 1:
        dir[num] = 1
    else:
        dir[num] = -1

    for i in reversed(range(num)):
        if gear[i][2] != gear[i + 1][6]:
            dir[i] = (-1) * dir[i + 1]
        else:
            break

    for i in range(num + 1, 4):
        if gear[i - 1][2] != gear[i][6]:
            dir[i] = (-1) * dir[i - 1]
        else:
            break

    for i in range(4):
        if dir[i] == 0:
            continue
        elif dir[i] == 1:
            gear[i] = rotate(gear[i], True)
        elif dir[i] == -1:
            gear[i] = rotate(gear[i], False)


score = gear[0][0] * 1 + gear[1][0] * 2 + gear[2][0] * 4 + gear[3][0] * 8
print(score)