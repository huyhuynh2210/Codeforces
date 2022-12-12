import sys
import math

def slove(n,m,a,b):
    max_a=max(a)
    max_b=max(b)
    #Alice first
    if max_a>=max_b:
        print('Alice')
    else:
        print('Bob')
    #Bob first
    if max_b>=max_a:
        print('Bob')
    else:
        print('Alice')
    return


t = int(sys.stdin.readline().rstrip())
for _ in range(0, t):
    n = int(sys.stdin.readline().rstrip())
    a = list(map(int, sys.stdin.readline().rstrip().split()))
    m = int(sys.stdin.readline().rstrip())
    b = list(map(int, sys.stdin.readline().rstrip().split()))

    slove(n,m,a,b)
    
