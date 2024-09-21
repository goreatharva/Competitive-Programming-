def func_1():
    return list(map(int, input().strip().split()))

v_1 = 200010
v_2 = [0]*(v_1)

def func_2(n):
    res = 0
    for i in str(n):
        res += int(i)
    return res

for i in range(v_1-1):
    v_2[i+1] = func_2(i+1) + v_2[i]

for _ in range(func_1()[0]):
    v_3 = []  
    v_4 = func_1()[0]
    v_5 = func_1()

    v_6 = {}

    v_7 = 2147483647
    v_8 = 0
    for i in v_5:
        if i not in v_6:
            v_6[i] = 0
        if v_7 - i not in v_6:
            v_6[v_7 - i] = 0 

        if v_6[v_7 - i] > 0:
            v_6[v_7 - i] -= 1
        else:
            v_6[i] += 1
            v_8 += 1

    print(v_8)
