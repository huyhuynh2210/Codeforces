import sys


def solve(n):
    if n==2:
        print('2 1')
        return
    if n==3:
        print(-1)
        return
    arr=[]
    m = int(n/2)
    for i in range(0, n):
        if i>=m:
            arr.append(i-m+1)
        else: 
            arr.append(n-i)
    
    for i in arr:
        print(i, end =' ')
    print()
    return



t = int(sys.stdin.readline().rstrip())
for _ in range(0, t):
    n = int(sys.stdin.readline().rstrip())

    solve(n)
