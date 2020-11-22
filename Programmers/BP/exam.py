answers = [1, 2, 3, 4, 5]
# answers = [1, 3, 2, 4, 2]
# answers = [1, 3, 2, 3, 2]


def solution(answers):
    first = [1, 2, 3, 4, 5, 1]
    second = [2, 1, 2, 3, 2, 4, 2, 5, 2]
    third = [3, 3, 1, 1, 2, 2, 4, 4, 5]
    x = y = z = 0
    ans = []
    for i in range(len(answers)):
        if first[i % len(first)] == answers[i]:
            x += 1
        if second[i % len(second)] == answers[i]:
            y += 1
        if third[i % len(third)] == answers[i]:
            z += 1

    max_chk = max(x, y, z)
    if max_chk == x:
        ans.append(1)
    if max_chk == y:
        ans.append(2)
    if max_chk == z:
        ans.append(3)

    return ans


print(solution(answers))
