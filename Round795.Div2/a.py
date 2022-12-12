import sys

def solve(n,ar):
    le=0
    chan=0
    for i in ar:
        if i%2==0:
            chan+=1
        else:
            le+=1
    
    if chan > le:
        return le
    else: return chan



t = int(sys.stdin.readline().rstrip())
for _ in range(0, t):
    n,m,k = map(int, sys.stdin.readline().rstrip().split())
    a = list(map(str, sys.stdin.readline().strip().split()))
    b = list(map(str, sys.stdin.readline().strip().split()))
    print(a)
    # res = solve(n,m,k,a,b)
    # print(res)
