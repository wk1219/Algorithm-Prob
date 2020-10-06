n = int(input())

arr = []
for i in range(n):
    arr.append(input().split())

a = sorted(arr, key=lambda age: int(age[0]))
for res in a:
    print(int(res[0]), res[1])
