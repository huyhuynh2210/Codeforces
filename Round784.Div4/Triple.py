import sys
t = int(sys.stdin.readline())

def slove(n, arr):
    b=dict()
    count=0
    for i in arr:
        if i in b:
            b[i] += 1
        else:
            b[i] = 1
    for i in b:
        if b[i]>=3:
            print(i)
            count = count +1
            return
    if count==0:
        print('-1')
    return


for _ in range(0, t):
    n = int(sys.stdin.readline())
    arr = list(map(int, sys.stdin.readline().strip().split()))
    slove(n, arr)