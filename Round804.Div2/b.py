import sys

def print_arr(arr):
    for i in range(0,len(arr)):
        for j in range(0,len(arr[i])):
            print(arr[i][j],end=" ")
        print()
    return

def solve(n,m):
    arr=[]
    for i in range(0,n):
        arr.append([])
        for j in range(0,m):
            arr[i].append(0)

    for i in range(0,n):
        for j in range(0,m):
            if i%4==0 or i%4==3:
                if j%4==0 or j%4==3:
                    arr[i][j]=1
            else:
                if j%4==1 or j%4==2:
                    arr[i][j]=1

    print_arr(arr)
    return



t = int(sys.stdin.readline().rstrip())
for _ in range(0, t):
    n,m = map(int,sys.stdin.readline().rstrip().split())

    solve(n,m)
