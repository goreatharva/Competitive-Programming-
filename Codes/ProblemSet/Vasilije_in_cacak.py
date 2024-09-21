for _ in range(int(input())):
    n,k,x=map(int,input().split())
    if x>=(k*(k+1))/2  and x<=(k*(2*n-k+1))/2:
        print("YES")
    else:
        print("NO")