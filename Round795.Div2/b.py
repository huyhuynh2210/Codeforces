import sys

def ss(aarr):
    ar_res=[]
    idx=0
    y=0
    while idx<len(aarr):
        while y<len(aarr) and aarr[idx]==aarr[y]:
            y +=1
        ar_res.append(idx)
        ar_res.append(y-1)
        idx=y

    return ar_res

def solve(n,arr):
    ar=ss(arr)
    
    res=[]
    for i in range(0, len(ar),2):
        start = ar[i]
        end = ar[i+1]
        if start != end:
            for x in range(start+1, end+1):
                res.append(x)
            res.append(start)
        else: res.append(-1)

    if -1 in res:
        print(-1)
        return
    else:
        for i in res:
            print(i+1, end=' ')
        print('')
        return 



t = int(sys.stdin.readline().rstrip())
for _ in range(0, t):
    n = int(sys.stdin.readline().rstrip())
    ar = list(map(int, sys.stdin.readline().strip().split()))

    solve(n,ar)
