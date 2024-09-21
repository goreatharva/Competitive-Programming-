T=int(input())
from collections import deque  
from sys import stdin
 
for t in range(T):
  S=stdin.readline()[:-1]
  U=stdin.readline()[:-1]
  if U=='a':
    print(1)
  elif 'a' in U:
    print(-1)
  else:
    a=S.count('a')
    print(pow(2,a))
