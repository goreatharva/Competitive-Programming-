def solve():
    n = int(input())
    arr = list(map(int, input().split()))
    sum_val = 0
    odd = 0
    eve = 0
    result = []
    
    for i in range(n):
        c = arr[i]
        sum_val += c
        if c % 2 == 1:
            odd += 1
        else:
            eve += 1
        
        r = odd // 3
        
        if eve == 0 and odd == 1:
            r = 0
        elif odd % 3 == 1:
            r = (odd + 2) // 3
        
        result.append(str(sum_val - r))
    
    print(" ".join(result))


def main():
    testcase = int(input())
    for _ in range(testcase):
        solve()


if __name__ == "__main__":
    main()
