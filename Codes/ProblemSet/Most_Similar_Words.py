def cost(s, t):
    c = 0
    for i in range(len(s)):
        c += abs(ord(s[i]) - ord(t[i]))
    return c
 
t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    s = [input() for _ in range(n)]
    ans = float('inf')
    for i in range(n - 1):
        for j in range(i + 1, n):
            ans = min(ans, cost(s[i], s[j]))
    print(ans)