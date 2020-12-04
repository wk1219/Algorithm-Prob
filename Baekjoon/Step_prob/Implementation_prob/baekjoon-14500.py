import sys
input = sys.stdin.readline

n, m = map(int, input().split())
maps = []
for i in range(n):
    maps.append(list(map(int, input().split())))
visited = [[0] * n for _ in range(n)]
a_res = []
b_res = []
c_res = []
d_res = []
e_res = []


def block_a(a_res):
    for i in range(n):
        for j in range(m):
            if i + 3 < n:                                                                           # ■
                # print(maps[i][j], maps[i + 1][j], maps[i + 2][j], maps[i + 3][j])                 # ■
                res = maps[i][j] + maps[i + 1][j] + maps[i + 2][j] + maps[i + 3][j]                 # ■
                a_res.append(res)                                                                   # ■

            if j + 3 < m:
                # print(maps[i][j], maps[i][j + 1], maps[i][j + 2], maps[i][j + 3])                 # ■ ■ ■ ■
                res = maps[i][j] + maps[i][j + 1] + maps[i][j + 2] + maps[i][j + 3]
                a_res.append(res)

    a_res = list(set(a_res))
    return a_res


def block_b(b_res):
    for i in range(n):
        for j in range(m):
            if i + 1 < n and j + 1 < m:
                # print(maps[i][j], maps[i][j + 1], maps[i + 1][j], maps[i + 1][j + 1])             # ■ ■
                res = maps[i][j] + maps[i][j + 1] + maps[i + 1][j] + maps[i + 1][j + 1]             # ■ ■
                b_res.append(res)

    b_res = list(set(b_res))
    return b_res


def block_c(c_res):
    for i in range(n):
        for j in range(m):
            if i + 2 < n and j + 1 < m:
                # print(maps[i][j], maps[i + 1][j], maps[i + 2][j], maps[i + 2][j + 1])             # ■
                res = maps[i][j] + maps[i + 1][j] + maps[i + 2][j] + maps[i + 2][j + 1]             # ■
                c_res.append(res)                                                                   # ■ ■

            if i + 1 < n and j + 2 < m:
                # print(maps[i][j], maps[i][j + 1], maps[i][j + 2], maps[i + 1][j])                 # ■ ■ ■
                res = maps[i][j] + maps[i][j + 1] + maps[i][j + 2] + maps[i + 1][j]                 # ■
                c_res.append(res)

            if i + 1 < n and j + 2 < m:
                # print(maps[i][j], maps[i + 1][j], maps[i + 1][j + 1], maps[i + 1][j + 2])         # ■
                res = maps[i][j] + maps[i + 1][j] + maps[i + 1][j + 1] + maps[i + 1][j + 2]         # ■ ■ ■
                c_res.append(res)

            if i + 2 < n and j + 1 < m:
                # print(maps[i][j], maps[i][j + 1], maps[i + 1][j + 1], maps[i + 2][j + 1])         # ■ ■
                res = maps[i][j] + maps[i][j + 1] + maps[i + 1][j + 1] + maps[i + 2][j + 1]         #   ■
                c_res.append(res)                                                                   #   ■

            if i + 2 < n and j + 1 < m:
                # print(maps[i][j + 1], maps[i + 1][j + 1], maps[i + 2][j], maps[i + 2][j + 1])     #   ■
                res = maps[i][j + 1] + maps[i + 1][j + 1] + maps[i + 2][j] + maps[i + 2][j + 1]     #   ■
                c_res.append(res)                                                                   # ■ ■

            if i + 1 < n and j + 2 < m:
                # print(maps[i][j + 2], maps[i + 1][j], maps[i + 1][j + 1], maps[i + 1][j + 2])     #     ■
                res = maps[i][j + 2] + maps[i + 1][j] + maps[i + 1][j + 1] + maps[i + 1][j + 2]     # ■ ■ ■
                c_res.append(res)

            if i + 1 < n and j + 2 < m:
                # print(maps[i][j], maps[i][j + 1], maps[i][j + 2], maps[i + 1][j + 2])             # ■ ■ ■
                res = maps[i][j] + maps[i][j + 1] + maps[i][j + 2] + maps[i + 1][j + 2]             #     ■
                c_res.append(res)

            if i + 2 < n and j + 1 < m:
                # print(maps[i][j], maps[i][j + 1], maps[i + 1][j], maps[i + 2][j])                 # ■ ■
                res = maps[i][j] + maps[i][j + 1] + maps[i + 1][j] + maps[i + 2][j]                 # ■
                c_res.append(res)                                                                   # ■

    c_res = list(set(c_res))
    return c_res


