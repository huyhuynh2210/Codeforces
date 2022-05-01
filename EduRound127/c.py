import sys


def slove(n, x, arr):
    count =0
    if x< min(arr):
        return count
    
    return 


t = int(sys.stdin.readline())
for _ in range(0, t):
    n, x = map(int, sys.stdin.readline().strip().split())
    arr = list(map(int, sys.stdin.readline().strip().split()))

    a = slove(n, x, arr)
    print(a)
