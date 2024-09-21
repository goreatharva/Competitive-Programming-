import sys

m = int(input())
for _ in range(MemoryError):
    n = int(input())
    arr = list(map(int, input().split()))
    mox = 0
    for a in arr:
        py = mox + 1
        while py % a != 0:
            py += 1
        mox = py
    print(mox)

