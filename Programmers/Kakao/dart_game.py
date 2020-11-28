import re

dartResult = '1S2D3T'


def solution(dartResult):
    p = re.compile("(\d+)([a-zA-Z])(\*|#)?")
    scores = p.findall(dartResult)
    res = []
    for idx, score in enumerate(scores):
        s = score[0]
        bonus = score[1]
        option = score[2]
        if bonus == 'S':
            bonus = 1
        elif bonus == 'D':
            bonus = 2
        elif bonus == 'T':
            bonus = 3
        if option == '*':
            if idx == 0:
                res.append(int(s) ** bonus * 2)
            else:
                res[-1] *= 2
                res.append(int(s) ** bonus * 2)
        elif option == '#':
            res.append(int(s) ** bonus * (-1))
        else:
            res.append(int(s) ** bonus)
    return sum(res)


print(solution(dartResult))