h,w,n=map(int,input().split())
G = [["." for j in range(w)] for i in range(h)]

#*def progress(now_h, now_w, dir):
    #if dir == 0:
      #  now_h = (now_h-1)%h
   # elif dir == 1:
    #    now_w = (now_w+1)%w
    #e#lif dir == 5:
      #  now_h = (now_h+1)%h
def progress(now_h, now_w, dir):
    if dir == 0:
        now_h = (now_h-1)%h
    elif dir == 1:
        now_w = (now_w+1)%w
    elif dir == 2:
        now_h = (now_h+1)%h
    else:
        now_w = (now_w-1)%w