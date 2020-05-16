num = list(str(input()))
num.sort(reverse=True)
ans = ''

for i in num:
    ans += i
print(int(ans))