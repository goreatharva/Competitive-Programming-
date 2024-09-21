n = int(input())
x_levels = set(map(int, input().split()[1:]))
y_levels = set(map(int, input().split()[1:]))
if x_levels.union(y_levels) == set(range(1, n+1)):
    print("I become the guy.")
else:

    print("Oh, my keyboard!")