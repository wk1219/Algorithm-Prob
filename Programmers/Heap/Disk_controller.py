# jobs = [[0, 3], [1, 9], [2, 6]]
jobs = [[0, 10], [4, 10], [5, 11], [15, 2]]
def solution(jobs):
    answer = 0
    cnt = 0
    res = []
    job_len = len(jobs)
    jobs = sorted(jobs, key=lambda x: x[1])

    while len(jobs) != 0:
        for i in range(len(jobs)):
            if jobs[i][0] <= cnt:
                cnt += jobs[i][1]
                res.append(cnt - jobs[i][0])
                jobs.pop(i)
                break
            if i == len(jobs) - 1:
                cnt += 1
    answer = sum(res) // job_len
    return answer


print(solution(jobs))