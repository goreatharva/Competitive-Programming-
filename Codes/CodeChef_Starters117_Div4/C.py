t = int(input())

for _ in range(t):
    n = int(input())
    s = input()
    
    idx = next((i for i in range(n - 1) if s[i] > s[i + 1]), n - 1)

    print(s[:idx] + s[idx + 1:])


