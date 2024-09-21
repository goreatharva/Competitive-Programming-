from itertools import accumulate

def Main():
    n = int(input())
    A = list(map(int, input().split()))

  
    acc = list(accumulate(A))
    
    
    min_acc = min(acc)
    
    
    first_adjustment = max(0, -min_acc)

    
    result = acc[-1] + first_adjustment

    print(result)
