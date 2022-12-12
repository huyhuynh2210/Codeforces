import sys


def solve(n, ar):
    while 0 in ar:
        ar.remove(0)
    
    am=[0]
    duong=[0]
    for i in ar:
        if i<0:
            am.append((-1)*i)
        else:
            duong.append(i)
    
    if sum(duong)>= sum(am):
        print(abs(sum(ar)-min(am)))
        return
    else:
        print(abs(sum(ar)-min(duong)))
        return
    

t = int(sys.stdin.readline().rstrip())
for _ in range(0, t):
    n = int(sys.stdin.readline().strip())
    ar = list(map(int, sys.stdin.readline().strip().split()))
    solve(n, ar)
    
