from heapq import heappop, heappush
s = [1, 2, 3, 9, 10, 12]
k = 7


def solution(scoville, K):
    ans = 0
    scoville = sorted(scoville)
    while len(scoville) > 1:
        if scoville[0] >= K:
            return ans
        else:
            a = heappop(scoville)
            b = heappop(scoville)
            heappush(scoville, a + b * 2)
            ans += 1

    if scoville[0] < K:
        return -1
    else:
        return ans


print(solution(s, k))