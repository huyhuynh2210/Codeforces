import sys
import math

def solve(n,ar):
    arr=ar.copy()
    tb= float(sum(arr)/n)
    a = ar.count(tb)
    if a>0:
        return 'YES'
    return "NO"



t = int(sys.stdin.readline().rstrip())
for _ in range(0, t):
    n = int(sys.stdin.readline().rstrip())
    ar = list(map(float, sys.stdin.readline().strip().split()))

    a = solve(n,ar)
    print(a)
