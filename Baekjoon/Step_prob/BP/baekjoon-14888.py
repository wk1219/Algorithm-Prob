import sys
from itertools import permutations
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
options = list(map(int, input().split()))
op = ''
for idx, opt in enumerate(options):
    op += str(idx) * opt
op = list(map(int, op))
res_list = []

for current_op in set(permutations(op, len(op))):
    res = a[0]
    for i in range(n - 1):      # Operator Count : N - 1
        if current_op[i] == 0:
            res += a[i + 1]     # a[i + 1] : 연산자 뒤의 숫자
        elif current_op[i] == 1:
            res -= a[i + 1]
        elif current_op[i] == 2:
            res *= a[i + 1]
        elif current_op[i] == 3:
            if res < 0:
                res = (res * (-1) // a[i + 1]) * (-1)
            else:
                res //= a[i + 1]
    res_list.append(res)

print(max(res_list))
print(min(res_list))