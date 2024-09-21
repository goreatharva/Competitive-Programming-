t = int(input())

for _ in range(t):
    x, y = map(int, input().split())

    if x == y:
        print("YES")
    elif x < y:
        if x + 1 == y or x + 2 == y:
            print("YES")
        else:
            print("NO")
    else:
        if y + 1 == x:
            print("YES")
        else:
            print("NO")
