n = int(input())
v = []
for i in range(n):
    v.append(input())

v_set = list(set(v))
v_list = []
for i in v_set:
    v_list.append((len(i), i))

v_list.sort()
for v_len, res in v_list:
    print(res)
