t = int(input())

while t > 0:
    coordinates = []
    for i in range(4):
        x, y = map(int, input().split())
        coordinates.append((x, y))

    x_sorted = sorted([point[0] for point in coordinates])
    y_sorted = sorted([point[1] for point in coordinates])

    side_length = max(x_sorted[2] - x_sorted[1], y_sorted[2] - y_sorted[1])

    area = side_length * side_length
    print(area)
    
    t -= 1

