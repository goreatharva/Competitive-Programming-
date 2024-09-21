def lbs(s):
    max_length = 0
    current_length = 1

    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            current_length += 1
        else:
            max_length = max(max_length, current_length)
            current_length = 1

    max_length = max(max_length, current_length)
    return max_length


t = int(input())

for _ in range(t):
    n, q = map(int, input().split())
    string = input()
    lengths = [lbs(string)]
   
    for _ in range(q):
        char = input()
        string += char
        lengths.append(lbs(string))

    print(*lengths)
