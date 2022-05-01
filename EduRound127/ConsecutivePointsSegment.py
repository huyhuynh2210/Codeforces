import sys


def slove(n, arr):
    
    return arr[n-1]-arr[0]-n +1


t = int(sys.stdin.readline())
for _ in range(0, t):
    n = int(sys.stdin.readline())
    arr = list(map(int, sys.stdin.readline().strip().split()))

    a = slove(n, arr)
    if a <=2:
        print('YES')
    else:
        print('NO')
