def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None

n = int(input())
a = list(map(int, input().split()))
m = int(input())
s = list(map(int, input().split()))

a.sort()

for i in s:
    res = binary_search(a, i, 0, n - 1)
    if res != None:
        print(1)
    else:
        print(0)