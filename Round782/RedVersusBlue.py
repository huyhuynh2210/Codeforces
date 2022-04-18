import sys
t = int(sys.stdin.readline())

def slove(n,r,b):
    arr=[0]*(b+1)
    i=0
    while i<r:
        for y in range(0,len(arr)):
            arr[y]=arr[y]+1
            i=i+1
            if i==r:
                return arr

for _ in range(0, t):
    n,r,b = map(int, sys.stdin.readline().strip().split())
    arr= slove(n,r,b)
    arr_res=[]
    for i in range(0, len(arr)):
        arr_res= arr_res+ ['R']*(arr[i])
        arr_res=arr_res+['B']
    arr_res.pop()
    
    for i in range(0, len(arr_res)):
        print(arr_res[i], end='')
    print('')