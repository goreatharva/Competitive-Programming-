from math import gcd

def solve():
    a, b = map(int, input().split())
    g = gcd(a, b)
    
    if a * b // g == b:
        for i in range(2, int(b**0.5) + 1):
            if i <= a and a % i == 0:
                print(b * i)
                return
            elif b % i == 0:
                print(b * i)
                return
        
        print(b * b)
    else:
        print(a * b // g)

def main():
    t = int(input())
    for _ in range(t):
        solve()

if __name__ == "__main__":
    main()
