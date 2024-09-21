def determine_winner(a, b):
    if (a - b) % 2 == 0:
        return "Bob"
    else:
        return "Alice"

t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    winner = determine_winner(a, b)
    print(winner)
