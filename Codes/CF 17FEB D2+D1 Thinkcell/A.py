def max_final_score(t, test_cases):
    results = []
    for case in test_cases:
        n = case[0]
        numbers = case[1]

        numbers.sort(reverse=True) 
        score = sum(numbers[i] for i in range(1, 2 * n, 2))
        results.append(score)

    return results

if __name__ == "__main__":
    t = int(input())
    test_cases = []

    for _ in range(t):
        n = int(input())
        numbers = list(map(int, input().split()))
        test_cases.append((n, numbers))

    results = max_final_score(t, test_cases)

    print()
    for result in results:
        print(result)
