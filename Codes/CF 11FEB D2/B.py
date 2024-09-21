import sys

def main():
    d = int(input())
    while d > 0:
          #d += 1
        #n = int(input())
        d -= 1
        n = int(input())
        input_line = input()
        v = [int(s) for s in input_line.split()]
        se = set(v)
        l = sorted(se)
        k = len(v)
        n = len(l)
        ans = 1
        for i in range(n):
            en = l[i] + k - 1
            it = len([x for x in l if x > en]) - i
            if ans < it:
                ans = it
        print(ans)

if __name__ == "__main__":
    main()

