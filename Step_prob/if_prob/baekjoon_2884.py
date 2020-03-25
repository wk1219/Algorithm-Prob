hour, min = input().split()
hour = int(hour)
min = int(min)

if hour > 0 and hour < 24 and min < 45:
    print(hour-1, min + 60 - 45)
elif hour == 0 and min < 45:
    print(hour+23, min + 60 - 45)
elif hour > 0 and hour < 24 and min >= 45:
    print(hour, min - 45)
elif hour == 0 and min >= 45:
    print(hour, min - 45)
