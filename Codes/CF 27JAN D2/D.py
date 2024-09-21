def solve():
    n, k, m, temp = map(str, input().split())
    cnt = 0
    s = ""
    ans = ""

    for el in temp:
        if k > ord(el) - 97:
            s += el

    if not s:
        print("NO")
        print('a' * n)
        return

    mp = {}

    for el in s:
        if el in mp:
            mp[el] += 1
        else:
            mp[el] = 1

        if len(mp) == k:
            ans += el
            cnt += 1
            mp.clear()

    if cnt >= n:
        print("YES")
        return

    print("NO")

    if not mp:
        ans += s[-1] * (n - len(ans))
        print(ans)
        return

    g = None

    for c in range(ord('a'), ord('a') + k):
        if chr(c) not in mp or mp[chr(c)] == 0:
            g = chr(c)
            break

    ans += g * (n - len(ans))

    print(ans)


def main():
    tc = int(input())
    while tc > 0:
        solve()
        tc -= 1


if __name__ == "__main__":
    main()
