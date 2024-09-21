from collections import Counter

def solve():
    t = int(input())
    while t > 0:
        t -= 1
        n = int(input())
        a = list(map(int, input().split()))
        cnt = 1
        cnt1 = 1
        if n == 1:
            print("0")
            continue
        for i in range(1, n):
            if a[0] == a[i]:
                cnt += 1
            else:
                break
        for i in range(n - 2, -1, -1):
            if a[n - 1] == a[i]:
                cnt1 += 1
            else:
                break
        if a[0] == a[n - 1]:
            print(max(0, n - cnt - cnt1))
        else:
            print(n - max(cnt, cnt1))

if __name__ == "__main__":
    solve()

