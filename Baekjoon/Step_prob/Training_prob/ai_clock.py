a, b, c = map(int, input().split())
d = int(input())

sec = (c + d) % 60
m = (c + d) // 60

min = (b + m) % 60
h = (b + m) // 60

hour = (a + h) % 24

print(hour, min, sec)