n = int(input())
array = []
for i in range(n):
    data = input().split()
    array.append((data[0], int(data[1])))
array = sorted(array, key=lambda stu: stu[1])

for stu in array:
    print(stu[0], end=' ')
