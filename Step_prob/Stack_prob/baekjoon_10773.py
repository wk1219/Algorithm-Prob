import sys

num = int(sys.stdin.readline())
stack = []
sum = 0
for i in range(num):
    n = int(sys.stdin.readline())
    if n == 0:
        stack.pop()
    else:
        stack.append(n)

for i in range(len(stack)):
    sum += stack[i]

print(sum)