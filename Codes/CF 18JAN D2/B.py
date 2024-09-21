def triangular_number(n):
    return (n * n - 1) * (n - 2) // 6

def pair_number(n):
    return (n * (n - 1)) // 2

def process_input():
    n = int(input())
    frequency_count = [0] * (n + 1)

    x_values = list(map(int, input().split()))
    for x in x_values:
        frequency_count[x] += 1

    total_count = 0
    prev_count = 0
    for i in range(n + 1):
        if frequency_count[i] >= 3:
            total_count += triangular_number(frequency_count[i])
        if frequency_count[i] >= 2:
            total_count += pair_number(frequency_count[i]) * prev_count
        prev_count += frequency_count[i]

    print(total_count)

num_tests = int(input())
for _ in range(num_tests):
    process_input()
