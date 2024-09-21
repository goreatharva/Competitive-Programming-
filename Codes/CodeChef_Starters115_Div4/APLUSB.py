def solve():
    t = int(input())

    for _ in range(t):
        n = int(input())

        a = list(map(int, input().split()))
        b = list(map(int, input().split()))

        maxx = max(a)
        minn = min(b)

        result_a = sorted(a, reverse=True)
        result_b = sorted(b)

        flag = False

        for i in range(n):
            if result_a[i] + result_b[i] != maxx + minn:
                print(-1)
                flag = True
                break

        if not flag:
            print(' '.join(map(str, result_a)))
            print(' '.join(map(str, result_b)))

if __name__ == "__main__":
    solve()




