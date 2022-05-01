import sys
t = int(sys.stdin.readline())

def slove(n, arr):
    bool1=1
    le=0
    chan=0
    for i in range(0,n,2):
        if arr[i]%2==1:
            le=le+1
        else: chan=chan+1
    if chan==0 or le==0:
        bool1=1
    else: bool1=0

    le=0
    chan=0
    bool2=1
    for i in range(1,n,2):
        if arr[i]%2==1:
            le=le+1
        else: chan=chan+1
    if chan==0 or le==0:
        bool2=1
    else: bool2=0
    if bool1==1 and bool2==1:
        print('YES')
    else: print('NO')


for _ in range(0, t):
    n = int(sys.stdin.readline())
    arr = list(map(int, sys.stdin.readline().strip().split()))
    slove(n, arr)