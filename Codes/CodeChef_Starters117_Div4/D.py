t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    if n <= 2:
        print(-1)
    else:
        idx1 = a.index(1) + 1
        idx2 = a.index(3) + 1
        a[idx1 - 1], a[idx2 - 1] = a[idx2 - 1], a[idx1 - 1]
        for num in a:
            print(num, end=' ')
        print()
