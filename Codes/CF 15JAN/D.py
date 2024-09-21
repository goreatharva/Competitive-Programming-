def solve():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    a.sort()
    b.sort(reverse=True)

    l, r, d, i, j = 0, n - 1, 0, 0, m - 1

    while l <= r and i <= j:
        while l < n and a[l] == b[i]:
            l += 1
        while r >= 0 and a[r] == b[j]:
            r -= 1

        if l > r or i > j:
            break

        if l == r:
            d += max(abs(a[l] - b[i]), abs(a[r] - b[j]))
            r -= 1
            j -= 1
            l += 1
            i += 1
            continue

        d += abs(a[l] - b[i]) + abs(a[r] - b[j])
        r -= 1
        j -= 1
        l += 1
        i += 1

    print(d)


def main():
    tt = int(input())
    while tt > 0:
        solve()
        tt -= 1


if __name__ == "__main__":
    main()
