def solve():
    n = int(input())
    a = input().strip()
    b = input().strip()
    c = input().strip()

    cnt = 0

    for i in range(n):
        if a[i] == c[i] or b[i] == c[i]:
            cnt += 1

    if cnt == n:
        print("NO")
        return

    print("YES")


t = int(input())


for _ in range(t):
    solve()


