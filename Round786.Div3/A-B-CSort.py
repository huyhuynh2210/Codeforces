import sys


def slove(n, arr):
    a=arr.copy()
    if n%2==0:
        sta=0
    else:sta =1
    for i in range(sta, n, 2):
        if arr[i]>arr[i+1]:
            arr[i], arr[i+1] = arr[i+1], arr[i]
    a=sorted(a)
    if a==arr:
        return 1
    return 0


t = int(sys.stdin.readline().rstrip())
for _ in range(0, t):
    n = int(sys.stdin.readline().rstrip())
    arr = list(map(int, sys.stdin.readline().strip().split()))

    a = slove(n, arr)
    if a==1:
        print('YES')
    else: print('NO')