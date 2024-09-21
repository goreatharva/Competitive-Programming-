def find_removed_elements(t, test_cases):
    results = []
    for i in range(t):
        n, k = test_cases[i][0]
        b = test_cases[i][1]

        product = 2023
        remaining_product = 1
        for num in b:
            remaining_product *= num

        if remaining_product % product == 0 and (remaining_product // product) > 1:
            factors = []
            remaining = remaining_product // product
            while len(factors) < k - 1:
                for j in range(2, remaining + 1):
                    if remaining % j == 0:
                        factors.append(j)
                        remaining //= j
                        break
            factors.append(remaining)
            results.append((True, factors))
        else:
            results.append((False, None))
    return results

# Input handling
t = int(input())
test_cases = []
for _ in range(t):
    n, k = map(int, input().split())
    b = list(map(int, input().split()))
    test_cases.append((n, k, b))

outputs = find_removed_elements(t, test_cases)
for result, removed_elements in outputs:
    if result:
        print("YES")
        print(' '.join(map(str, removed_elements)))
    else:
        print("NO")
