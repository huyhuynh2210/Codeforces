import sys
import math

def slove(n, arr):
    arrgoc=[[]]*(n+1)
    for i in range(1,n+1):
        arrgoc[i].append(i)
    print(arrgoc)


    return 1


t = int(sys.stdin.readline().rstrip())
for _ in range(0, t):
    n = int(sys.stdin.readline().rstrip())
    arr = list(map(int, sys.stdin.readline().rstrip().split()))

    a = slove(n, arr)
    print(a)
