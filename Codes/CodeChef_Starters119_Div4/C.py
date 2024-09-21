def main():
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        a = list(map(int, input().split()))
        ans = []
        count = 0
        for i in range(n):
            if k <= a[i]:
                p = a[i] % k
                ans.append(p)
                count += 1

        if count < 1:
            print("-1")
        else:
            ans.sort()
            print(ans[0])

if __name__ == "__main__":
    main()
