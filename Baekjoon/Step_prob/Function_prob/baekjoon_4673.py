def self_num():
    arr = list()
    res = 0
    for i in range(1, 10001):
        if i < 10:
            res = i + i
            arr.append(res)
        elif i < 100:
            res = i + int(i / 10) + int(i % 10)
            arr.append(res)
        elif i < 1000:
            res = i + int(i / 100) + int((i % 100) / 10) + int((i % 100) % 10)
            arr.append(res)
        elif i < 10000:
            res = i + int(i / 1000) + int((i % 1000) / 100) + int(((i % 1000) % 100 / 10)) + int(
                ((i % 1000) % 100) % 10)
            if res <= 10000:
                arr.append(res)
    arr.sort()
    arr1 = [i for i in range(1, 10001)]
    s = [x for x in arr1 if x not in arr]
    for data in s:
        print(data)

self_num()
