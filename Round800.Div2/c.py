import sys

def prefix_sum(arr):
    for i in range(1,len(arr)):
        arr[i] += arr[i-1]
    return arr

def solve(n,ar):
    arr=prefix_sum(ar)
    while True:
        if len(arr)==1:
            break
        
        if arr[len(arr)-1]==0:
            if arr[len(arr)-2]!=0:
                break
            else:
                arr.pop()
        else:
            break
    boo=1
    for i in range(len(arr)-1):
        if arr[i]<=0:
            boo=0
            break
    boo1=1
    if arr[len(arr)-1]!=0:
        boo1=0

    if boo==1 and boo1==1:
        print('yes')
    else:
        print('no')
    return



t = int(sys.stdin.readline().rstrip())
for _ in range(0, t):
    n = int(sys.stdin.readline().rstrip())
    ar = list(map(int, sys.stdin.readline().rstrip().split()))
    
    solve(n,ar)
    