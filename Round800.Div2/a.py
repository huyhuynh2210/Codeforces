import sys


def solve(a,b):
    if a<=b:
        print('01'*a+'1'*(b-a))
    else:
        print('01'*b+'0'*(a-b))
    
    return 



t = int(sys.stdin.readline().rstrip())
for _ in range(0, t):
    a,b = map(int, sys.stdin.readline().rstrip().split())
    
    
    solve(a,b)
    