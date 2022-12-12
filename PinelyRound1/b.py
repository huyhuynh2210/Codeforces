import sys


def solve(n,ar):
    d={}
    for i in ar:
        if i in d:
            d[i]+=1
        else:
            d[i]=1
    
    if min(d.values()) == 1:
        print(n)
        return
    if len(d)==2:
        print(int(n/2+1))
        return
    print(n)
    return
    

t = int(sys.stdin.readline().rstrip())
for _ in range(0, t):
    n = int(sys.stdin.readline().strip())
    ar = list(map(int, sys.stdin.readline().strip().split()))
    solve(n,ar)
    
