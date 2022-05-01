import sys
t = int(sys.stdin.readline())

def slove(n, arr):
    count=0
    booll=1
    for i in arr:
        if i=='':
            count=count+1
        else: 
            if 'R'in i and 'B' in i:
                booll=1
            else: 
                return 0
    if count==n:
        booll=1
    return booll

for _ in range(0, t):
    n = int(sys.stdin.readline())
    arr = list(map(str, sys.stdin.readline().strip().split('W')))
    a=slove(n, arr)
    if a==1:
        print("YES")
    else: 
        print("NO")