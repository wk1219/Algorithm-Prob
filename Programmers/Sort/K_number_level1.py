array = [1, 5, 2, 6, 3, 7, 4]
commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]


def solution(array, commands):
    res = []
    for i in range(len(commands)):
        x = array[commands[i][0] - 1:commands[i][1]]
        x.sort()
        res.append(x[commands[i][2] - 1])
    return res

print(solution(array, commands))