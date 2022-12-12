import sys
import math

def solve(n,ar):
    ar=sorted(ar)
    y = round(len(ar)/2)
    a,b = ar[0 : y], ar[y: n]

    arr=[]
    if n%2==0:
        for i in range(0,y):
            arr.append(a[i])
            arr.append(b[i])
    else:
        for i in range(0,y-1):
            arr.append(a[i])
            arr.append(b[i])
        arr.append(a[len(a)-1])   
    arr.extend([arr[0],arr[1]])

    bo=[]
    for i in range(0, len(arr)-2):
        a,b,c = arr[i], arr[i+1], arr[i+2]
        if a>b and c>b:
            bo.append(1)
        if a<b and c<b:
            bo.append(1)
        
    if bo.count(1)==n: 
        print('YES')
        for i in range(n):
            print(arr[i], end = ' ')
        print('')
        return
    print('NO')
    return



t = int(sys.stdin.readline().rstrip())
for _ in range(0, t):
    n = int(sys.stdin.readline().rstrip())
    ar = list(map(int, sys.stdin.readline().strip().split()))

    solve(n,ar)

