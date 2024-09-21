t = int(input())

for _ in range(t):
    n, x, y = map(int, input().split())

    leaves = y // 3
    x_left, leaves1 = 0, 0

    if x >= leaves:
        x_left = x - leaves
        leaves1 = leaves
    else:
        x_left = 0
        leaves1 = x

    leaves2 = x_left // 2

    if leaves2 + leaves1 >= n:
        print("YES")
    else:
        print("NO")
