import sys
import math

def slove(n,m,a,b):
    sum_b=sum(b)
    i=sum_b%n
    print(a[i])

    return


t = int(sys.stdin.readline().rstrip())
for _ in range(0, t):
    n = int(sys.stdin.readline().rstrip())
    a = list(map(int, sys.stdin.readline().rstrip().split()))
    m = int(sys.stdin.readline().rstrip())
    b = list(map(int, sys.stdin.readline().rstrip().split()))

    slove(n,m,a,b)
    
