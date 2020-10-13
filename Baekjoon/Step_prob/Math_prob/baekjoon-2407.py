import math

n, m = map(int, input().split())
u = math.factorial(n)
d = (math.factorial(n-m))*(math.factorial(m))
print(u // d)
