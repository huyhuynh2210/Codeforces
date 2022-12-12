import sys


def solve(n):
    a=b=0
    if n/2==int(n/2):
        c=n/2
    else:
        c=-1
        
    if c==-1:
        print(c)
    else:
        print(a,b,int(c))
    return



t = int(sys.stdin.readline().rstrip())
for _ in range(0, t):
    n = int(sys.stdin.readline().rstrip())

    solve(n)
