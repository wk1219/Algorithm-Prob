from itertools import permutations
# numbers = "17"
numbers = "011"


def is_prime(num):
    p_list = []
    for x in num:
        chk = True
        for i in range(2, x):
            if x % i == 0:
                chk = False
                break
        if x > 1 and chk:
            p_list.append(x)
    return len(p_list)


def solution(numbers):
    numbers = list(numbers)
    num = []
    for i in range(1, len(numbers)+1):
        tmp = permutations(numbers, i)
        for n in tmp:
            tmp_str = "".join(n)
            num.append(int(tmp_str))
    num = list(set(num))
    return is_prime(num)


print(solution(numbers))