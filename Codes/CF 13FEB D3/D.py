def solve():
    n, x, y = map(int, input().split())
    a = list(map(int, input().split()))
    mp = {}
    ans = 0
    for i in range(n):
        if a[i] % y in mp and x - (a[i] % x) in mp[a[i] % y]:
            ans += mp[a[i] % y][x - (a[i] % x)]
        if a[i] % y in mp:
            if a[i] % x in mp[a[i] % y]:
                mp[a[i] % y][a[i] % x] += 1
            else:
                mp[a[i] % y][a[i] % x] = 1
        else:
            mp[a[i] % y] = {a[i] % x: 1}
    print(ans)
