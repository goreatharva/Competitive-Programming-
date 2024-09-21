t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    time = 0
    last_digit = 0
    for i in range(n):
        if s[i] != '0':
            time += int(s[i]) + 1  # Add the digit value and +1 sec to reset it to zero
            last_digit = i  # store the position of the last non-zero digit
    # Reduce the second that was added extra for last digit '0'
    if s[last_digit] != '0':
        time -= 1
    print(time)
