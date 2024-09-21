import math as m

t=int(input())
for _ in range(t):
  x, n=map(int, input().split())
  q=x//n
  st=set()
  for i in range(1,int(x**0.5)+1):
    if x%i==0:
      st.add(i)
      st.add(x//i)
  it=iter(sorted(st))
  for val in it:
    if val>q:
      r=pr
      break
    pr=val
  print(r)
