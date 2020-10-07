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
data = list(map(int, input().split()))
m = int(input())
search_data = list(map(int, input().split()))

for i in search_data:
    res = binary_search(data, i, 0, n - 1)
    if res != None:
        print('yes', end=' ')
    else:
        print('no', end=' ')