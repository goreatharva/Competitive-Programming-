def solve():
    a, b = map(int, input().split())
    s1 = ""
    while a > 0:
        i = 0
        while i < b:
            s1 += chr(ord('a') + i)
            i += 1
        a -= 1
    print(s1)

t = int(input())
while t > 0:
    solve()
    t -= 1
