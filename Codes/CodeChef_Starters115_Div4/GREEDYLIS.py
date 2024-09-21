t = int(input())

for _ in range(t):
    n, x = map(int, input().split())

    if n == 1 and x == 0:
        print(1)
        continue

    alice = 2
    remaining = n - 1

    if x != 0 and (x == n or x == n - 1):
        print(-1)
    elif x == 0:
        for j in range(1, n + 1):
            print(j, end=" ")
        print()
    else:
        sequence = []
        for j in range(1, n):
            sequence.append(j)
        sequence.insert(max(0, n - x - 2), n)
        for j in sequence:
            print(j, end=" ")
        print()
