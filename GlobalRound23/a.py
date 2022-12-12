import sys

def solve(a, n, k):
    if 1 in a:
        print('YES')
    else: print('NO')
    return


t = int(sys.stdin.readline().rstrip())
for _ in range(0, t):
    n, k = map(int, sys.stdin.readline().rstrip().split())
    a = list(map(int, sys.stdin.readline().strip().split()))
    solve(a, n, k)
