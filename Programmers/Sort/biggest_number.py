# numbers = [6, 10, 2]
# numbers = [3, 30, 34, 5, 9]
numbers = [100, 38, 83, 9, 3]


def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x: x*3, reverse=True)
    return str(int(''.join(numbers)))


s = solution(numbers)
print(s)