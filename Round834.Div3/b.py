import sys


def solve(m, s, ar):
    i=1
    while s>0:
        if i not in ar:
            s-=i
            ar.append(i)
        i+=1
    
    if s==0 and max(ar)==len(ar):
        print('YES')
    else:
        print('NO')
    return
    

t = int(sys.stdin.readline().rstrip())
for _ in range(0, t):
    m, s = map(int, sys.stdin.readline().strip().split())
    ar = list(map(int, sys.stdin.readline().strip().split()))
    solve(m,s,ar)
    
