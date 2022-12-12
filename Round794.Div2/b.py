import sys
import math

def solve(n,ar):
    count = 0
    i=0
    while i<n-1:
        if ar[i]>ar[i+1]:
            count +=1
            i+=1
        i+=1
    return count



t = int(sys.stdin.readline().rstrip())
for _ in range(0, t):
    n = int(sys.stdin.readline().rstrip())
    ar = list(map(int, sys.stdin.readline().strip().split()))

    a = solve(n,ar)
    print(a)
