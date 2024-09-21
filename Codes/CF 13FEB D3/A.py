def main():
    n = 80
    ans = ["frog"] * n
    for a in range(ord('a'), ord('z')+1):
        for b in range(ord('a'), ord('z')+1):
            for c in range(ord('a'), ord('z')+1):
                tot = chr(a) + chr(b) + chr(c)
                val = a + b + c - ord('a') * 3
                ans[val] = tot if ans[val] == "frog" else ans[val]
    tt = int(input())
    for _ in range(tt):
        n = int(input())
        print(ans[n - 3])

if __name__ == "__main__":
    main()
