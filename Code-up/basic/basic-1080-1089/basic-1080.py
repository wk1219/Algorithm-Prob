a = int(input())
sum = 0
for i in range(0, a+1):
    sum += i
    if sum >= a:
        print(i)
        break