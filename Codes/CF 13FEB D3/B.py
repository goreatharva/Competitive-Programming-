t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    s = sum(a)
    k = s // n
    budget = 0
    temp = True
    for i in range(n):
        if a[i] > k:
            budget += a[i] - k
        elif a[i] < k:
            if budget >= k - a[i]:
                budget -= k - a[i]
            else:
                temp = False
                break
    if temp:
        print("YES")
    else:
        print("NO")

