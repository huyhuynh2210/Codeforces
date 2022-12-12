import sys


def solve(n,m,a):
    res= sum(a)-m
    if res>0:
        print(res)
    else:print(0)
    return 



t = int(sys.stdin.readline().rstrip())
for _ in range(0, t):
    n,m = map(int, sys.stdin.readline().rstrip().split())
    a = list(map(int, sys.stdin.readline().strip().split()))
    
    solve(n,m,a)
    