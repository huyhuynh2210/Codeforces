import sys


def solve(n,ar):
    count=1
    if n==1:
        print('1')
        return

    for i in range(1,n):
        if ar[i]!=ar[i-1]:
            count+=i
        count+=1
    print(count)
    return



t = int(sys.stdin.readline().rstrip())
for _ in range(0, t):
    n = int(sys.stdin.readline().rstrip())
    ar = list(map(int, sys.stdin.readline().rstrip()))
    
    
    solve(n,ar)
    