p = {')':'(', ']':'['}

while True:
    words = input()
    z = []
    cnt = 0
    if words == '.':
        break

    for i in words:
        if i in '[(':
            z.append(i)
        elif i in p:
            if len(z) == 0:
                print("no")
                cnt = 1
                break
            else:
                x = z.pop(-1)
                if x != p[i]:
                    print("no")
                    cnt = 1
                    break

    if len(z) != 0 and cnt == 0:
        print("no")
    elif len(z) == 0 and cnt == 0:
        print("yes")
