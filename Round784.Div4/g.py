import sys
t = int(sys.stdin.readline())


def slove(n, m, arr):
    for i in range(m):
        ar=arr[i][0:n]
        print(ar)
    return


for _ in range(0, t):
    n, m = map(int, sys.stdin.readline().rstrip().split())
    arr = []
    for _ in range(n):
        arr.append((list(input().rstrip())))
    print(arr)
    slove(n, m, arr)
