while True:
    n = int(input())
    if n == 0:
        break
    if list(str(n)) == list(str(n))[::-1]:
        print("yes")
    else:
        print("no")
