from audioop import reverse
import sys


def solve(a):
    a.sort(reverse = 1)
    if a[0] == a[1]+a[2]:
        print('YES')
    else:
        print('NO')
    
    return
    



t = int(sys.stdin.readline().rstrip())
for _ in range(0, t):
    a = list(map(int, sys.stdin.readline().strip().split()))
    solve(a)
