
def min_hits_to_defeat_boss(T, test_cases):
    for case in test_cases:
        H, X, Y1, Y2, K = case

        if K == 0:
            hits_needed = (H - 1) // X + 1
        else:
            initial_damage = K * Y1
            reduced_damage = (H - initial_damage - 1) // (Y1 - Y2) + 1
            hits_needed = K + reduced_damage

        print(hits_needed)


T = int(input())
test_cases = []

for _ in range(T):
    case = list(map(int, input("Enter values for H, X, Y1, Y2, K: ").split()))
    test_cases.append(case)

# Call the function
min_hits_to_defeat_boss(T, test_cases)
