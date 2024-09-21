def e():
    return list(map(int, input().strip().split()))

for _ in range(e()[0]):
    M = []
    n, k = e()
    i = 1
    while True:
        cur = n // 2 + (n & 1)
        if cur >= k:
            print((2 * k - 1) * i)
            break
        else:
            k -= cur
            i = i * 2
            n //= 2
