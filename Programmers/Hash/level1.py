from collections import Counter
# participant = ["marina", "josipa", "nikola", "vinko", "filipa"]
# completion = ["josipa", "filipa", "marina", "nikola"]
# participant = ["leo", "kiki", "eden"]
# completion = ["eden", "kiki"]
participant = ["mislav", "stanko", "mislav", "ana"]
completion = ["stanko", "ana", "mislav"]


def solution(participant, completion):
    participant.sort()
    completion.sort()
    answer = Counter(participant) - Counter(completion)
    answer = list(answer)[0]
    return answer


print(solution(participant, completion))
