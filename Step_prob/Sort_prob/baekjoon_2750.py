case = int(input())
n = []
for i in range(case):
    a = int(input())
    n.append(a)
    n.sort()

for i in range(len(n)):
    print(n[i])