import sys


def solve(n, ar):
    if ar[0] > min(ar[1::]):
        print("Alice")
    else:
        print("Bob")
    return
    

t = int(sys.stdin.readline().rstrip())
for _ in range(0, t):
    n = int(sys.stdin.readline().strip())
    ar = list(map(int, sys.stdin.readline().strip().split()))
    solve(n, ar)
    
