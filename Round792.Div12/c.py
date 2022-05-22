import sys
import math

def slove(n, m, arr):
    decreasing = []
    non_decreasing = []
    for i in range(n):
        for j in range(m-1):
            if arr[i][j] <= arr[i][j+1]:
                decreasing.append(1)
            if arr[i][j] >= arr[i][j+1]:
                non_decreasing.append(1)
    if decreasing.count(1)==n*m-n:
        print(1,1)
        return
    if non_decreasing.count(1)==n*m-n:
        print(1,m)
        return
    print(-1)
    return


t = int(sys.stdin.readline().rstrip())
for _ in range(0, t):
    n, m = map(int, sys.stdin.readline().rstrip().split())
    arr=[]
    for _ in range(n):
        arr.append(list(map(int, sys.stdin.readline().rstrip().split())))

    slove(n, m, arr)
    
