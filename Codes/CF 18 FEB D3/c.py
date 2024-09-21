def solve(n, m, arr, comm):
    product = arr[0]
    left = 0
    right = n - 1
    for i in range(1, n):
        product *= arr[i]
    for i in range(n):
        print(product % m, end=" ")
        if comm[i] == 'L':
            product = product // arr[left]
            left += 1
        else:
            product = product // arr[right]
            right -= 1
    print()

T = int(input())
for _ in range(T):
    n, m = map(int, input().split())
    input_arr = list(map(int, input().split()))
    commands = input()
    solve(n, m, input_arr, commands)
