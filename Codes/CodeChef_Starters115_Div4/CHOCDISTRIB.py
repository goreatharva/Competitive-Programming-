def calculate_children(N):

    min_children = N
  
    if N % 2 == 0:
        max_children = N // 2
    else:
        max_children = (N // 2) + 1
    return min_children, max_children


T = int(input())


for _ in range(T):
    N = int(input())
    min_children, max_children = calculate_children(N)
    print(max_children, min_children)
