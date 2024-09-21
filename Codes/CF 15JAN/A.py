
def calculate_square_area(x1, y1, x2, y2, x3, y3, x4, y4):
    side_length = max(x1, x2, x3, x4) - min(x1, x2, x3, x4)
    return side_length ** 2


t = int(input())


for _ in range(t):
  
    x1, y1 = map(int, input().split())
    x2, y2 = map(int, input().split())
    x3, y3 = map(int, input().split())
    x4, y4 = map(int, input().split())
    
 
    area = calculate_square_area(x1, y1, x2, y2, x3, y3, x4, y4)
    print(area)
