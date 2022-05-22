import sys
import math

def slove(arr):
    if len(arr)==2:
        return arr[len(arr)-1]
    while len(arr)!=1:
        min_index=arr.index(min(arr))
        arr[len(arr)-2], arr[min_index] = arr[min_index], arr[len(arr)-2]
        arr.pop()
    return arr[0]


t = int(sys.stdin.readline().rstrip())
for _ in range(0, t):
    n = str(sys.stdin.readline().rstrip())
    ar=[int(n[i]) for i in range(len(n))]

    a = slove(ar)
    print(a)
