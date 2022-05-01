import sys
t = int(sys.stdin.readline())

def slove(n,m,arr):
    if m/n<2:
        return 0
    arr.sort()
    sum=0
    for i in range(1,n):
        sum = sum + arr[i]
    sum = sum + arr[len(arr)-1] + n
    if sum <= m:
        return 1
    else: return 0

for _ in range(0, t):
    n,m = map(int, sys.stdin.readline().strip().split())
    arr = list(map(int, sys.stdin.readline().strip().split()))

    a=slove(n,m,arr)
    if a==0: 
        print('NO')
    else: print('YES')