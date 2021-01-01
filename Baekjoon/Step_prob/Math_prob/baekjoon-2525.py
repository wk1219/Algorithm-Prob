a, b = map(int, input().split())
c = int(input())

minute = b + c
if minute > 60:
    a += 1
    minute = minute - 60
elif minute == 60:
    a += 1
    minute = 0

if a >= 24:
    a = a - 24

print("%d %d" % (a, minute))