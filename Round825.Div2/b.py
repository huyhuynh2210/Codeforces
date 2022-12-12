import sys

def solve(n, arr):
    if n<=2:
        print('YES')
        return
    
    ar = arr.copy()
    arr.sort(reverse=1)
    if ar==arr:
        print('YES')
        return
    else:
        print('NO')
        return
    return



t = int(sys.stdin.readline().rstrip())
for _ in range(0, t):
    n = int(sys.stdin.readline().rstrip())
    arr = list(map(int, sys.stdin.readline().rstrip().split()))
    solve(n, arr)
