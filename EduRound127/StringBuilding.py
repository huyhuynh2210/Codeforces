import sys


def split_ab(n):
    arr=[]
    y=0
    for i in range(0,len(n)-1):
        ss=n[i]
        if ss[0]!=n[i+1]:
            arr.append(n[y:i+1])
            y=i+1
    return arr


def slove(arr):
    for i in arr:
        if len(i)==1:
            return 0
    return 1


t = int(sys.stdin.readline())
for _ in range(0, t):
    n = str(sys.stdin.readline())
    
    arr=split_ab(n)
    a=slove(arr)
    if a==1:
        print('YES')
    else: print('NO')
    
