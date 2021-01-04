colors = []
for i in range(3):
    colors.append(input())


def resist(color, i):
    val = 0
    m = 0
    if color == 'black':
        val = 0
        m = 1
    elif color == 'brown':
        val = 1
        m = 10
    elif color == 'red':
        val = 2
        m = 100
    elif color == 'orange':
        val = 3
        m = 1000
    elif color == 'yellow':
        val = 4
        m = 10000
    elif color == 'green':
        val = 5
        m = 100000
    elif color == 'blue':
        val = 6
        m = 1000000
    elif color == 'violet':
        val = 7
        m = 10000000
    elif color == 'grey':
        val = 8
        m = 100000000
    elif color == 'white':
        val = 9
        m = 1000000000

    if i != 2:
        return val
    else:
        return m


value = ''
for i in range(3):
    if i == 2:
        value = int(value) * resist(colors[i], i)
    else:
        s = str(resist(colors[i], i))
        value += s
print(value)
