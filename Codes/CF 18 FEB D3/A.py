def solve():
    n = int(input())
    s = input()
    coins = 0
    i = 0
    while i < n:
        if s[i] == '.':
            i += 1
        elif s[i] == '@':
            coins += 1
            i += 1
        else:
            if i + 1 < n and s[i + 1] == '*':
                break
            else:
                i += 1
    print(coins)

t = 1
t = int(input())
while t > 0:
    solve()
    t -= 1
