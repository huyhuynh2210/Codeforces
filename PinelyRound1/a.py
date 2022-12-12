import sys


def solve(n,a,b):
    if n==a and n==b:
        print('YES')
        return
    if n-a-b>=2:
        print('YES')
        return
    print('NO')
    return
    

t = int(sys.stdin.readline().rstrip())
for _ in range(0, t):
    n,a,b = map(int, sys.stdin.readline().strip().split())
    solve(n,a,b)
    
