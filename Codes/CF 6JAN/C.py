t = int(input())

for _ in range(t):
    n = int(input())
    values = list(map(int, input().split()))
    
    a = float('inf')
    b = float('inf')
    cnt = 0
    
    for i in range(n):
        if a > b:
            a, b = b, a

        if values[i] <= a:
            a = values[i]
        elif values[i] <= b:
            b = values[i]
        else:
            a = values[i]
            cnt += 1

    print(cnt)
