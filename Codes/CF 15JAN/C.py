t = int(input())

for _ in range(t):
    n, f, a, b = map(int, input().split())
    vec = list(map(int, input().split()))

    pre = 0
    mn = 0

    for i in range(n):
        mn = min(b, abs(vec[i] - pre) * a)
        f -= mn
        pre = vec[i]

    if f > 0:
        print("YES")
    else:
        print("NO")
