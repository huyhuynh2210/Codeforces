import sys


def solve(n,m):
    sum = 0
    for i in range(1,m+1):
        sum += i
    for i in range(2,n+1):
        sum += m*i
    print(sum)
    return



t = int(sys.stdin.readline().rstrip())
for _ in range(0, t):
    n,m = map(int,sys.stdin.readline().rstrip().split())
    
    solve(n,m)
    