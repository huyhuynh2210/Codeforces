import sys


def solve(n):
    ar=[]
    if n%2==0:
        j = int(n/2)
    else:
        j = n//2 + 1
    for i in range(n, 0, -1):
        if j==0:
            break
        ar.append(j)
        ar.append(i)
        j-=1
        
    for i in range(n):
        print(ar[i], end=' ')
    print('')
    return
    

t = int(sys.stdin.readline().rstrip())

for _ in range(0, t):
    n = int(sys.stdin.readline().strip())
    solve(n)
    