def block_d(d_res):
    for i in range(n):
        for j in range(m):
            if i + 2 < n and j + 1 < m:
                # print(maps[i][j], maps[i + 1][j], maps[i + 1][j + 1], maps[i + 2][j + 1])         # ■
                res = maps[i][j] + maps[i + 1][j] + maps[i + 1][j + 1] + maps[i + 2][j + 1]         # ■ ■
                d_res.append(res)                                                                   #   ■

            if i + 1 < n and j + 2 < m:
                # print(maps[i][j + 1], maps[i][j + 2], maps[i + 1][j], maps[i + 1][j + 1])         #   ■ ■
                res = maps[i][j + 1] + maps[i][j + 2] + maps[i + 1][j] + maps[i + 1][j + 1]         # ■ ■
                d_res.append(res)

            if i + 1 < n and j + 2 < m:
                # print(maps[i][j], maps[i][j + 1], maps[i + 1][j + 1], maps[i + 1][j + 2])         # ■ ■
                res = maps[i][j] + maps[i][j + 1] + maps[i + 1][j + 1] + maps[i + 1][j + 2]         #   ■ ■
                d_res.append(res)

            if i + 2 < n and j + 1 < m:
                # print(maps[i][j + 1], maps[i + 1][j], maps[i + 1][j + 1], maps[i + 2][j])         #   ■
                res = maps[i][j + 1] + maps[i + 1][j] + maps[i + 1][j + 1] + maps[i + 2][j]         # ■ ■
                d_res.append(res)                                                                   # ■

    d_res = list(set(d_res))
    return d_res


def block_e(e_res):
    for i in range(n):
        for j in range(m):
            if i + 1 < n and j + 2 < m:
                # print(maps[i][j], maps[i][j + 1], maps[i][j + 2], maps[i + 1][j + 1])             # ■ ■ ■
                res = maps[i][j] + maps[i][j + 1] + maps[i][j + 2] + maps[i + 1][j + 1]             #   ■
                e_res.append(res)

            if i + 2 < n and j + 1 < m:
                # print(maps[i][j], maps[i + 1][j], maps[i + 1][j + 1], maps[i + 2][j])             # ■
                res = maps[i][j] + maps[i + 1][j] + maps[i + 1][j + 1] + maps[i + 2][j]             # ■ ■
                e_res.append(res)                                                                   # ■

            if i + 1 < n and j + 2 < m:
                # print(maps[i][j + 1], maps[i + 1][j], maps[i + 1][j + 1], maps[i + 1][j + 2])     #   ■
                res = maps[i][j + 1] + maps[i + 1][j] + maps[i + 1][j + 1] + maps[i + 1][j + 2]     # ■ ■ ■
                e_res.append(res)

            if i + 2 < n and j + 1 < m:
                # print(maps[i][j + 1], maps[i + 1][j], maps[i + 1][j + 1], maps[i + 2][j + 1])     #   ■
                res = maps[i][j + 1] + maps[i + 1][j] + maps[i + 1][j + 1] + maps[i + 2][j + 1]     # ■ ■
                e_res.append(res)                                                                   #   ■

    e_res = list(set(e_res))
    return e_res


a = block_a(a_res)
b = block_b(b_res)
c = block_c(c_res)
d = block_d(d_res)
e = block_e(e_res)
res_list = list(set(a + b + c + d + e))
print(max(res_list))