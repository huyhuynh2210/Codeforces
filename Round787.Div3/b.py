import sys
import math

def slove(n, arr):
    count =0
    for i in range(1,n):
        while arr[n-i]<=arr[n-i-1]:
            arr[n-i-1]=int(arr[n-i-1]/2)
            count+=1
            if arr[n-i-1]==0 and arr[n-i]==0:
                return -1
            if arr[n-i-1]==0 and n-i-1!=0:
                return -1
            elif arr[n-i-1]==0 and n-i-1==0:
                return count

    return count


t = int(sys.stdin.readline().rstrip())
for _ in range(0, t):
    n = int(sys.stdin.readline().rstrip())
    arr = list(map(int, sys.stdin.readline().rstrip().split()))

    a = slove(n, arr)
    print(a)
