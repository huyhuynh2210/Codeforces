from audioop import reverse
import sys


def solve(a, n):
    a.sort()
    for i in range(n-1):
        if a[i]==a[i+1]:
            print('NO')
            return
        
    print('YES')    
    return
    



t = int(sys.stdin.readline().rstrip())
for _ in range(0, t):
    n = int(sys.stdin.readline().strip())
    a = list(map(int, sys.stdin.readline().strip().split()))
    solve(a, n)
