def solve():
    n, k, m, temp = map(int, input().split())
    temp = input()

    s = ""
    for el in temp:
        if k > ord(el) - ord('a'):
            s += el

    if not s:
        print("NO")
        print('a' * n)
        return

    ans = ""
    cnt = 0
    mp = {}

    for el in s:
        mp[el] = mp.get(el, 0) + 1
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

    g = ''
    for c in range(ord('a'), ord('a') + k):
        if mp.get(chr(c), 0) == 0:
            g = chr(c)
            break

    ans += g * (n - len(ans))
    print(ans)

def main():
    tc = int(input())
    for _ in range(tc):
        solve()

if __name__ == "__main__":
    main()
