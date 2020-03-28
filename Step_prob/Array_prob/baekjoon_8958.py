case = int(input())

for i in range(0, case):
    str = input()
    cnt = 0
    tot = 0
    for j in range(0, len(str)):
        if str[j] == 'O':
            cnt += 1
            tot += cnt
        elif str[j] == 'X':
            cnt = 0
            tot += 0

    print(tot)

