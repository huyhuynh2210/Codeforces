import sys

def solve(a, n):
    count=0
    i, j = 0, n-1
    while i<j:
        while i<j and a[i]==0: i+=1
        while i<j and a[j]==1: j-=1
        if i>=j:
            break
        count+=1
        i+=1
        j-=1
         
    print(count)     
    return


t = int(sys.stdin.readline().rstrip())
for _ in range(0, t):
    n = int(sys.stdin.readline().rstrip())
    a = list(map(int, sys.stdin.readline().strip().split()))
    solve(a, n)
