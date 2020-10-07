from string import ascii_lowercase

res = [0] * 26
alpha = list(ascii_lowercase)
data = list(input())

for i in range(len(data)):
    if data[i] in alpha:

        res[alpha.index(data[i])] += 1
for i in res:
    print(i, end=' ')
