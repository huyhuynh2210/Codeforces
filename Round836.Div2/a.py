import sys


def solve(ar):
    print(ar+ar[::-1])
    return
    

t = int(sys.stdin.readline().rstrip())
for _ in range(0, t):
    ar = str(sys.stdin.readline().strip())
    solve(ar)
    
