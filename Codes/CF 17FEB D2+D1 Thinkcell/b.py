def solve():
    n = int(input())
    i, j, c = 1, n, 1
    result = []
    while c <= n:
        if c % 2 != 0:
            result.append(str(i))
            i += 1
        else:
            result.append(str(j))
            j -= 1
        
        c += 1
    print(" ".join(result))

if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        solve()
