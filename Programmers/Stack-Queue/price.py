prices = [1, 2, 3, 2, 3]


def solution(prices):
    s = [0] * len(prices)
    for i in range(len(prices)):
        for j in range(i + 1, len(prices)):
            if prices[i] <= prices[j]:
                s[i] += 1
            else:
                s[i] += 1
                break
    return s


print(solution(prices))