t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    g = [list(map(int, input().split())) for _ in range(n)]
    ans = 0
    for r in range(n):
        for c in range(m):
            sum = 0
          
            i = 1
            while r - i >= 0 and c - i >= 0:
                sum += g[r - i][c - i]
                i += 1
           
            i = 1
            while r + i < n and c + i < m:
                sum += g[r + i][c + i]
                i += 1
        
            i = 1
            while r + i < n and c - i >= 0:
                sum += g[r + i][c - i]
                i += 1
         
            i = 1
            while r - i >= 0 and c + i < m:
                sum += g[r - i][c + i]
                i += 1
            sum += g[r][c]
            ans = max(ans, sum)
    print(ans)
    