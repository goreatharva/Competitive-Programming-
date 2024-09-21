def numbers():
    return list(map(int, input().strip().split()))

for _ in range(numbers()[0]):
    matrix = []  
    size = numbers()[0]

    unique_numbers = set()
    for _ in range(size):
        row = input()
        if '1' in row:
            unique_numbers.add(row.count('1'))

    if len(unique_numbers) == 1:
        print("SQUARE")
    else:
        print("TRIANGLE")
