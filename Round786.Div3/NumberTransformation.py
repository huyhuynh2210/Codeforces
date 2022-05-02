import sys
import math

def slove(x,y):
    if y%x==0:
        return 1, int(y/x)
    else: return 0, 0

t = int(sys.stdin.readline().rstrip())
for _ in range(0, t):
    x,y = map(int, sys.stdin.readline().strip().split())

    a,b = slove(x,y)
    print(a, b)